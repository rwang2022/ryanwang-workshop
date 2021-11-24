# Sophie Liu, Ryan Wang
# SoftDev
# K19: A RESTful Journey Skyward
# 2021-11-23

from flask import Flask, render_template
from json import loads
import urllib

app = Flask(__name__)

key = ""
with open("key_nasa.txt") as file:
    key = file.read()

json = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=%s" % key).read()
dict = loads(json)

@app.route("/")
def main():
    return render_template("main.html", pic=dict['url'], ex=dict['explanation'])

app.run()
