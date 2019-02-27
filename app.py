from flask import Flask, render_template, request,  
from random import randint
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html", name="Senay", lucky_num=randint(1,1000))
    #return "<html><body><h1>Hi!</h1></body></html>"

@app.route("/another")
def some_other_name():
    return "<html><body><h1>Yo!</h1></body></html>"    


@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/story")
def show_story():
    noun=request.args.get("noun")
    adj=request.args.get("adjective")
    verb=request.args.get("verb")
    noun2=request.args.get("noun-2")
    return render_template("story.html", 
    noun=noun,
    adjective=adj,
    verb=verb,
    noun2=noun2
    )
@app.route("story-as-json")
def story_as_json():
    noun=request.args.get("noun")
