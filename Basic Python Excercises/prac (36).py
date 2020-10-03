"""Write a function that takes a vowel character (i.e. a 
string of length 1) and returns True if it is a vowel, 
False otherwise."""

vowels = ['a', 'e', 'i', 'o', 'u']

def vornot(str):
  if str in vowels:
      print("Valid Vowel Char")
      return True
  else:
      print("Not Valid Vowel Char")
      return False

#test
print (vornot('f'))
