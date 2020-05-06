from flask import Flask
from flask import render_template
from flask import request
import mysql.connector

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def init():
	return render_template('page.html')


@app.route('/classes_dump',methods=['POST','GET'])
def process_classes_1():
	config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('select * from classes')
	results = [(a, b, c) for (a, b, c) in cursor]
	str_results = ''
	for elem in results:
		for c in elem:
			str_results += str(c)
			str_results += ' ----  '
		str_results += '\n'


	return str_results


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
		cursor.execute(command);
		#cursor.callproc('h');
		# results = [(name, classs, description) for (name, classs, description) in cursor.stored_results()] 
		results = [(name, classs, description) for (name, classs, description) in cursor]
		#cursor.execute('select h()');
		#results = [(a) for (a) in cursor]
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

@app.route('/champs_raport',methods=['POST','GET'])
def process_raport_1():
	config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.execute('select * from champions_stats')
	results = [(n, a, b, c, d) for (n, a, b, c,d) in cursor]

	print(results[1])
	output = ''
	for elem in results:
		output += "Champion " + str(elem[0]) + "<br>"
		output += "<pre class=\"tab\">" + "Health: " + str(elem[1]) + "<br>"
		output += "    Armour: " + str(elem[2]) + "<br>"
		output += "    Magic Resist: " + str(elem[3]) + "<br>"
		output += "    Adaptive Damage: " + str(elem[4]) + "<br><br>"
		output += "                 Force power based on the above stats: " + \
				str((elem[1] + elem[2] + elem[3] + elem[4]) / 4) + "</pre>"
		output += "--------------------------------------------------------------------------------------------------------------<br><br>"


	cursor.execute('select get_nr_champs()')
	result = [(a) for (a) in cursor]
	print(result[0][0])

	return render_template('back.html') + "<br><br>" + output + \
		"TOTAL NUMBER OF CHAMPIONS: " + str(result[0][0])

@app.route('/classes',methods=['POST','GET'])
def process_classes():
	config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('select * from classes')
	results = [(a, b, c) for (a, b, c) in cursor]
	str_results = ''
	for elem in results:
		for c in elem:
			str_results += str(c)
			str_results += ' ----  '
		str_results += '<br> <br>'

	print(results)

	return str_results + render_template('back.html') + "<br><br>"

@app.route('/items_raport',methods=['POST','GET'])
def process_raport_2():
	config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.callproc('get_all_items');
	results = [(name, a, b,c) for (name, a, b,c) in cursor.stored_results()]

	str_results = ''
	for elem in results[0]:
		for c in elem:
			str_results += str(c)
			str_results += ' '
		str_results += '<br> <br>'

	cursor.execute('select get_nr_items()')
	result = [(a) for (a) in cursor]

	str_results += "------------------- <br> <br> Total:   " + str(result[0][0])

	return str_results + "<br><br>" + render_template('back.html') + "<br><br>"

@app.route('/items_raport_dump',methods=['POST','GET'])
def process_raport_3():
	config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	cursor.callproc('get_all_items');
	results = [(name, a, b,c) for (name, a, b,c) in cursor.stored_results()]

	str_results = ''
	for elem in results[0]:
		for c in elem:
			str_results += str(c)
			str_results += ' '
		str_results += '\n'

	cursor.execute('select get_nr_items()')
	result = [(a) for (a) in cursor]

	str_results += "\n-------------------  Total:   " + str(result[0][0])

	return str_results


@app.route('/champions_dump',methods=['POST','GET'])
def process_form5():
	config = {
			'user': 'root',
			'password': 'root',
			'host': 'database',
			'port': '3306',
			'database': 'lol'
		}

	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()	

	champion_name = request.args['champion']
	command = "SELECT * FROM champions where name = '" + champion_name + "'"
	cursor.execute(command);
	results = [(name, classs, description) for (name, classs, description) in cursor]

	if results == []:
		return "This champions does not exists"
	else:
		name = results[0][0]
		classs = results[0][1]
		description = results[0][2]

		output = "Name: " + name + "\n" + "Class: " + classs + "\n" + \
			"Description: " + description + "\n\n"

		return output


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
