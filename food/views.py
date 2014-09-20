from food import app
from flask import render_template, request

@app.route('/', methods=['GET','POST'])
def index():
    return "hello, world!"
