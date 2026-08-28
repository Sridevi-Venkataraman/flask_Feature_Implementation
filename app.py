from flask import Flask, request, jsonify

app = Flask(__name__)

password_store = {}

@app.route('/add', methods=['GET'])
def add_user():
    username = request.args.get("username")
    password = request.args.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    password_store[username] = password
    return jsonify({"message": f"Stored {username} with password {password}"})


@app.route('/get/<username>', methods=['GET'])
def get_password(username):
    if username in password_store:
        return jsonify({"username": username, "password": password_store[username]})
    else:
        return jsonify({"error": "Username not found"}), 404

@app.route('/delete', methods=['GET'])
def delete_user_query():
    username = request.args.get("username")
    if not username:
        return jsonify({"error": "Username required"}), 400

    if username in password_store:
        del password_store[username]
        return jsonify({"message": f"User {username} deleted successfully"})
    else:
        return jsonify({"error": "Username not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
