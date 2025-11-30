from flask import Flask, jsonify, request
import random
import datetime

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Azure CI/CD Test - Version 5</h1>
    <p>Deployment Time: {now}</p>
    <p>This version includes dynamic time, random data, query params, and error handling.</p>
    <ul>
        <li><a href="/about">About Page</a></li>
        <li><a href="/random">Random Number</a></li>
        <li><a href="/api/user?name=Durga">API with Query Params</a></li>
        <li><a href="/api/error">Trigger Error</a></li>
    </ul>
    """

# About Page
@app.route("/about")
def about():
    return "<h2>CI/CD Version 5</h2><p>This is the advanced version with multiple tests.</p>"

# Random number API
@app.route("/random")
def random_number():
    number = random.randint(1, 100)
    return f"<h3>Your random number is: {number}</h3>"

# API endpoint with query parameters
@app.route("/api/user")
def api_user():
    name = request.args.get("name", "Guest")
    return jsonify({
        "message": f"Hello, {name}!",
        "info": "This API supports query parameters.",
        "version": 5
    })

# API endpoint that returns error intentionally
@app.route("/api/error")
def api_error():
    return jsonify({
        "status": "error",
        "message": "This is a test error response.",
        "version": 5
    }), 500

# Main entry
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


