# -*- coding: utf-8 -*-
#Matplot - Scatter Plot
#-----------------------------
#%
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
x
y

#plot

plt.scatter(x, y)

plt.plot(x,y)  #this is faster is customisation is not required
plt.scatter(x, y, color='r')
plt.scatter(x, y, c='r' , marker='*')


size = (30 * np.random.rand(100))

size

plt.scatter(x, y, c='r' , marker='o', s=size)



x = [0,2,4,6,8,10]
y = [0]*len(x)

s = [20*4**n for n in range(len(x))]

plt.scatter(x,y,s=s)
plt.show()

#matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)

#https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html



#eg2
import matplotlib.pyplot
import pylab

x = [1,2,3,4]
y = [3,4,8,6]
size = (30 * np.random.rand(4))**2
matplotlib.pyplot.scatter(x,y, s=size)
matplotlib.pyplot.show()





#Pie Chart
#-----------------------------
#%
import matplotlib.pyplot as plt

sizes=[40,30,30]

labels = ['BBA', 'MBA','PHD']

fig1, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
ax1.axis('equal')
plt.show()




import matplotlib.pyplot as plt

sizes=[4,5,6,3,2]

labels = ['A', 'B','C', 'D', 'E']

fig1, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False)
ax1.axis('equal')
plt.show()



#%%%
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#909090'
plt.rcParams['axes.labelcolor']= '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size']=12



import matplotlib.pyplot as plt
labels = ['Male',  'Female']
percentages = [60, 40]
explode=(0.1,0)
#

color_palette_list = ['#009ACD', '#ADD8E6', '#63D1F4', '#0EBFE9', '#C1F0F6', '#0099CC']

fig, ax = plt.subplots()

ax.pie(percentages, explode=explode, labels=labels, colors= color_palette_list[0:2], autopct='%1.0f%%',  shadow=False, startangle=0,  pctdistance=1.2, labeldistance=1.5)
ax.axis('equal')
ax.set_title("Distribution of Gender in Class", y=.2)
ax.legend(frameon=False, bbox_to_anchor=(0.2,0.8))
plt.show()

