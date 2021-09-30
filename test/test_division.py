from code import division


def division_util(a,b):
	return division.divide(a,b)

def test_division_by_zero():
    if division_util('10','5')[1] == 1:
    	assert division_util('10','5')[0] == 2.0
    else:
    	assert division_util('10','5')[0] == -1

def test_general_division():
	assert division_util('100000000000001', '2')[0] == 50000000000000.5

def test_general_division_small():
	assert division_util('25', '2')[0] == 12.5