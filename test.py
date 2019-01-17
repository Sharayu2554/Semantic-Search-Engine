import sys
import Task3
from Task3 import Task3

Task3 = Task3()

#sys argument can be either "Read_Corpus" ,  "Task2" , "Task3" , "Task4"
#sys argument has test sentence "Company suffering from losses"

if len(sys.argv) >= 2:
	if sys.argv[1] == "Read_Corpus" : 
		Task3.ReadCorpus()
	elif sys.argv[1] == "Task2" and  sys.argv[2] is not None:
		Task3.analyzeSingleSentenceTask2(sys.argv[2])
	elif sys.argv[1] == "Task3" and  sys.argv[2] is not None:
		Task3.analyzeSingleSentenceTask3(sys.argv[2])
	elif sys.argv[1] == "Task4" and  sys.argv[2] is not None:
		Task3.analyzeSingleSentenceTask4(sys.argv[2])
	else:
		print("Incorrect Parameter, Enter in format python test.py Read_Corpus or python test.py Task2 'Company suffering from losses' ")
else:
	print("Number of Arguments are incorrect, Enter in format python test.py Read_Corpus or python test.py Task2 'Company suffering from losses' ")