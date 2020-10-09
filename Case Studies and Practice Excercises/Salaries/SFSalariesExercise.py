#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


sal = pd.read_csv('Salaries.csv')


# In[4]:


sal.head()


# ** Check the head of the DataFrame. **

# In[8]:





# ** Use the .info() method to find out how many entries there are.**

# In[5]:


sal.info()


# In[9]:





# **What is the average BasePay ?**

# In[9]:


sal['BasePay'].mean()


# In[10]:





# ** What is the highest amount of OvertimePay in the dataset ? **

# In[10]:


sal.head()


# In[11]:


sal['OvertimePay'].max()


# In[11]:





# In[ ]:





# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[12]:


sal.head()


# In[26]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'] #Not using loc because it is a column where we are looking


# In[12]:





# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[27]:


joseph = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'] #Not using loc because it is a column where we are looking


# In[35]:


sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[ ]:





# In[13]:





# ** What is the name of highest paid person (including benefits)?**

# In[41]:


#sal[sal['EmployeeName']]
#sal['TotalPayBenefits'].max()
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()] #Conditional search


# In[14]:





# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[42]:


sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
# The strange thing I notiche is that he actually owes money and earns nothing


# In[15]:





# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[58]:


#sal[sal['Year'] == 2011]['BasePay'].mean()
#sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
sal.groupby('Year').mean()['BasePay'] #GroupBy method


# In[16]:





# ** How many unique job titles are there? **

# In[61]:


sal['JobTitle'].nunique() # unique gives list of jobs, nunique gives amount of jobs


# In[17]:





# ** What are the top 5 most common jobs? **

# In[70]:


sal['JobTitle'].value_counts().head()
#dataframe['name'].value_counts().idxmax()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[81]:


jobs = sal[sal['Year'] == 2013 ]['JobTitle'].value_counts() #Get first counts of all 2013 Jobs Frequencies
#[vc > 2].index[0]


# In[85]:


jobs[jobs == 1].count() #Secondly get jobs whoe gave 1 single frequency


# In[19]:





# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[94]:


sal[sal['JobTitle'].str.contains('Chief')]['JobTitle'].count()
#df[df['A'].str.contains("hello")]


# In[21]:





# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[95]:


sal.head(10)

