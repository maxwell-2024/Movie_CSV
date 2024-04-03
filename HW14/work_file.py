import json
import pprint
import os
os.chdir("HW14")



file_path = "data.json"
file_obj = open(file_path)
str_to_dict = json.load(file_obj)
print(type(str_to_dict),str_to_dict)

file_path = "data.json"
file_obj = open(file_path)
file_data = file_obj.read()
str_to_dict = json.loads(file_data)
print(type(str_to_dict),str_to_dict)
