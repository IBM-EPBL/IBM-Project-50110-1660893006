from flask import Flask, redirect, url_for, render_template
import ibm_db

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=;PORT=;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA;UID;PWD",'','')
app = Flask(__name__)

@app.route("/")
def name():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/aboutpage")
def aboutpage():
    return render_template("aboutpage.html")


if __name__ == "__main__":
    app.run()
