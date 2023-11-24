f=False
k=False
try:
    f=open("demofile.txt")
    k=open("copied.txt","w")
    k.write(f.read())
except IOError as io:
    print(io)
finally:
    if f:
        f.close()    
