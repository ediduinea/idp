from flask import Flask
from flask import render_template
from flask import request
import mysql.connector

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def init():
	return render_template('page.html')


@app.route('/champions',methods=['POST','GET'])
def process_form():
			
	form_input = request.form['name']

	return render_template('back.html') + "<br><br>" + render_template('index.html', name=form_input)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
