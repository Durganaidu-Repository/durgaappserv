from flask import Flask, render_template, jsonify, request
import random
import datetime

app = Flask(__name__)

# Homepage
@app.route("/")
def home():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("home.html", time=now, title="Home")

# About Page
@app.route("/about")
def about():
    return render_template("about.html", title="About")

# Random number page
@app.route("/random")
def random_number():
    number = random.randint(1, 100)
    return f"<h3>Your random number is: {number}</h3>"

# Query parameter API
@app.route("/api/user")
def api_user():
    name = request.args.get("name", "Guest")
    return jsonify({
        "message": f"Hello, {name}!",
        "info": "This API supports query parameters.",
        "version": "UI"
    })

# JSON API
@app.route("/api/data")
def api_data():
    return jsonify({
        "status": "success",
        "version": "UI",
        "message": "Styled Flask App Working"
    })

# Error API
@app.route("/api/error")
def api_error():
    return jsonify({
        "status": "error",
        "message": "This is a test error response."
    }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
