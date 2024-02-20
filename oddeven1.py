n=int(input("Enter number:"))
b=0
m=n
n=(n//10)*10
m=m-n
while m>0:
    m=m-2
    b=b+1
print("even") if m==0 else print("odd")