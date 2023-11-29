#A pgm to demonstarte AssertError in python for negative input

try:
    x=int(input("Enter a number: "))
    assert(x>0), "Too low value"
    if x>0:
        print("Positive Number")

except AssertionError as ae:
    print(ae)
    
'''Enter a number: -2
Too low value'''
