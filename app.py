from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")
    #return "<html><body><h1>Hi!</h1></body></html>"

@app.route("/another")
def some_other_name():
    return "<html><body><h1>Yo!</h1></body></html>"    