def divide(a, b):
	if a.isnumeric() and b.isnumeric():
		if float(b) != 0.0:
			return int(a)/int(b), 1, ""
		else:
			return -1, 0, "Can not divide by zero"
	else:
		return -1, 0, "Please provide valid input"