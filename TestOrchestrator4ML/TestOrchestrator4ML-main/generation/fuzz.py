import main
import py_parser
import label_perturbation_main

if __name__ == '__main__':

	#Fuzzing generateUnitTest. Expects a valid algorithm and attack type. We give it a valid attack type, but we give it 'invalidAlgo'
	try:
		main.generateUnitTest('invalidAlgo', 'random') #passing an invalid filename for the algorithm
	except Exception as exc:
		print(exc)

	#Fuzzing checkAlgoNames. Expects a function list, instead we give it 43
	try:
		py_parser.checkAlgoNames(43) #Inputs something that should not work, but does not return an error
	except Exception as exc:
		print(exc)

	# Fuzzing checkForLibraryImport. Expects a valid model name, instead we give it notWhatItNeeds (which is a list of different data types)
	try:
		notWhatItNeeds = [12, "willit work", 'n']
		py_parser.checkForLibraryImport(notWhatItNeeds)
	except Exception as exc:
		print(exc)

	# Fuzzing run_experiment. Expects a valid model name, instead we give it notWhatItNeeds (which is a list of different data types)
	try:
		notWhatItNeeds = [12, "willit work", 'n']
		label_perturbation_main.run_experiment(notWhatItNeeds)
	except Exception as exc:
		print(exc)

	# Fuzzing run_label_perturbation. Expects a valid model name, instead we give it 'george'
	try:
		label_perturbation_main.run_label_perturbation('george')
	except Exception as exc:
		print(exc)

	py_parser.getPythonParseObject(py_parser)
