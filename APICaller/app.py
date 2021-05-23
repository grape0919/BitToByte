# --*-- coding: UTF-8
from flask import Flask, g, render_template, request, redirect, session, flash, send_file, url_for

from APICaller.log.Logger import Logger
import os

from flask_session import Session

from APICaller.conf.config import Config

app = Flask(__name__)
sess = Session()
app.secret_key = 'aGtkZXZzdHVkaW8='
config = Config()
config.load()
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DATABASE = os.path.join(PROJECT_ROOT,'rdbms','example.db')

@app.route("/")
def root():
    # if not session.get("login"):
    #     return redirect("/login")
    return render_template("stockSample.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

    pass
