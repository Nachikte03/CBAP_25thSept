# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:02:48 2020

@author: vikas
"""

stud = {'rollno':1, 'name':' Vikas', 'Admit': True, 1:'Vikas' }

stud

stud ['rollno']

stud[1]

car= {'brand': 'Honda', 'model':'Jazz', 'year': 2020}

car['brand']

car.get('brand')

#mutable

car['brand'] ='Tata'

car

car.values()

car.keys()

car.items()


for i in car.values():
    print(i)
    
    
for i,j in car.items():
    print(i)
    print(j)


car.pop('year')


car.popitem()


car['color'] ='Black'


car.popitem()


del car['brand']

car


copy_car= car
car
copy_car

car['color']= 'Black'

car
copy_car


copy_car= car.copy()
car
copy_car

car['color1']= 'Black'

car
copy_car

#car('color', 'model')

type(car)



#Tupple

T1 = (2,1,3,4)
T1

Unmutable

T1[0]=10

T2= (2, 'Vikas')

T2




for i in T1:
    print(i)



T1 = ("Vikas", "Raman", "Aditya", 11)


1 in T1


T1.append("Khullar")

T1.remove()




#Enumerate

L1 = ["Tiger", "Monkey", "Lion"]


for i in L1:
    print(i)


E1 = enumerate(L1)
E1

for i in E1:
    print(i)
        
E1 = enumerate(L1, start=10)
E1

for i in E1:
    print(i)



L1= list(range(100,120))

L1

E1 = enumerate(L1, start=10)
E1



for i, j in E1:
    print(i, j)
    if(j==109):
        break
    
    
for i, j in E1:
    print(i, j)

        

for i, j in E1:
    print(i, j)





# frozen set
    
    
fzs1 = frozenset([1,2,3,4])

type(fzs1)


b= set([1,2,3])
type(b)

b.add(6)

b


fzs1.add(10)


fzs1.union(b)


vowels = ('a', 'e', 'i','o','u')

fzs1= frozenset(vowels)

s1= set(['a', 'b', 'z'])


fzs1.intersection(s1)




#Functions

'''
def [function_name]():
    Statments1
    Statments2
'''
'''
function_name()
'''


def oper(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

oper(10,20)
oper(30,20)

def printhello():
    print("Hello")


printhello()


def printhello(batch):
    print("Hello "+batch)


printhello("IIT/IIM")


def printhello(batch, batch1):
    print("Hello "+batch + batch1)


printhello("IIT","IIM")




def oper(a,b):
    return(a+b, a-b, a*b,a/b, "Vikas")
    
print(oper(10,20))


def oper(name, email="Nil"):
    print(name)
    print(email)

oper("vikas", "vikas@gmail.com")

oper("vikas")






import random

x= random.randint(1,10)
x

L1 = [11,22,33,44,55]

random.choice(L1)

random.choices(L1, k=3)




w_s ={20,30,40,50}

w =random.choice(tuple(w_s))
print(w)

ws =random.choices(tuple(w_s), k=10)
print(ws)



w_d = {"Kelly": 50, "Red":68, "Jhon":30}

key = random.choice(tuple(w_d.keys()))
key


val = random.choice(tuple(w_d.values()))
val



for i in range(5):
    random.seed(1)
    print(random.randint(1,1000))



for i in range(5):
    print(random.randint(1,1000))









