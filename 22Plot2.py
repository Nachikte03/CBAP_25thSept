#Box Plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_1 = np.random.normal(100, 10, 200) 
data_2 = np.random.normal(90, 20, 200) 
data_3 = np.random.normal(80, 30, 200) 
data_4 = np.random.normal(70, 40, 200) 
data = [data_1, data_2, data_3, data_4] 

data  

fig = plt.figure(figsize =(5, 5)) 
# Creating axes instance 
ax = fig.add_axes([0,1,2,3]) 
ax

# Creating plot 
bp = ax.boxplot(data)

# show plot 
plt.show() 




#Different dataset
import pandas as pd
data = pd.read_csv('brain_size.csv', sep=';', na_values='.')
data
# Box plot of FSIQ and PIQ (different measures od IQ)
plt.figure(figsize=(4, 3))
data.columns

data.boxplot(['FSIQ', 'PIQ', 'VIQ'])

plt.show();

data
data['FSIQ'] - data['PIQ']
# Boxplot of the difference
plt.figure(figsize=(4, 3))
plt.boxplot(data['FSIQ'] - data['PIQ'])

plt.xticks((1, 0, 2), ('FSIQ - PIQ','VV', 'AA' ))

plt.yticks((-10, -15,), ("BB", "AA",))

plt.show();


