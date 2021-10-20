# Team threeCoffeePeanuts: Jesse Xie, Yaying Liang Li, Ryan Wang
#SoftDev
#K15 -- Sessions Greetings
#2021-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

# do a better secret_key later
app.secret_key = "dogs say woof"

#hard coding single username and password
real_user = "coffee"
real_passwd = "peanut"

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    # check whether or not it is already is session
    print("\n\n\n####### SESSION HERE #######")
    print(session)
    print(session.get(real_user))
    print("####### SESSION HERE #######\n\n\n")

    if not session.get(real_user):
        return render_template('login.html')
    else:
        return render_template("response.html", username=real_user)


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    
    # using conditional in order to make GET/POST fail-safe
    if request.method == "GET":
        username = request.args['username']
        password = request.args['password']
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    # if username and password are a correct pair, we send them to response.html (logs you in)
    if (username == real_user and password == real_passwd):
        session[username] = password
        return render_template('response.html', method=request.method, username=username)
    
    # login failed because of wrong pass, tells you error at the bottom (at login.html)
    elif (username == real_user and password != real_passwd):
        error = "user exists but wrong password"
        return render_template( 'login.html', error=error)

    # login fails because username isn't correct / doesn't exist
    else:
        error = "Error: that username does not exist"
        return render_template( 'login.html', error=error)
    

@app.route("/logout") # , methods=['GET', 'POST'])
def logout():
    if real_user in session:
        session.pop(real_user)
    return render_template('login.html')

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
