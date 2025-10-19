⚛️ CGAI Frontend — Project Setup Guide

This is the frontend for the CGAI Project, built with React.
It communicates with a Django REST backend and uses Firebase for authentication.

🧩 1. Firebase & Environment Setup (CRITICAL)

Before running the project, you must set up Firebase and create a .env file.

🔥 Step A: Get Your Firebase Config

Go to the Firebase Console
.

Open your CGAI project.

Click the ⚙️ Settings icon → Project Settings.

Under the General tab, scroll down to Your apps.

Select your Web app (the one with the </> icon).

Find the firebaseConfig object — it looks like this:

const firebaseConfig = {
  apiKey: "AIzaSy***************",
  authDomain: "your-app.firebaseapp.com",
  projectId: "your-app",
  storageBucket: "your-app.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abcdef123456",
  measurementId: "G-XXXXXXX"
};


You’ll need these values for your .env file.

⚙️ Step B: Create Your .env File

In the frontend root folder (same level as package.json), create a new file named .env.

Paste the following template and replace the placeholders with your Firebase credentials:

# --- React App Firebase Config ---
# Get these values from your Firebase project settings
REACT_APP_FIREBASE_API_KEY="YOUR_FIREBASE_API_KEY_HERE"
REACT_APP_FIREBASE_AUTH_DOMAIN="YOUR_FIREBASE_AUTH_DOMAIN_HERE"
REACT_APP_FIREBASE_PROJECT_ID="YOUR_FIREBASE_PROJECT_ID_HERE"
REACT_APP_FIREBASE_STORAGE_BUCKET="YOUR_FIREBASE_STORAGE_BUCKET_HERE"
REACT_APP_FIREBASE_MESSAGING_SENDER_ID="YOUR_FIREBASE_SENDER_ID_HERE"
REACT_APP_FIREBASE_APP_ID="YOUR_FIREBASE_APP_ID_HERE"
REACT_APP_FIREBASE_MEASUREMENT_ID="YOUR_FIREBASE_MEASUREMENT_ID_HERE"

# --- Backend API URL ---
# This should point to your local Django backend API
REACT_APP_API_BASE_URL=http://127.0.0.1:8000/api


💡 Pro Tip:
Make sure .env is listed in your .gitignore file so your secrets aren’t pushed to GitHub.

🧰 2. Available Scripts

Once your .env file is ready, you can install and run the project.

📦 Install Dependencies

Run this once to install all the required dependencies:

npm install

⚡ Start the Development Server

Launch the app in development mode:

npm start


This will automatically open the app at:
👉 http://localhost:3000/

⚠️ Important Note

If your app was already running when you created or modified the .env file:

Stop the server with Ctrl + C

Then restart it with npm start
Otherwise, your new environment variables won’t be loaded.

🧠 You’re All Set!

You now have:

🔥 Firebase Authentication configured

⚙️ React frontend connected to Django backend

💻 A clean environment setup ready for development