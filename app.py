from __future__ import print_function
from flask import Flask, render_template, request, jsonify
import logging
import sys
from codecs import encode

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def log(what, var):
	app.logger.warning('!!DBG: ' + what + " " + str(var))
	sys.stdout.flush()

@app.route('/')
def default():
	return render_template("index.html")

@app.route('/index')
def index():
	return render_template("index.html")
        
@app.route('/page1')
def page1():
    return render_template('page1.html')
    
@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/calculate_result', methods=['GET', 'POST'])
def calculate_result():
        if (request.method == 'GET'):
                a = int(request.args.get('val1'))
                b = int(request.args.get('val2'))
        elif (request.method == 'POST'):
                a = int(request.form.get('val1'))
                b = int(request.form.get('val2'))
        log("a", a)
        log("b", b)
        return jsonify({"result":a+b})

@app.route('/register', methods=['GET', 'POST'])
def register():
        if (request.method == 'GET'):
                username = request.args.get('username')
                password = request.args.get('pass')
        elif (request.method == 'POST'):
                username = request.form.get('username')
                password = request.form.get('pass')
        if username != "" and password != "":
                with open("server/db.txt", 'a') as file:
                        nameread = file.write("\n")
                        nameread = file.write(username)
                        nameread = file.write("\n")
                        passread = file.write(password[::-1])
                        log("username", username)
                        log("nameread", nameread)
                return jsonify({"result2":"reg ok"})
        else:
                return jsonify({"result2":"reg not ok"})
        
@app.route('/login', methods=['GET', 'POST'])
def login():
        if (request.method == 'GET'):
                username = request.args.get('username')
                password = request.args.get('pass')
        elif (request.method == 'POST'):
                username = request.form.get('username')
                password = request.form.get('pass')
        check = "login not ok"
        with open("server/db.txt", 'r') as file:
                nameread = file.readline()
                passread = file.readline()
                log("username", username)
                log("nameread", nameread)
                log("test", nameread.rstrip() == username)
                log("pass", password)
                log("passread", passread)
                log("test", passread.rstrip()[::-1] == password)
                if username != "" and password != "" and username == nameread.rstrip() and password == passread.rstrip()[::-1]:
                        check = "ok"
                else: 
                        while nameread:
                                nameread = file.readline()
                                passread = file.readline()
                                log("username", username)
                                log("nameread", nameread)
                                log("test", nameread.rstrip() == username)
                                log("pass", password)
                                log("passread", passread)
                                log("test", passread.rstrip() == password)
                                if username != "" and password != "" and username == nameread.rstrip() and password == passread.rstrip()[::-1]:
                                        check = "ok"
        return jsonify({"result2":check})

@app.route('/upload', methods=['GET', 'POST'])
def upload():
        if (request.method == 'GET'):
                filestring = request.args.get('file')
                filename = "files/"+request.args.get('filename')
        elif (request.method == 'POST'):
                filestring = request.form.get('file')
                filename = request.form.get('filename')
        # log("filestring", filestring)
        log("filename", filename)
        f = encode(filestring.encode().decode('unicode_escape'),"raw_unicode_escape")
        # log("rawoutput", f)
        with open("files/"+filename, 'wb') as file:
                file.write(f)
        return jsonify({"result":"File "+filename+" uploaded!"})
	
if __name__ == "__main__":
        app.debug = True
        app.run()