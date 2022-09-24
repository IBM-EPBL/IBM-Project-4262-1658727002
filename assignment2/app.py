from flask import Flask
from flask import render_template

app = Flask(__name__)


users = { }

@app.route("/")
@app.route("/base")
def base():
    return render_template("base.html")
    
@app.route("/home")
def home():
  return render_template("home.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signin", methods = ['POST', 'GET'])
def signin():
  if request.method == 'POST':   
    email = request.form["email"]
    password = request.form["password"]        



    if email in users:
      user = users[email]
      if user["password"] == password:
        return render_template("thankyou.html", fname=user["fname"], lname=user["lname"], email=user["email"])

    return render_template("wrong_cred.html", email=email)
    
  else:
    return render_template("signin.html")

@app.route("/signup", methods = ['POST', 'GET'])
def signup():
  if request.method == 'POST':    
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]        

    users[email] = {
      "fname": fname,
      "lname": lname,
      "email": email,
      "password": password,
    }
    print(users)
    return render_template("thankyou.html", fname=fname, lname=lname, email=email)
  else:
    return render_template("signup.html")

@app.route("/thankyou")
def thankyou():
  return render_template("thankyou.html", e="test")