for i in range(7):
    for j in range(5):
        if j==0 or j==3 or i==3 or i==0:
            print("*",end="")
        else:
            print(end=" ")   
    print("")
