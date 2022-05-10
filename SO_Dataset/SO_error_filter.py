import json
import pprint
import os

error_types = set()
path = r"C:\Users\samil\Desktop\StackOverflowSuggestBot\TestDataset"

os.chdir(path)
with open ("preprocessed_test_data.json") as file:
    data = json.load(file)


for key in data:
    error_types.add(data[key]["errorType"])

with open("error_types.txt","w") as f:
    f.write(str(error_types))

#pprint.pprint(error_types)
