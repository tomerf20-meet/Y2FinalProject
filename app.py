from flask import Flask, request, redirect, url_for, render_template
from database import *
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")


@app.route('/contact')
def contact():
	return render_template("contact_us.html")


@app.route('/search',methods=["GET", "POST"])
def search():
	if request.method=="GET":
		return render_template("search.html")
	else:
		s = request.form["search"]
		return redirect(url_for('results',keyword=s))

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/api')
def api():
    return render_template('api.html')

@app.route('/results/<keyword>',methods=["GET","POST"])
def results(keyword):
	food_list=[]
	restaurant_list=Get_All_Restaurants()
	for i in restaurant_list:
		if keyword in i.Foods:
			food_list.append(i)
	return render_template("results.html", food=food_list)



if __name__ == '__main__':
	app.run(debug=True)