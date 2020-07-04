#14. Write a function that reads a CSV file. It should return a list of
#dictionaries, using the first row as key names, and each subsequent
#row as values for those keys.
#For the data in the previous example it would return:
#[{'name': 'George', 'address': '4312 Abbey Road', 'age': 22}, {'name':
#'John', 'address': '54 Love Ave', 'age': 21}]

import csv

def csv_read(csv_file):
    with open(csv_file, newline='') as csv_data:
        csv_reader = csv.DictReader(csv_data )
        result_dict ={}
        result_list = []
        for row in csv_reader:
            result_dict['Name'] = row['Name']
            result_dict['Address'] = row['Address']
            result_dict['Age'] = row['Age']
            result_list.append(result_dict)
    print(result_list)
csv_read('CSVfile.csv')
