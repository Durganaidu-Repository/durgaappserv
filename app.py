from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Azure CI/CD Test - Version 4</h1>
    <p>This deployment should now work correctly.</p>
    <a href="/about">About Page</a> |
    <a href="/api/data">API Test</a>
    """

@app.route("/about")
def about():
    return "<h2>CI/CD Test Successful!</h2><p>If you see this, deployment happened automatically.</p>"

@app.route("/api/data")
def api_data():
    return jsonify({
        "status": "success",
        "version": 4,
        "message": "API is working correctly!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


