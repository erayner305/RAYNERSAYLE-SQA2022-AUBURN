from detection.main import get_test_details
from generation.main import generateUnitTest
from generation.main import generateAttack
from label_perturbation_attack.cliffsDelta import runs

if __name__ == '__main__':
	# Input invalid parms to generateUnitTest
	get_test_details('not a test at all') #passing something that is not a test
	generateUnitTest('invalidAlgo', 'random') #passing an invalid filename for the algorithm
	generateAttack(12, delta) #passing the incorrect data type
	runs([1]) #passing an invalid list to the method