a=input("Enter the numbers: ")
a=list(map(int, a.split(',')))
l=[]
for item in a:
    if(item not in l):
        l.append(item)
print(l)
