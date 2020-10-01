#Lambda
#-----------------------------
#%

names = ['name','gender','count']
print(names)


# Anonymous Lambda Functions
def f(x):
    return x*2

f(2)


f_lambda= lambda x: x*2

f_lambda(2)



f_lambda = lambda x: x*2
f_lambda2 = lambda y: y*3

print(f(3)) # 6
print(f(5)) # 10
print(f_lambda(3)) # 6
print(f_lambda2(4)) # 12

#import pandas as pd
#input_list = [1,2,3]
#print(pd.lreshape(input_list, lambda x: x * 2))

def my_test2(row):
    return row['a'] % row['c']


#used within other functions
#The power of lambda is better shown when you use them as an anonymous function inside another function
def func1(n):   
    return lambda x : x + n

func2 = func1(2)

func2 = lambda x : x+2

func2

func2(11)
func2(15)


# -*- coding: utf-8 -*-
#lambda function
# small anonymous function
# take any number of arguments but can have one expression

#lamda arguments : expression

import pandas as pd
import numpy as np
#
x1 = lambda a : a + 10
x1(5)

x2 = lambda a, b, c : a + b + c
x2(1,2,3)


#DF
import pandas as pd    

df = pd.DataFrame((np.random.rand(10, 4)*100), columns=list('ABCD'))

df

df.apply(lambda s: s+1)[:3]  #first 3 rows

df.apply(lambda s: s[0] + s[1] + s[2])  #add first rows

df.apply(lambda s: s[0] + s[1], axis=1) #add first 2 columns

#Apply a square root function to every single cell in the whole data frame applymap() applies a function to every single element in the entire dataframe.# Return the square root of every cell in the dataframe
df
df.applymap(np.sqrt)
df

#
dict1 = {'name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],  'year': [2012, 2012, 2013, 2014, 2014],  'reports': [4, 24, 31, 2, 3], 'coverage': [25, 94, 57, 62, 70]}
type(dict1)

dict1

df2 = pd.DataFrame(dict1, index = ['Cochice', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])

df2


capitalizer = lambda x: x.upper()  #lambda function



df2['name'].apply(capitalizer)

#map() applies an operation over each element of a series

df2['name'].map(capitalizer)




