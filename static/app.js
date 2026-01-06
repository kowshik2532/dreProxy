// Use relative URL for API - works in both local and deployed environments
const API_BASE_URL = window.location.origin + '/api';

// Store all agents for search functionality
let allAgents = [];

// Navigation functionality
document.addEventListener('DOMContentLoaded', () => {
    const navItems = document.querySelectorAll('.nav-item');
    const pages = document.querySelectorAll('.page');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetPage = item.getAttribute('data-page');

            // Update active nav item
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            // Show target page
            pages.forEach(page => page.classList.remove('active'));
            document.getElementById(`${targetPage}-page`).classList.add('active');

            // Load agents if on list page
            if (targetPage === 'list') {
                loadAgents();
            }
        });
    });

    // Form submission
    const agentForm = document.getElementById('agent-form');
    agentForm.addEventListener('submit', handleFormSubmit);

    // Reset button
    const resetBtn = document.getElementById('reset-btn');
    resetBtn.addEventListener('click', () => {
        agentForm.reset();
        hideMessage();
    });

    // Refresh button
    const refreshBtn = document.getElementById('refresh-btn');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', loadAgents);
    }

    // Search input
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', handleSearch);
    }
});

// Handle form submission
async function handleFormSubmit(e) {
    e.preventDefault();
    hideMessage();

    const formData = new FormData(e.target);
    const agentData = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone_number: formData.get('phone_number'),
        licence_number: formData.get('licence_number')
    };

    try {
        const response = await fetch(`${API_BASE_URL}/agents`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(agentData)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to create agent');
        }

        const result = await response.json();
        showMessage('Agent created successfully!', 'success');
        e.target.reset();
        
        // Optionally switch to list page
        setTimeout(() => {
            document.querySelector('[data-page="list"]').click();
        }, 1500);
    } catch (error) {
        showMessage(`Error: ${error.message}`, 'error');
    }
}

// Load and display agents
async function loadAgents() {
    const agentsList = document.getElementById('agents-list');
    agentsList.innerHTML = '<p class="loading">Loading agents...</p>';

    try {
        const response = await fetch(`${API_BASE_URL}/agents`);
        
        if (!response.ok) {
            throw new Error('Failed to load agents');
        }

        allAgents = await response.json();
        
        // Apply current search filter if any
        const searchInput = document.getElementById('search-input');
        if (searchInput && searchInput.value.trim()) {
            filterAndDisplayAgents(searchInput.value.trim());
        } else {
            displayAgents(allAgents);
        }
    } catch (error) {
        agentsList.innerHTML = `<p class="error">Error loading agents: ${error.message}</p>`;
    }
}

// Handle search input
function handleSearch(e) {
    const searchQuery = e.target.value.trim().toLowerCase();
    filterAndDisplayAgents(searchQuery);
}

// Filter and display agents based on search query
function filterAndDisplayAgents(searchQuery) {
    const agentsList = document.getElementById('agents-list');
    
    if (!searchQuery) {
        displayAgents(allAgents);
        return;
    }

    const filteredAgents = allAgents.filter(agent => {
        const name = (agent.name || '').toLowerCase();
        const email = (agent.email || '').toLowerCase();
        const phone = (agent.phone_number || '').toLowerCase();
        const licence = (agent.licence_number || '').toLowerCase();
        
        return name.includes(searchQuery) || 
               email.includes(searchQuery) || 
               phone.includes(searchQuery) || 
               licence.includes(searchQuery);
    });

    displayAgents(filteredAgents);
}

// Display agents in the list
function displayAgents(agents) {
    const agentsList = document.getElementById('agents-list');
    
    if (agents.length === 0) {
        agentsList.innerHTML = '<p class="empty-state">No agents found. Add an agent using the form.</p>';
        return;
    }

    agentsList.innerHTML = agents.map(agent => `
        <div class="agent-card">
            <h3>${escapeHtml(agent.name)}</h3>
            <p><span class="label">Email:</span> ${escapeHtml(agent.email)}</p>
            <p><span class="label">Phone:</span> ${escapeHtml(agent.phone_number)}</p>
            <p><span class="label">Licence Number:</span> ${escapeHtml(agent.licence_number)}</p>
        </div>
    `).join('');
}

// Utility functions
function showMessage(message, type) {
    const messageEl = document.getElementById('form-message');
    messageEl.textContent = message;
    messageEl.className = `message ${type}`;
}

function hideMessage() {
    const messageEl = document.getElementById('form-message');
    messageEl.className = 'message';
    messageEl.textContent = '';
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

