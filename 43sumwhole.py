def n_whole(n):
    if(n==0):
        return n
    else:
        return n+n_whole(n-1)
i=int(input("Enter a positive number: "))
print("The sum is: ",n_whole(i-1))
