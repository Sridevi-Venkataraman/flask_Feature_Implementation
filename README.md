## Project Title
Password Management with Flask application

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

# Remove the specified user's record from storage and confirm deletion. If the username does not exist, return an appropriate error message. 
http://127.0.0.1:5000/delete/<username>

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

# Add User
<img width="965" height="390" alt="addUser" src="https://github.com/user-attachments/assets/0cdb8b77-25ed-49f7-a0cd-092ab1c644a9" />

# Get User
<img width="981" height="402" alt="getUserdetails" src="https://github.com/user-attachments/assets/c37eadbe-d2e0-4202-a7a9-6d53be2341ef" />

# Unknown User
<img width="827" height="312" alt="Unknownuser" src="https://github.com/user-attachments/assets/fa7eefa3-5865-4561-9d2c-e42f0d01d2fb" />

# Delete User
<img width="952" height="352" alt="deleteUser" src="https://github.com/user-attachments/assets/1fb36c25-0e47-4ea0-b624-77ff8ee3b8aa" />

# Dev commits
<img width="1712" height="721" alt="Dev Ss" src="https://github.com/user-attachments/assets/690f5e37-bf0d-4af8-b8a2-3b4a41197262" />

# Merge commits

---



