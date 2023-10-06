import math
s=input('Enter a list of numbers: ')
s=list(map(int,s.split(',')))
sort=[]
for i in s:
    if min(s)==i:
        sort.append(i)
        s.remove(i)
print("The second smallest element is: ",sort[1])

        
    

