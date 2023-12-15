for i in range(5):
    for j in range(5):
        if j==0 or (i==1 and j==1) or (i==2 and j==2) or (i==1 and j==3) or j==4:
            print("*", end="")
        else:
            print(end=" ")    
    print("")        