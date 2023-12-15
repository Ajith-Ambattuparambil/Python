import csv

f=open('abc.csv','r')
file=csv.reader(f)
for lines in file:
    if lines:
        print(lines[0],'\t',lines[1],'\t',lines[2])
