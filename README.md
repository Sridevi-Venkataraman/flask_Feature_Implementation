## Project Title
PAssword MAnagement with Flask application

---

## Description
 A basic in-memory store where users can save a username and password, and retrieve the password later by username. 

---

## Installation and Setup

Follow these steps to run the app locally:

bash
# 1. Clone the repository
git@github.com:Sridevi-Venkataraman/flask_Feature_Implementation.git
cd flask-Feature_Impementation

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# 3. Run the app
python app.py

---

## API Endpoint Reference

 # Accepts JSON body with a username and password field and stores them 
http://127.0.0.1:5000/add?username=ganesh&password=secret234   

# Returns the stored password for that username, or an appropriate error if the username does not exist 
http://127.0.0.1:5000/get/username   

---

## GIT Workflow

1. We have used two branches.
2. Work is done in dev
3. Once tested, changes are merged into main (Stable production-ready code)
4. GitHub shows both branches, and merge history tracks releases.

---

## Version History
v1.0	Initial Flask app with basic routes
V2.0    With newly added routes
---

## Screenshots



---




