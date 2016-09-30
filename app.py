from flask import Flask, render_template
from utils import check
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("form.html")

@app.route("/authenticate")
def auth:
    return check(request.form)
if __name__=='__main__':
    app.debug=True
    app.run()
        
