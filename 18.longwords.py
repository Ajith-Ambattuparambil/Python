s=input('Enter words in a comma separated list: ')
s=list(s.split(','))
n=int(input("Enter a number: "))
for i in s:
    if(len(i)>n):
        print(i)
