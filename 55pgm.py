f=False
try:
    f=open("demofile.txt","r")
    l=len(f.readlines())
    print("length of file: ",l)
except IOError as io:
    print(io)
finally:
    if f:
        f.close()
