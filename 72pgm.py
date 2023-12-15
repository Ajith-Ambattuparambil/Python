import csv

f=open('prgrm72.csv','w+')
fields=['Name','Age','Gender']
insert=csv.DictWriter(f,fieldnames=fields)
insert.writeheader()
rows=[{'Name':'Ajith','Age':'21','Gender':'Male'},{'Name':'Ajai','Age':'32','Gender':'Male'}] 
insert.writerows(rows)
f.close()
f1=open('prgrm72.csv','r')
readit=csv.DictReader(f1)
for lines in readit:
    if readit:
        print(lines['Name'],'\t',lines['Age'],'\t',lines['Gender'])
f1.close()
