string=input("Enter the string: ")
start=string[-1::]
end=string[:1:]
output=start+string[1:-1:]+end
print("The swapped string is",output)
