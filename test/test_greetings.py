from src import greetings

def greetings_util():
	return greetings.greet()

def test_greetings_string():
	assert greetings_util() == "Please provide your details in the \"User_parameters\\user_info\" file for more personalised messages.\nIf you don't have the parameters file contact developers.\nYou can follow the instructions in the readme.md to fill the parameters file"

