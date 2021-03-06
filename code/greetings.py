import configparser

def greet():
	config = configparser.ConfigParser()
	try:
		config.read('..\\User_parameters\\user_info.ini')

		name = config['Personal_info']['Name']
		email = config['Personal_info']['email']
		msg = "Hello " + name
	except:
		msg = "Please provide your details in the \"User_parameters\\user_info\" file for more personalised messages.\nIf you don't have the parameters file contact developers.\nYou can follow the instructions in the readme.md to fill the parameters file"
	return msg