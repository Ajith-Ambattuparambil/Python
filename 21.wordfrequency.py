word=input("Enter the word: ")
letter={}
for i in word:
    letter[i]=letter.get(i,0)+1
print(letter)
    
