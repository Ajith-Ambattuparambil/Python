import csv
fields=['Name','Department','DOJ']
rows=[{'Name':'Ajith','Department':'MCA','DOJ':'August'},{'Name':'Ashish','Department':'MCA','DOJ':'September'}]
with open('employee.csv','w') as f:
    writer=csv.DictWriter(f,fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    f.close()