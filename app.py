from flask import Flask
from flask import render_template, request 

app = Flask(__name__) # assigning this app to me

@app.route("/") # @ -> to run the 1st line
def index():
    return(render_template("index.html"))

if __name__ == "__main__": # to double confirm that the application belongs to me
    app.run()
    
