# -*- coding: utf-8 -*-
#Functions
#Block of code which only runs when it is called
#can pass data, known parameters into function
#it can return data as result
#defined using keyword def with colon :



#declaration or defination of function

def oper():
    print(a+b)
    print(a-b)
    print(a*b)



#calling that declared Functions


a=10
b=20



oper()

oper()

oper()


def printHello():
    print("Hello ")
    
    
printHello()


def printHello2(fname, lname):
    print("Hello \t" + fname + lname)


printHello2() #error


printHello2('vikas', 'khullar')



def printHello3(name='Student'):
    print("Hello \t" + name)


printHello3()  #without value

printHello3('Dhiraj')



def printdef1(a,b):
    print("name "+a+b)

printdef1("Amit", "Saho")



L1=['a','b','c']

L2=['d','e','f']

L3=['g','h','i']


for i in L1:
    print("Hello \t" + i)



for i in L2:
    print("Hello \t" + i)
    
    

for i in L3:
    print("Hello \t" + i)
    
    
#passing a list 
def printHello4(names):
    for i in names:
        print("Hello \t" + i)

printHello4(L1)

printHello4(L2)

printHello4(L3)



printHello4()
printHello4('Dhiraj')

printHello4(['Dhiraj','Kounal','Pooja'])

namelist  = ['Student1','Student2','Student3']
printHello4(namelist)


#retun values

def totalSale(x=0,y=0):
    return(x + y)
    
totalSale()
totalSale(5,10)
