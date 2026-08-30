from flask import Flask, jsonify

app = Flask(__name__)

votes = {}

# Version 1.0.0 changes are present in this code snippet. The following changes have been made:
@app.route("/")
def home():
    return "Welcome to the App"


@app.route("/health")
def health():
    return "App is running"

# Version 2.0.0 changes are present in this code snippet. The following changes have been made:
# Implemented a voting system with endpoints to vote for candidates, view results, and reset votes.
@app.route("/vote/<name>")
def vote(name):
    votes[name] = votes.get(name, 0) + 1
    return jsonify({
        "message": "Vote recorded",
        "candidate": name,
        "votes": votes[name]
    })


@app.route("/results")
def results():
    return jsonify(votes)


@app.route("/reset")
def reset():
    votes.clear()
    return jsonify({
        "message": "All vote counts have been reset"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
