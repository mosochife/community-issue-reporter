# Community Issue Reporter

A web app where residents report community problems such as broken roads, water issues and faulty street lights, and where each report's status can be tracked from Open to Resolved.

Built with Python, Flask and SQLite.

## Features
- Report an issue with title, description, location and category
- View all reported issues, filtered by category
- Open an issue and update its status

## Run locally
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python database.py
5. python app.py
6. Open http://127.0.0.1:5000