from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to Azure App Service!</h1>
    <p>This change is to test CI/CD deployment.</p>
    <a href='/about'>Go to About Page</a>
    """

@app.route("/about")
def about():
    return """
    <h2>About Page</h2>
    <p>This page is added to verify automatic deployment from GitHub.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

