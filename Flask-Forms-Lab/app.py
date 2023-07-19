from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/',methods=['GET','POST'])
def login():
	if request.method=='POST':
		usern = request.form['username']
		passzain = request.form['password']
		if(usern==username and passzain==password):
			return redirect(url_for('home'))
		else:
			return render_template('login.html')	

	else:
		return render_template('login.html')
	
@app.route('/friend_exists/<string:name>')
def fri(name):
	if name in facebook_friends:
		return render_template(
				'friend_exists.html', n = name,h=True)
	else:
		return render_template(	
			'friend_exists.html', n = name,h=False)
		


@app.route('/home',methods=['GET','POST'])
def home():
	return render_template('home.html',face=facebook_friends)

if __name__ == "__main__":# Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)
