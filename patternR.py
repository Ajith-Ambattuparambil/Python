for i in range(5):
    for j in range(3):
        if j==0 or j==2 or i==2 or i==0:
            print("*",end="")
        else:
            print(end=" ")   
    print("")