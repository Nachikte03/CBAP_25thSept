#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___
# # Ecommerce Purchases Exercise
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# ____
# ** Import pandas and read in the Ecommerce Purchases csv file and set it to a DataFrame called ecom. **

# In[1]:


import pandas as pd


# In[2]:


ecom = pd.read_csv('Ecommerce Purchases')


# In[86]:





# **Check the head of the DataFrame.**

# In[4]:


ecom.head()


# In[87]:





# ** How many rows and columns are there? **

# In[5]:


ecom.info()


# In[88]:





# ** What is the average Purchase Price? **

# In[8]:


ecom.head(1)


# In[9]:


ecom['Purchase Price'].mean()


# In[90]:





# ** What were the highest and lowest purchase prices? **

# In[10]:


ecom['Purchase Price'].max()


# In[92]:





# In[11]:


ecom['Purchase Price'].min()


# In[93]:





# ** How many people have English 'en' as their Language of choice on the website? **

# In[19]:


ecom[ecom['Language']=='en'].count()
#sal['JobTitle'].value_counts().head()


# In[ ]:





# In[94]:





# ** How many people have the job title of "Lawyer" ? **
# 

# In[20]:


ecom.head(1)


# In[25]:


ecom[ecom['Job'].str.contains("Lawyer")]['Job'].count()


# In[95]:





# ** How many people made the purchase during the AM and how many people made the purchase during PM ? **
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) ) **

# In[28]:


ecom['AM or PM'].value_counts().head()


# In[96]:





# ** What are the 5 most common Job Titles? **

# In[29]:


ecom['Job'].value_counts().head()


# In[97]:





# ** Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction? **

# In[30]:


ecom.head(1)


# In[32]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# In[ ]:





# In[99]:





# ** What is the email of the person with the following Credit Card Number: 4926535242672853 **

# In[34]:


ecom[ecom['Credit Card']==4926535242672853]['Email']


# In[100]:





# ** How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[46]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price'] > 95)].count()


# In[101]:





# ** Hard: How many people have a credit card that expires in 2025? **

# In[60]:


ecom[ecom['CC Exp Date'].str.contains("/25")]['CC Exp Date'].count() #Using str.contains to find the /25 year


# In[102]:





# ** Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...) **

# In[72]:


ecom.head(3)


# In[78]:


ecom['Email Domain'] = ecom['Email'].str.split("@").str[1] #Generate another column with email dominas using str split at the @ element, we keep the domain only
#ecom['Email'].str.split("@").str[1]


# In[80]:


ecom.head(1)


# In[82]:


ecom['Email Domain'].value_counts().head()
#ecom['Job'].value_counts().head()


# In[56]:





# # Great Job!
