# python writing files (.txt, .json, .csv)

# w = write a file
# x = check for exixsing file than write a file if it don't exist
# a = append to a file if it exists
# r = read a file
# txt_data = "I like to travel the world"
# employees = ["John Doe", "Sally", "Candy", "Peter" ]
import json
import csv

# employees = {
#     "name": "John",
#     "age" : 30,
#     "position": "Software Engineer",
#     "salary": 80000
# }

employees = [["name", "age", "job"],
            ["John", 30, "cook"], 
            ["Sally", 23, "Designer"], 
            ["Candy", 35, "driver"],
            ["Mack", 32, "engineer"]]

file_path = "C:/Users/ogunt/Desktop/output.csv"


try:
    with open(file_path, "w", newline="") as file:
        # - list file
        # for employee in employees:
        #     file.write(employee + "\n") 

        # - txt file
        # file.write("\n" + txt_data) 

        # - json file
        # json.dump(employees, file, indent = 4) 

        # csv file
        writer = csv.writer(file)
        
        for row in employees:
            writer.writerows([row])

        print(f"csv file '{file_path}' created successfully.")

except FileExistsError:
    print(f"That file already exists.")