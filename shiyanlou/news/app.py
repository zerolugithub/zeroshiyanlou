#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 10:48
# @Author  : zero
# @File    : app.py.py
# @Software: PyCharm

from flask import Flask,render_template,abort
import json
import os


app = Flask(__name__,template_folder="../templates")




def handleJson(fileName,key):
    jf = json.load(open(fileName,"r"))
    return jf[key]



@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404

@app.route("/")
def index():
    os.chdir("../files")
    titles = []
    for root,dir,files in os.walk(os.getcwd()):
        for f in files:
            titles.append(handleJson(f,"title"))

    return render_template("index.html",titles=titles)


@app.route("/files/<filename>")
def files(filename):
    os.chdir("../files")
    jf = os.getcwd()+"/"+ filename+".json"
    if not os.path.exists(jf):
        abort(404)
    fileContent = handleJson(jf,"content")
    import re
    fileContents =  re.split(r" \\n | \\\\n",fileContent)

    return render_template("file.html",fileContents = fileContents)

if __name__ == "__main__":
    app.run(debug=True,port=3000)
