from flask import Flask, render_template, request, session, url_for, redirect
from utils import check
app=Flask(__name__)

@app.route("/")
def login():
    return render_template("form.html")

@app.route("/authenticate/", methods =['POST'])
def auth():
    if check.check(request.form):
        acc="ACCEPTED"
    else:
        acc="DENIED"
    return render_template("accept.html",status=acc)

@app.route("/register/", methods = ['POST'])
def reg():
    check.register(request.form)
    return redirect(url_for("login"))

if __name__=='__main__':
    app.debug=True
    app.run()
        
