from flask import Flask
import os

api = Flask(__name__)

@api.route("/")
def index():
    return "Hello World\n"

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)