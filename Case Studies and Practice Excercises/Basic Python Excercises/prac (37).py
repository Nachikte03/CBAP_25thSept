"""Write a function translate() that will translate a text 
into "rovarspraket" (Swedish for "robber's language"). 
That is, double every consonant and place an occurrence 
of "o" in between. For example, translate("this is fun") 
should return the string "tothohisos isos fofunon"."""

import string

all_letters = string.ascii_letters
all_letters
vowels = ['a','e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

chr1=[]

for chr in all_letters:
    if chr not in vowels:
       chr1.append(chr) 
chr1

consonants = [chr for chr in all_letters if chr not in vowels]
consonants


def robberlang(str):
  result = ""
  for c in str:
    print("consonent " +c)
    if c in consonants:
      result = result + c+'o'+c
      print(result)
    else:
      result += c
      print(result)
  return result

#test
print (robberlang("This is kind a fun"))
print robberlang("I Think YoU Might BE righT!")