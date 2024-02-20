n=int(input("Enter number:"))
m=n
n=(n//10)*10
m=m-n
print("even") if m in (0,2,4,6,8) else print("odd")