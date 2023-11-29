#Pgm that accepts an integer from user and raises valueError with argument 'Abnormal',if the reading is not within 90 - 120
try:
    x=int(input("Enter a number: "))
    if x<90 or x>120:
        raise ValueError
except ValueError:
    print("Abnormal Condition!!!")
else:
    print("Okay")

    
'''Enter a number: 15
Abnormal Condition!!!'''
