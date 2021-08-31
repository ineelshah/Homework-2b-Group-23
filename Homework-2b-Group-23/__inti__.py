import configparser

config = configparser.ConfigParser()
config.read('..\\User_parameters\\user_info.ini')

name = config['Personal_info']['Name']
email = config['Personal_info']['email']

print("hello " + name)