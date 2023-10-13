s=input("Enter the sentence: ")
w={}
for i in s.split():
    w[i.lower()]=w.get(i,0)+1
print(w)
