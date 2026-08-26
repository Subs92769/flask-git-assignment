from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory username/password store
users = {}


@app.route("/")
def home():
    return "Username Password Store"


@app.route("/add", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({
            "error": "username and password are required"
        }), 400

    username = data["username"]
    password = data["password"]

    users[username] = password

    return jsonify({
        "message": "User added successfully",
        "username": username
    }), 201


@app.route("/get/<username>", methods=["GET"])
def get_password(username):
    if username not in users:
        return jsonify({
            "error": "Username not found"
        }), 404

    return jsonify({
        "username": username,
        "password": users[username]
    }), 200


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/delete/<username>", methods=["DELETE"])
def delete_user(username):
    if username not in users:
        return jsonify({
            "error": "Username not found"
        }), 404

    del users[username]

    return jsonify({
        "message": "User deleted successfully",
        "username": username
    }), 200