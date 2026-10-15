
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>CI/CD Pipeline Using Jenkins</h1>
    <p>Flask application deployed using Docker.</p>
    <p>Experiment 5 - Cloud Computing and DevOps</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
