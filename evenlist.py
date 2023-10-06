a=input("Enter your numbers: ")
a=list(map(int,a.split(',')))
even=[i for i in a if(i%2==0)]
print(even)
