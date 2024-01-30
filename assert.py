try:
    x=int(input("Enter a number:"))
    if x<90 or x>120:
        raise ValueError
    else:
        print(x)
except ValueError:
    print("Abnormal condition")
