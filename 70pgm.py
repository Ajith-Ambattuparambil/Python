import csv

f=open('abc.csv','w+')
insert=csv.writer(f)
fields=input('Enter the fields seperated with comma: ').split(',')
insert.writerow(fields)
n=int(input('Enter the number of rows to insert: '))
for i in range(0,n):
    print('row',i+1,' : ')
    rows=input('Enter values seperated with comma: ').split(',')
    insert.writerow(rows)

f.close()
