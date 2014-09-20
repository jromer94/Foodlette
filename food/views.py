from food import app
from flask import render_template, request

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")
    #this is home page

@app.route('/order', methods=['GET','POST'])
def ordr():
	return render_template("pricerange.html")
	# first order page that asks about price and stuff
	
@app.route('/info', methods=['GET','POST'])
def info():
	return render_template("userinfo.html")
	
@app.route('/credit', methods=['GET','POST'])
def credit():
	return render_template("credit.html")