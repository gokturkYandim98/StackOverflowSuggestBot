import pickle
from platform import python_branch
from colorPrint import printGreen,printYellow

# ----------------------------------------------------------------------------------------
# Read statQC pickle (data dictionaries) files

file = open("statQC Data\single_code_answer_qid_to_code.pickle", 'rb')      # Contains [question id, single code] dictionary
s_id_to_code = pickle.load(file)                                            
file.close()

file = open("statQC Data\single_code_answer_qid_to_title.pickle", 'rb')     # Contains [question id, question title] dictionary
s_id_to_title = pickle.load(file)
file.close()

# ----------------------------------------------------------------------------------------
# Example usage
# Print question and single line code snippet

printYellow(s_id_to_title[15334846])
printGreen(s_id_to_code[15334846])