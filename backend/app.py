from flask import Flask


app = Flask(__name__)
CORS(app, origins=['http://localhost:5173'], supports_credentials=True)

@app.route("/", methods=["GET"])
def hello():
    return "hello"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)