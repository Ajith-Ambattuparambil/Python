def count(n):
    c=0
    while n:
        n=n//10
        c+=1
    return c
def zfill(c):
    a=1
    while c:
        a=a*10
        c=c-1
    return a
def temp(n,m):
    return n*zfill(count(m))+m
n=int(input("Enter number for checking length:"))
m=int(input("Enter number for adding to end:"))
a=count(n)
b=zfill(m)
z=temp(n,m)
print(z)

