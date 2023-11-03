def even_c(i):
     for item in i:
         if(item==237):
             break
         elif not item%2:
             print(item)
n=input('Enter some integers: ')
n=list(map(int,n.split()))
even_c(n)
