def rev(name):
    for word in name[::-1]:
        print(word,end=' ')
n=input("Enter the name: ")
n=n.split()
rev(n)

        
