def sum_d(n):
    if not(n//10):
        return n
    else:
        return ((n%10)+sum_d(n//10))
i=int(input("Enter a number: "))
print('Sum = ',sum_d(i))
