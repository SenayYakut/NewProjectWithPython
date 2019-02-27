from flask import Flask 

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<html><body><h1>Hi!</h1></body></html>"