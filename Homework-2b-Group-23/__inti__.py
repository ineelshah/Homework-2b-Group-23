import configparser

config = configparser.ConfigParser()
try:
	config.read('..\\User_parameters\\user_info.ini')

	name = config['Personal_info']['Name']
	email = config['Personal_info']['email']
	msg = "Hello " + name
except:
	msg = "Please provide your details in the \"User_parameters\\user_info\" file for more personalised messages.\nIf you don't have the parameters file contact developers.\nYou can follow the instructions in the readme.md to fill the parameters file"

def divide(a, b):
	if isnumeric(a) and isnumeric(b):
		return (-1, msg, "please provide valid numeric inputs")
	if b == 0:
		return (-1, msg, "Can not divide by zero")
	return (a/b, msg, "")