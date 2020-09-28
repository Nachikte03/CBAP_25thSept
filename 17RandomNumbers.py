# -*- coding: utf-8 -*-
#Random Numbers
#https://pynative.com/python-random-choice/


import random


from random import randint
x = randint(1,10)
x


#Random Choices


import random
list  = [111,222,333,444,555]
print("random.choice() to select random item from list - ", random.choice(list))
print("\nrandom.choice() to select random item from list - ", random.choice(list))


#https://www.python-course.eu/weighted_choice_and_sample.php
from random import choice
choice("abcdefghij")
professions = ["scientist", "philosopher", "engineer", "priest"]
choice(professions)
choice(("beginner", "intermediate", "advanced"))

import random
sampling = random.choices(professions, k=10)
sampling


#---
import random
weight_set = {20, 35, 45, 65, 82}  #set
weight = random.choice(tuple(weight_set))
print ("Randomly item from Set is - ", weight)


#
import random
weight_dict = { "Kelly": 50,  "Red": 68,  "Jhon": 70,  "Emma" :40 }
key = random.choice(list(weight_dict))
print ("Random key value pair from dictonary is ", key, " - ", weight_dict[key])

#
from random import randrange
movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']
random_index = randrange(len(movie_list))
item = movie_list[random_index]
print ("Randomly selected item and its index is - ", item, "Index - ", random_index)


#same element
import random
float_list = [22.5, 45.5, 88.5, 92.5, 55.4]


# random module is imported 
'''Seed function is used to save the state of a random function, 
so that it can generate same random numbers on multiple executions 
of the code on the same machine or on different machines 
(for a specific seed value). The seed value is the previous 
value number generated by the generator. 
For the first time when there is no previous value, it uses current system time.
'''
random.seed(100)

print(random.randint(1, 1000))


import random 
for i in range(5): 
	# Any number can be used in place of '0'. 
	random.seed(100) 
	print(random.randint(1, 1000))
	
random.seed(100)
random.randint(1,1000)

random_item = random.choice(float_list)
print("random item", random_item)
random.seed(4)
random_item = random.choice(float_list)
print("random item", random_item)



#Choose a random element from a multidimensional array in Python
import numpy
array = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 

print("Printing 2D Array")
print(array)

print("Choose random row from 2D array")
randomRow = numpy.random.randint(3, size=1)
print(array[randomRow,:])



#https://pynative.com/python-random-choice/
