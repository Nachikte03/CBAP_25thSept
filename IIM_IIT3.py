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



