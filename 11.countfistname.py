s=input("Enter names in a comma separated list: ")
name=list(s.split(','))
print(name)
name=[item.split('.') for item in name]
count=0
print("Names are")
for item in name:
    print(item[0])
    if(item[0][0]=='a' or item[0][0]=='A'):
        count=count+1
print("No. of names start with A is", count)
