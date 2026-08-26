from flask import Flask, jsonify

app = Flask(__name__)

votes = {}


@app.route("/")
def home():
    return "Welcome to the App"


@app.route("/health")
def health():
    return "App is running"


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
