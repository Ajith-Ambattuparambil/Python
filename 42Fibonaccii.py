def fib(n):
    if(n<=1):
        return n
    else:
        return fib(n-1)+fib(n-2)
i=int(input('Enter a number: '))
print('The fibonacci number is: ',fib(i))
    
