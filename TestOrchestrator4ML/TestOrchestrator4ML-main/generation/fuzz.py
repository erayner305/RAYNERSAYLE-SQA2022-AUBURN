import detection.main
if __name__ == '__main__':
	# Input invalid parms to generateUnitTest
	detection.main.get_test_details('not a test at all') #passing something that is not a test
	generateUnitTest('invalidAlgo', 'random') #passing an invalid filename for the algorithm
	generateAttack(12, delta) #passing the incorrect data type
	runs([1]) #passing an invalid list to the method