# python reading files (.txt, .json, .csv)
import json
import csv

file_path  = "C:/Users/ogunt/Desktop/output.csv"


try:
    with open(file_path, 'r') as file:
        # content = file.read()
        # content = json.load(file)  
        content = csv.reader(file)
        for line in content:
            print(line)

        # print(content)

except FileNotFoundError:
    print("The file was not found.")

except PermissionError:
    print("You do not have permission to access this file.")
