def reverse_str(s):
   if len(s) == 0:
      return s
   else:
      return reverse_str(s[1:]) + s[0]

i = input('Enter your string:')
print("reversed String: ",reverse_str(i))
