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
	if request.method == 'POST':
		form_input = request.form['name']
		config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}

		connection = mysql.connector.connect(**config)
		cursor = connection.cursor()	
		command = "SELECT * FROM champions where name = '" + form_input + "'"
		print(command)
		cursor.execute(command);
		#cursor.callproc('h');
		# results = [(name, classs, description) for (name, classs, description) in cursor.stored_results()] 
		results = [(name, classs, description) for (name, classs, description) in cursor]
		#cursor.execute('select h()');
		#results = [(a) for (a) in cursor]
		print(results)
		#print(cursor.stored_results())

		if results == []:
			return  render_template('back.html') + "<br><br>" + render_template('index.html') + "This champions does not exists"
		else:
			name = results[0][0]
			classs = results[0][1]
			description = results[0][2]
			img = form_input + ".jpg"

			output = "Name: " + name + "<br><br>" + "Class: " + classs + "<br><br>" + \
				"Description: " + description + "<br><br>" + \
				"<img src=static/" + img + ">"
 
			return render_template('back.html') + "<br><br>" + render_template('index.html', name=form_input) + output
	else:
		return  render_template('back.html') + "<br><br>" + render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
