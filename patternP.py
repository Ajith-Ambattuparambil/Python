h=int(input('Enter the height of P: '))
w=int(input('Enter the width of P: '))
for i in range(h):
    for j in range(w):
        if i==0 or j==0 or i==2 or (i==1 and j==2):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print('')