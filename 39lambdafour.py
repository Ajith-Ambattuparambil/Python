large = lambda a,b:a if a>b else b
divisible=lambda a:not a%5
removed = lambda s:[x for x in s.split() if len(x)<5]
n=int(input("First number: "))
m=int(input("Second number: "))
s=input('Enter a iist of words: ')
print("Largest number is: ",large(m,n))
print("Is first number divisible by 5?",divisible(m))
print("Remove all strings", removed(s))

