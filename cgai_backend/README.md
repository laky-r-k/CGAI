🚀 CGAI Backend — Project Setup Guide

This is the backend for the CGAI Project, built with Django REST Framework and Firebase Authentication.
Follow this guide carefully to get your local environment up and running.

🧩 1. Prerequisites (CRITICAL)

Before running the backend, you must obtain two secret files and create one manually.

🔑 A. Get the Firebase Admin Key

Go to the Firebase Console
.

Open the CGAI project.

Click the ⚙️ Settings icon → Project Settings → Service accounts tab.

Click “Generate new private key” → download the JSON file.

Rename it to:

serviceAccountKey.json


Move this file into the project root folder (same level as manage.py).

📁 Example structure:

cgai_backend/
├── manage.py
├── .env
├── serviceAccountKey.json
└── ...

⚙️ B. Create the .env File

This file contains all your secret keys and environment variables.

In the project root folder, create a file named .env

Paste the following content:

# --- Django Core ---
# ⚠️ Replace this with the real key from the project admin (Lakshmish)
SECRET_KEY='django-insecure-YOUR-REAL-KEY-GOES-HERE'
DEBUG=True

# --- Database (optional, for future use) ---
# DB_NAME='your_db_name'
# DB_USER='your_db_user'
# DB_PASSWORD='your_db_password'

🧠 2. Local Backend Setup

Once your secrets are in place, you can set up the Python environment.

🐍 Step 1: Create and Activate Virtual Environment

Keep your dependencies isolated from your system packages.

# Create the virtual environment
python3 -m venv venv

# Activate it
# On macOS / Linux:
source venv/bin/activate

# On Windows (Git Bash):
source venv/Scripts/activate


✅ You should now see (venv) at the start of your terminal prompt.

📦 Step 2: Install Dependencies

Install all required packages listed in requirements.txt:

(venv) $ pip install -r requirements.txt

🗃️ Step 3: Create the Local Database

Run Django migrations to create the db.sqlite3 database:

(venv) $ python manage.py migrate

🌐 3. Run the Development Server

You’re all set! Start the local Django server:

(venv) $ python manage.py runserver


Your backend API is now live at:
👉 http://127.0.0.1:8000/

✅ You’re Ready to Go!

You now have:

🔥 Firebase Authentication integrated

🧱 Django REST Framework backend

🛠️ Local environment set up for development