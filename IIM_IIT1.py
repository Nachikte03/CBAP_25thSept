# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:02:48 2020

@author: vikas
"""

import numpy as np

arr = np.arange(0,20)

arr

arr.shape

arr_re = arr.reshape(4,5)

arr_re.shape

arr_re

#arr_re = arr.reshape(4,6)

arr_re.shape

arr_re.shape[0]
arr_re.shape[1]



arr_sc= arr_re.reshape(arr_re.shape[0]*arr_re.shape[1])

arr_sc.shape


arr1 = np.arange(0, 50)

arr1.shape


arr_re_3d = arr1.reshape(2,5,5)

arr_re_3d

arr_re_3d1 =arr_re_3d.reshape(5,5,2)

arr_re_3d1




arr2 = np.arange(0, 6, dtype =float)
arr2

arr3 = arr2.reshape(2,3)
arr2
arr3

arr4 = arr2.reshape(3,2)
arr4


'''
arr5 = arr4.reshape((3,2), order = 'C')
arr5
'''

import numpy as np

a = np.zeros((2,4), dtype =int)
a

b = np.ones((2,5), dtype =int)
b

c=a
c

c = np.empty((2,5))

c = (c)

i=0

while(i<5):
    c=c+b
    i=i+1

c


d= np.eye(3,4)
d


np.linspace(0,12, num=4)

np.linspace(0,100, num=25)



L1= list(range(1,10))


x= np.array(L1, dtype ='int16')

x.dtype


x

x.min()

x.max()

x.max()- x.min()

x.mean()

x.std()

np.mean(x)

np.std(x)




x1 = np.random.normal(loc=0, scale=1, size= 100)

x1

x1.mean()
x1.std()


import matplotlib.pyplot as plt
plt.hist(x1)




x1 = np.random.normal(loc=50, scale=20, size= 1000)

x1

x1.mean()
x1.std()


import matplotlib.pyplot as plt

plt.hist(x1)


x2= np.linspace(10,15,9)

x2

np.diff(x2)

x2.round(2)

np.floor([1.2,1.6])
np.ceil([1.2,1.6])
np.trunc([1.2,1.6])

np.floor([-1.2,-1.6])
np.ceil([-1.2,-1.6])
np.trunc([-1.2,-1.6])


np.full((1,3), [3.14, 7.28, 10])


a= np.array(['Vikas', 'Aman'])

a.dtype

fname= np.char.array(['Vikas', 'Aman'])
fname

lname = np.char.array(['Khullar','Singh'])
lname.dtype

fname + lname



'''

str1=np.array(["This", "is", "NumPy","This", "is", "NumPy" ])

str2=np.array(['This', 'is', 'NumPy'],dtype='<U5')

str3=np.array(['This', 'is', 'NumPy'],dtype='<U7')

str1
str2
str3

len(str1)
len(str2)
len(str3)




dt = np.dtype([('name', np.unicode_, 16), ('grades', np.float64, (2,))])
dt['name']
dtype('|U16')

dt['grades']
dtype(('float64',(2,)))

'''


ns1 = np.array([1,2,3,4])
ns1
ns1.shape

ns1a = ns1[:, np.newaxis]
ns1a
ns1a.shape

ns1a = ns1[ np.newaxis, :]
ns1a
ns1a.shape



ns1 = np.array([1,2,3,4,5,6])
ns1 =ns1.reshape(2,3)
ns1.shape

ns1a = ns1[:,:, np.newaxis]
ns1a.shape
ns1a
ns1



x4= np.array([1,2,3,4,5,6,7])
x2.shape

x5= np.concatenate([x4, np.ones(5)])

x5


x6 = np.array([1,2,3,4,5,6])
x6=x6.reshape(2,3)
x6              



x7 = np.concatenate([x6, np.random.randint(10,20, size=(1,3))], axis=0)

x7

x8 = np.concatenate([x6, np.ones((2,1))], axis=1)

x8

x1 = np.array(list(range(0,6))).reshape(2,3)
x2 = np.array(list(range(0,9))).reshape(3,3)
np.concatenate([x1,x2])


x=np.arange(10,25)
x

x1 = np.split(x, 2)
x1
x1[0]
x2[1]

x2=np.split(x, [3,5], axis=0)

x2

x[:3]
x[3:5]
x[5:]


x=np.arange(1,101)
x.shape

y= x.reshape(20,5)

rows= y.shape[0]

rows= int(rows * (70/100))

rows

np.vsplit(y,[rows])


np.hsplit(y, [2])


x=np.arange(1,10)
x
np.add(x,5)
x= np.multiply(x,7)
x

np.greater(x,40).sum()

np.greater_equal(x, 35)

np.less(x,35)

np.less_equal(x,35)


x

np.all(x>35)
np.all(x>6)

np.any(x>=63)


x = np.random.randint(0,100, size=10, dtype=int)
x

x.sort()

x










