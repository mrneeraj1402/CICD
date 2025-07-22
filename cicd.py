from flask import Flask

myapp=Flask(__name__)

@myapp.route("/info")
def lwinfo():
    return "thisis lw "

@myapp.route("/mail")
def lwmail():
    return "thiasdfasd "

@myapp.route("/Aboutme")
def tellaboutme():
    n = "Neeraj"
    return f"i m {n}"

myapp.run()