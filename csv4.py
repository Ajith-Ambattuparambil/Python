import csv
with open('employee.csv',mode='r') as f:
    file=csv.DictReader(f)
    for lines in file:
        if lines:
            print(lines['Name'],'\t',lines['Department'],'\t',lines['DOJ'])