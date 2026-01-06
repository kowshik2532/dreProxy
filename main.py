from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr
from typing import Optional
import firebase_admin
from firebase_admin import credentials, firestore
import os
import glob
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    try:
        service_account_file = None
        # Method 1: Check for individual environment variables (preferred for deployment)
        firebase_type = os.getenv("FIREBASE_TYPE")
        firebase_project_id = os.getenv("FIREBASE_PROJECT_ID")
        firebase_private_key = os.getenv("FIREBASE_PRIVATE_KEY")
        firebase_client_email = os.getenv("FIREBASE_CLIENT_EMAIL")
        
        if firebase_type and firebase_project_id and firebase_private_key and firebase_client_email:
            import json
            import tempfile
            # Build credentials from individual environment variables
            creds_dict = {
                "type": firebase_type,
                "project_id": firebase_project_id,
                "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID", ""),
                "private_key": firebase_private_key.replace('\\n', '\n'),
                "client_email": firebase_client_email,
                "client_id": os.getenv("FIREBASE_CLIENT_ID", ""),
                "auth_uri": os.getenv("FIREBASE_AUTH_URI", "https://accounts.google.com/o/oauth2/auth"),
                "token_uri": os.getenv("FIREBASE_TOKEN_URI", "https://oauth2.googleapis.com/token"),
                "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL", "https://www.googleapis.com/oauth2/v1/certs"),
                "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL", ""),
                "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN", "googleapis.com")
            }
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(creds_dict, f)
                service_account_file = f.name
            print("Using Firebase credentials from individual environment variables")
        
        # Method 2: Check for JSON string in environment variable
        elif os.getenv("FIREBASE_CREDENTIALS_JSON"):
            import json
            import tempfile
            firebase_creds_json = os.getenv("FIREBASE_CREDENTIALS_JSON")
            with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
                json.dump(json.loads(firebase_creds_json), f)
                service_account_file = f.name
            print("Using Firebase credentials from FIREBASE_CREDENTIALS_JSON environment variable")
        
        # Method 3: Check for service account file
        elif os.path.exists("serviceAccountKey.json"):
            service_account_file = "serviceAccountKey.json"
        else:
            # Look for dreproxy-*.json files
            dreproxy_files = glob.glob("dreproxy-*.json")
            if dreproxy_files:
                service_account_file = dreproxy_files[0]
                print(f"Found Firebase service account: {service_account_file}")
        
        if service_account_file:
            cred = credentials.Certificate(service_account_file)
            firebase_admin.initialize_app(cred)
            print(f"Firebase initialized successfully")
        else:
            # Try to use Application Default Credentials (for GCP environments)
            try:
                cred = credentials.ApplicationDefault()
                firebase_admin.initialize_app(cred)
                print("Firebase initialized with Application Default Credentials")
            except Exception:
                print("Warning: Firebase credentials not found.")
                print("Please set environment variables or add serviceAccountKey.json to the root directory.")
                print("The app will start but Firebase operations will fail until credentials are added.")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        print("Please ensure Firebase credentials are properly configured.")

try:
    # Use default database - if you created a named database, change "(default)" to your database ID
    # For example: db = firestore.client(database="your-database-id")
    db = firestore.client()  # This connects to the "(default)" database
    print("Firestore client initialized successfully (using default database)")
except Exception as e:
    error_msg = str(e)
    if "does not exist" in error_msg or "404" in error_msg:
        print(f"\n⚠️  Firestore Database Error: {error_msg}")
        print("\n📋 To fix this:")
        print("   1. Visit: https://console.cloud.google.com/datastore/setup?project=dreproxy-2d948")
        print("   2. Click 'Create Database'")
        print("   3. Choose a location for your database")
        print("   4. Select 'Firestore in Native mode' (recommended)")
        print("   5. Wait a few minutes for the database to be created")
        print("\n   Alternatively, visit: https://console.firebase.google.com/project/dreproxy-2d948/firestore")
    else:
        print(f"Warning: Could not initialize Firestore client: {e}")
    db = None

app = FastAPI(title="Agent Management API")

# CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Pydantic models for request/response
class Agent(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    licence_number: str

class AgentResponse(Agent):
    id: str

@app.get("/")
async def read_root():
    return RedirectResponse(url="/static/index.html")

@app.post("/api/agents", response_model=AgentResponse)
async def create_agent(agent: Agent):
    """Create a new agent"""
    if db is None:
        raise HTTPException(
            status_code=503, 
            detail="Firestore database not initialized. Please create a Firestore database at https://console.cloud.google.com/datastore/setup?project=dreproxy-2d948"
        )
    try:
        # Add agent to Firestore
        doc_ref = db.collection("agents").document()
        agent_data = agent.dict()
        doc_ref.set(agent_data)
        
        # Return the created agent with ID
        return AgentResponse(id=doc_ref.id, **agent_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agents", response_model=list[AgentResponse])
async def get_agents():
    """Get all agents"""
    if db is None:
        raise HTTPException(
            status_code=503, 
            detail="Firestore database not initialized. Please create a Firestore database at https://console.cloud.google.com/datastore/setup?project=dreproxy-2d948"
        )
    try:
        agents = []
        docs = db.collection("agents").stream()
        for doc in docs:
            agent_data = doc.to_dict()
            agents.append(AgentResponse(id=doc.id, **agent_data))
        return agents
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agents/{agent_id}", response_model=AgentResponse)
async def get_agent(agent_id: str):
    """Get a specific agent by ID"""
    if db is None:
        raise HTTPException(
            status_code=503, 
            detail="Firestore database not initialized. Please create a Firestore database at https://console.cloud.google.com/datastore/setup?project=dreproxy-2d948"
        )
    try:
        doc = db.collection("agents").document(agent_id).get()
        if not doc.exists:
            raise HTTPException(status_code=404, detail="Agent not found")
        agent_data = doc.to_dict()
        return AgentResponse(id=doc.id, **agent_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/agents/{agent_id}", response_model=AgentResponse)
async def update_agent(agent_id: str, agent: Agent):
    """Update an existing agent"""
    if db is None:
        raise HTTPException(
            status_code=503, 
            detail="Firestore database not initialized. Please create a Firestore database at https://console.cloud.google.com/datastore/setup?project=dreproxy-2d948"
        )
    try:
        doc_ref = db.collection("agents").document(agent_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="Agent not found")
        
        doc_ref.update(agent.dict())
        updated_data = doc_ref.get().to_dict()
        return AgentResponse(id=agent_id, **updated_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/agents/{agent_id}")
async def delete_agent(agent_id: str):
    """Delete an agent"""
    if db is None:
        raise HTTPException(
            status_code=503, 
            detail="Firestore database not initialized. Please create a Firestore database at https://console.cloud.google.com/datastore/setup?project=dreproxy-2d948"
        )
    try:
        doc_ref = db.collection("agents").document(agent_id)
        if not doc_ref.get().exists:
            raise HTTPException(status_code=404, detail="Agent not found")
        
        doc_ref.delete()
        return {"message": "Agent deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

