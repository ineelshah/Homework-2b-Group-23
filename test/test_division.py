from src import division

# Test division by zero:


def division_util(a,b):
	return division.divide(a,b)

def test_capitalize_string():
    if division_util('10','5')[1] == 1:
    	assert division_util('10','5')[0] == 2.0
    else:
    	assert division_util('10','5')[0] == -1

def test_general_division():
	assert division_util('100000000000001', '2')[0] == 50000000000000.5

