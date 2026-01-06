# Quick Deployment Guide

## 🚀 Deploy to Render.com (5 minutes)

### Step 1: Get Firebase Credentials
Your Firebase credentials are ready in: `firebase_creds_compact.json`

### Step 2: Deploy to Render

1. **Go to Render**: https://render.com
   - Sign up (free) or login
   
2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo OR use "Public Git repository"
   - If using public repo, paste: `https://github.com/YOUR_USERNAME/dreproxy` (or upload manually)

3. **Configure Service**:
   ```
   Name: agent-management-api
   Environment: Python 3
   Region: Choose closest to you
   Branch: main (or master)
   Root Directory: . (leave empty)
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

4. **Add Environment Variable**:
   - Click "Advanced" → "Add Environment Variable"
   - Key: `FIREBASE_CREDENTIALS_JSON`
   - Value: Copy the entire content from `firebase_creds_compact.json` file
   - Click "Add"

5. **Deploy**:
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment

6. **Your URL**:
   - After deployment, your app will be at:
   - `https://agent-management-api.onrender.com`
   - (or `https://YOUR-SERVICE-NAME.onrender.com` if you used a different name)

## ✅ Verify Deployment

Once deployed, test:
- Frontend: `https://YOUR-URL.onrender.com`
- API: `https://YOUR-URL.onrender.com/api/agents`
- Docs: `https://YOUR-URL.onrender.com/docs`

## 🔧 Alternative: Railway (Even Faster)

1. Go to https://railway.app
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add Environment Variable:
   - Key: `FIREBASE_CREDENTIALS_JSON`
   - Value: Content from `firebase_creds_compact.json`
5. Railway auto-detects Python and deploys
6. Your URL: `https://YOUR-APP.up.railway.app`

## 📝 Get Firebase Credentials Value

Run this command to get the credentials value:
```bash
cat firebase_creds_compact.json
```

Copy the entire output and paste it as the `FIREBASE_CREDENTIALS_JSON` environment variable value.

