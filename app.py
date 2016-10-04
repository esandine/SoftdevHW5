from flask import Flask, render_template, request
from utils import check
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("form.html")

@app.route("/authenticate/", methods =['POST'])
def auth():
    if check.check(request.form):
        return render_template("accept.html",status="ACCEPTED")
    else:
        return render_template("accept.html",status="DENIED")

@app.route("/register/", methods = ['POST'])
def reg():
    check.register(request.form)
    return render_template("form.html")

if __name__=='__main__':
    app.debug=True
    app.run()
        
