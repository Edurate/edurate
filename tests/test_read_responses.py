import read_responses
"""tests the functionality of read_responses.py"""

#def test_read_responses():
	
	
def test_no_filepath():
	"""tests what happens when no meaningful filepath is specified"""
	result = read_responses.read_responses("", False)
	assert result == "File Not Found"