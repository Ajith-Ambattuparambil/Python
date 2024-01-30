import csv
with open('student.csv',mode='r') as f:
    file=csv.reader(f)
    for lines in file:
        if lines:
            print(lines[0],lines[1],lines[2])