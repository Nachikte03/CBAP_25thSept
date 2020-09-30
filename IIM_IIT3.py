# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:57:24 2020

@author: vikas
"""

import pandas as pd


print(dir(pd))


from pydataset import data

data('')

mtcars = data('mtcars')

type(mtcars)

mtcars.head(10)


mtcars.to_csv('mtcars.csv')


mtcars.shape


air_df = pd.read_csv('airline.csv')

air_df.shape[0]

air_df.head(10)





s = pd.Series(range(10,21))
s


s= pd.Series(range(100,100+ air_df.shape[0]))

type(s)


ps2 = air_df.set_index(s)

air_df.head()
ps2.head()

ps3 = air_df.set_index(air_df['month'])

ps3.head()

ps3=ps3.drop('month', axis=1)

ps3.head()
ps3.loc['1949-02']
ps3.iloc[2]


import pandas as pd


ps1 = pd.Series([1,4,6,8,11,65], dtype ='int')
ps1

ps1.values

ps1.index

ps1[0]

ps1[1:4]


ps2 =pd.Series([1,2,44,5,77,88], index = ['d','b','c','a','e','f'])
ps2

ps2['b':'a']




ps3 = pd.Series({'a':1, 'b':10, 'c':20})


ps3

ps3['a']
ps3.loc['a']

ps3.iloc[1:3]


'a' in ps3

10 in ps3


ps3['b'] = 30

ps3


course = pd.Series(['BTech', 'MTech', 'BBA', 'MBA', 'BBA'])
strength = pd.Series([100, 50, 200, 75, 80])
fees = pd.Series([2.5, 3,2,4],8)

course
strength
fees


pd1 = pd.DataFrame([course, strength, fees])

pd1


pd2 = pd.DataFrame({'Course': course, 'Strength': strength, 'Fees':fees })
pd2




pd2.index
pd2.columns

pd2.keys

pd2.count()

pd2[1:3]

pd2[:3]
pd2[-2:]
pd2

pd2['Course']

pd2.Course




pd2 is pd2

pd2.Course is pd2.Fees

pd2.Course is pd2.Course


pd2[1:3]
pd2.loc[1:3]

pd2.iloc[1:3]

pd2

ps2 = pd.Series(range(11,15))

pd2=pd2.set_index(ps2)

pd2

pd2[1:3]

pd2.iloc[1:3]

pd2.loc[11:13]

pd2

pd2.Course =='BBA'

pd2

pd2.loc[pd2.Course =='BBA']

pd2[pd2.Course =='BBA']



pd2.loc[pd2.Course =='MBA' , 'Strength' :'Fees']


pd2

pd2.iloc[1,2]=20
pd2


pd2.Fees > 2.5

pd2[pd2.Fees > 2.5]


#missing data

import numpy as np

placed =pd.Series([None, np.nan, 100, None])

placed



#placed.isnull



pd4  = pd.DataFrame([['Vikas', 50, 'M', 10000, 10], [None,None,None,None,None], ['Kanika', 28,None,None,None]])

pd4

pd4.dropna()

pd4
pd4.dropna(axis=0)

pd4.dropna(axis ='columns')
pd4.dropna(axis ='rows')

pd4
pd4.dropna(axis = 'rows', how = 'all')

pd4.dropna(axis = 'rows', how = 'any')

pd4.dropna(axis = 'columns', how = 'all')

pd4.dropna(axis = 'columns', how = 'any')

pd4.dropna(axis=0 , thresh =3)






course = pd.Series(['BTech', 'MTech', 'BBA', 'MBA', 'BBA'])
strength = pd.Series([100, 50, 200, 75, 80])
fees = pd.Series([2.5, 3,2,4],8)

course
strength
fees
placed

pd1 = pd.DataFrame({'course':course, 'strength':strength, 'fees':fees, 'placed':placed})

pd1

pd1.placed.sum()
pd1.strength.max()
pd1.strength.min()
pd1.strength.count()

pd1.placed.isnull()

pd1.placed.notnull()

pd1

pd1[pd1.placed.notnull()]



pd1.placed.fillna(0)

pd1
pd1.placed.fillna(method='ffill')
pd1.placed.fillna(method='bfill')




pl1= pd.Series([1,2,None, 5, 'Vikas', None, 8])
pl1

pl1.fillna(method='ffill')
pl1.fillna(method='bfill')
pl1

pd1 = pd.DataFrame({'strength':strength, 'fees':fees, 'course':course,'placed':placed})

pd1


pd2= pd1.fillna(method='ffill', axis=0)
pd2= pd1.fillna(method='ffill', axis=1)


pd1.dtypes

pd2.dtypes



































