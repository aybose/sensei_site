import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)