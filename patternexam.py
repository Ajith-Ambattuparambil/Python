i=1
temp=n=5
c=0
while i<=n:
  p=temp
  q=1
  j=1
  while j<=10:
    if j<=5 and p>=1:
        print(p,end=" ")
        p-=1
    if p==0:
        for k in range(c):
            print(end="  ")
        p=-1
    if j>5 and j<=10 and q<=temp:
        print(q,end=" ")
        q+=1
    j+=1
  temp-=1
  c+=2
  i+=1
  print()