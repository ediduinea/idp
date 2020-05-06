from typing import List, Dict
import mysql.connector
import json
import sys

def insert_champion(connection,cursor, name, classs, description):
	query = "INSERT INTO champions (name, class, description) \
					VALUES(%s, %s, %s)"
	args = (name, classs, description)
	
	cursor.execute(query, args);

	connection.commit()

	cursor.execute("SELECT * FROM champions");
	results = [(name, classs, description) for (name, classs, description) in cursor]

	print(results)

	#return results
	

if __name__ == '__main__':
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'database',
		'port': '3306',
		'database': 'lol'
	}
	
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()

	while True:
		print('\n')
		print('USAGE: command [arguments]. [] are not used, only describe arguments')
		print("                    ---------- AVAILABLE COMMANDS ---------")
		print("     insert_champion [name class description]")
		print("     exit")
		print()

		command = input('---> ')
		command = command.split(' ')

		if command[0] == 'insert_champion':
			if len(command) == 1:
				print("You must provide champion name, class, and description")
				continue
			elif len(command) == 2:
				print("You must provide champion class, and description")
			elif len(command) == 3:
				print("You must provide champion a description")
			else:
				insert_champion(connection, cursor, *command[1:])

		elif command[0] == 'exit':
			connection.commit()
			cursor.close()
			connection.close()

			sys.exit()	
		else:
			print('Unrecognized command, please try again')

	connection.commit()
	cursor.close()
	connection.close()
			
