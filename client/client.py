import requests

if __name__ == '__main__':

	print('Welcome to Wiki League of Legends! What can we help you with?')

	while True:
		print('')
		print("                    ---------- OPTIONS ---------")
		print("     search_champion [champion_name]")
		print("     display_classes")
		print("     display_items")
		print("     exit")
		print()

		option = input('---> ')	
		option = option.split(' ')
		
		if option[0] == 'search_champion':
			payload = {'champion': option[1]}
			response = requests.post('http://server:5000/champions_dump', params=payload)
	
			print(response.text)
			
		elif option[0] == 'display_classes':
			response = requests.get('http://server:5000/classes_dump')
	
			print(response.text)
			
		elif option[0] == 'display_items':
			response = requests.get('http://server:5000/items_raport_dump')

			print(response.text) 		

		elif option[0] == "exit":
			print("Bye bye!")
			break
		else:
			print('Invalid option')
