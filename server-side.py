from flask import Flask, render_template, request, send_file, Response, make_response, jsonify, redirect, flash
import os
import time

path = os.getcwd()
app = Flask(__name__)

cek = """<center><img src="vvvfotovvv"></img>
        <form action="/cur">
        <input type="submit" value="Click Me"></input>
        </form>
        </center>"""


@app.route("/", methods=['POST', 'GET'])
def cam():
    if request.method == 'POST':
        file = request.files["file"]
        os.system("rm " + path + "/static/*.jpg")
        file.save(path + "/static/" + str(time.time()) + ".jpg")
    else:
        for fil in os.listdir(path + "/static/"):
            if ".jpg" in str(fil):
                return cek.replace("vvvfotovvv", "/static/" + str(fil))
        return ("what a lovely day")
                
@app.route("/cur")
def currentTime():
    t = open(path + "/static/t.txt", "w")
    t.write(str(time.time()))
    t.close()
    return redirect("/")
