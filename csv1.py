import csv
fields=['Name','Rollno','dept']
rows=[['Ajith','9','MCA'],['Amal','10','MCA']]
with open('student.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(rows)
    f.close()