#13. Write a function to write a comma-separated value (CSV) file. It
#should accept a filename and a list of tuples as parameters. The
#tuples should have a name, address, and age. The file should create
#a header row followed by a row for each tuple. If the following list of
#tuples was passed in:
#[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
#it should write the following in the file:
#name,address,age
#George,4312 Abbey Road,22
#John,54 Love Ave,21

import csv

def csv_write(filename, info_tuple):
    with open(filename+'.csv', mode = "w") as csv_data:
        header = ['Name', 'Address', 'Age']
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(header)
        for row in info_tuple:
            csv_writer.writerow(row)
        csv_data.close()

csv_write('CSVfile', [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)])