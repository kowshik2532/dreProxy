# Deployment Instructions

## Deploy to Render.com (Recommended - Free Tier Available)

### Step 1: Prepare Firebase Credentials
1. Read your Firebase service account JSON file:
   ```bash
   cat dreproxy-2d948-firebase-adminsdk-fbsvc-bbbb1ad6b1.json
   ```
2. Copy the entire JSON content - you'll need it for environment variables

### Step 2: Deploy to Render
1. Go to [Render.com](https://render.com) and sign up/login
2. Click "New +" → "Web Service"
3. Connect your GitHub repository (or use manual deploy)
4. Configure the service:
   - **Name**: agent-management-api
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add Environment Variable:
   - **Key**: `FIREBASE_CREDENTIALS_JSON`
   - **Value**: Paste the entire JSON content from your service account file
6. Click "Create Web Service"
7. Wait for deployment (5-10 minutes)
8. Your app will be available at: `https://agent-management-api.onrender.com` (or your custom name)

## Alternative: Deploy to Railway

1. Go to [Railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add Environment Variable:
   - **Key**: `FIREBASE_CREDENTIALS_JSON`
   - **Value**: Your Firebase JSON content
5. Railway will auto-detect Python and deploy
6. Your app will be available at: `https://your-app-name.up.railway.app`

## Alternative: Deploy to Fly.io

1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `fly auth login`
3. Initialize: `fly launch`
4. Set environment variable:
   ```bash
   fly secrets set FIREBASE_CREDENTIALS_JSON="$(cat dreproxy-2d948-firebase-adminsdk-fbsvc-bbbb1ad6b1.json)"
   ```
5. Deploy: `fly deploy`
6. Your app will be at: `https://your-app-name.fly.dev`

## Quick Deploy Script

Run this to get your Firebase credentials ready:
```bash
python3 -c "import json; print(json.dumps(json.load(open('dreproxy-2d948-firebase-adminsdk-fbsvc-bbbb1ad6b1.json'))))"
```

Copy the output and use it as the `FIREBASE_CREDENTIALS_JSON` environment variable.

