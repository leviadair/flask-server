from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def home():
	return 'Home'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'


# string as path param
@app.route('/user/<string:user_name>')
def getUserName(user_name):
	return "User name is: " + user_name


#int as path param
@app.route('/user/<int:user_id>')
def getUserId(user_id):
	return "User id is: %d" % user_id


@app.route('/user/<path:secondary_path>')
def getSubPath(secondary_path):
	return "Sub Path is " + secondary_path

@app.route("/html")
@app.route('/html/<name>')
def getStaticHtmlFile(name=None):
	return render_template('hello.html', name=name)
	