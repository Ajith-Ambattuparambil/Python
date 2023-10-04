a=input("Enter the numbers separated by commas")
a=list(map(int,a.split(',')))
print("Part A")
pos=[item for item in a if(item>0)]
print(pos)
print("Part B")
sqr=[item**2 for item in a]
print(sqr)
print("Part C")
vowels=['a','A','e','E','i','I','o','O','u','U']
s1=input("Enter the word to check the vowels: ")
s2=list(s1)
print(s2)
v1=[item for item in s2 if(item in vowels)]
print(v1)
print("Part D")
noteven=[item for item in a if (item%2==1 or item<0)]
print(noteven)
print("Part E")
year=int(input("Enter the year"))
leap=[i for i in range(2023, year) if ((i%400==0 or (i%100!=0) and i%4==0))]
print(leap)
