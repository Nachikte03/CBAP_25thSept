#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


# ## Q1 In the above dataset :   
# 
# ### a. In case age is less than 18, replace it with mean of age values.

# In[4]:


Customer_Acq = pd.read_csv("Customer Acqusition.csv")


# In[5]:


df = pd.DataFrame(Customer_Acq)
df.loc[df['Age']<18,'Age'] = df.Age.mean()
df


# ### b. In case spend amount is more than the limit, replace it with 50% of that customer’s limit.

# In[6]:


Spend_amt = pd.read_csv('spend.csv')


# In[12]:


#Merging Spend and Customer Acquistion csv files
df1 = pd.merge(left = Customer_Acq,
               right = Spend_amt,
               left_on = 'Customer',
               right_on = 'Customer',
               how = 'inner',
               indicator = True)
Cust_limit = 0.50*df1.Limit
df1.loc[df1['Amount']>df1['Limit'],['Amount','Limit']] = Cust_limit
df1


# ### c. Incase the repayment amount is more than the limit, replace the repayment with the limit. 

# In[8]:


Repayment = pd.read_csv('Repayment.csv')


# In[9]:


#Merging Repayment and Customer Acquistion csv files
df2 = pd.merge(left = Customer_Acq,
               right = Repayment,
               left_on = 'Customer',
               right_on = 'Customer',
               how = 'inner',
               indicator = True)
df2.drop(df2.columns[11],axis=1)

df2.loc[df2['Amount']>df2['Limit'],['Amount','Limit']] = df2.Limit
df2


# ## Q2. From the above dataset create the following summaries:
# 
# 
# ### a. How many distinct customers exist?

# In[10]:


Customer_Acq.Customer.nunique()


# ### b. How many distinct categories exist?

# In[13]:


print("Product ",df1.Product.nunique())
print("Segment ",df1.Segment.nunique())
print("Type   ",df1.Type.nunique())


# ### c. What is the average monthly spend by customers?

# In[14]:


df1['Month'] = pd.to_datetime(df1['Month'])
df1['month'] = df1['Month'].dt.month
avg_month_spend = df1.groupby(["Customer","month"])['Amount'].mean()
display(pd.DataFrame(avg_month_spend))


# ### d. What is the average monthly repayment by customers?

# In[20]:


df2['Month'] = pd.to_datetime(df2['Month'])
df2['month'] = df2['Month'].dt.month
avg_month_repay = df2.groupby(["Customer","month"])['Amount'].mean()
display(pd.DataFrame(avg_month_repay))


# ### e. If the monthly rate of interest is 2.9%, what is the profit for the bank for each month?

# In[31]:


profit = df2.Amount - df1.Amount
df2['profit'] = profit
profit_mon = df2.groupby(["month"])['profit'].sum()

profit_mon


# ### f. What are the top 5 product types?

# In[12]:


Top_5 = Spend_amt.groupby('Type').sum().sort_values("Amount",ascending = False).head(5)
t = (Top_5).reset_index()
display(t)


# ### g. Which city is having maximum spend?

# In[13]:


group_city = df1.groupby(['City'])['Amount'].sum()
group_city.nlargest(1)


# ### h. Which age group is spending more money?

# In[14]:


group_age = df1.groupby('Age').sum()
amount_spend =  group_age['Amount']
amount_spend.nlargest(1)


# ### i. Who are the top 10 customers in terms of repayment?

# In[15]:


Top_10 = df2.groupby('Customer').sum().sort_values("Amount",ascending = False).head(10)
t = Top_10
display(t)


# ## Q3. Calculate the city wise spend on each product on yearly basis. Also include a graphical representation for the same.

# In[16]:


df1['Month'] = pd.to_datetime(df1['Month'])
df1['year'] = df1['Month'].dt.year
g = df1.groupby(["City","Product","year"])            
tot_amount = g[["Amount"]].sum().add_prefix("Total_")
tot_amount


#Graph
sns.set()
pd.pivot_table(df1, index =['City','Product'],columns ='year',values ='Amount').plot.bar(figsize=(12,6))
plt.ylabel('Total amount spend')
plt.show()


# ## Q4. Create graphs for -
# 
# ### a. Monthly comparison of total spends, city wise

# In[48]:


# sns.set()
# pd.pivot_table(df1, index ='Month',columns = 'City',values = 'Amount').plot(kind='bar')
# plt.ylabel("Total amount spend")
df1['Month'] = pd.to_datetime(df1['Month'])
df1['month'] = df1['Month'].dt.month
sns.set()
pd.pivot_table(df1, index ='City',columns ='month',values="Amount").plot(kind='bar',figsize=(18,6))
ax = plt.subplot(111)
ax.legend(loc='upper center', bbox_to_anchor=(1.045,1), shadow=True, ncol=1)
plt.ylabel('Total amount spend')
plt.show()


# ### b. Comparison of yearly spend on air tickets

# In[18]:


df1['Month'] = pd.to_datetime(df1['Month'])
df1['Year'] = df1['Month'].dt.year

s = df1.loc[(df1.Type == 'AIR TICKET')]
spend = s.groupby(['Year']).aggregate({'Amount':['sum']})

spendgraph=spend.plot.bar(figsize=(8,6))
plt.legend()
plt.ylabel('Total amount spend on Air tickets')
plt.show()


# ### c. Comparison of monthly spend for each product

# In[49]:


df1['Month'] = pd.to_datetime(df1['Month'])
df1['month'] = df1['Month'].dt.month
g = df1.groupby(["Product","month"])            
tot_amount = g[["Amount"]].sum().add_prefix("Total_")
tot_amount


#Graph
sns.set()
pd.pivot_table(df1, index ='Product',columns ='month',values ='Amount').plot.bar(figsize=(18,6))
plt.ylabel('Monthly amount spend')
plt.show()


# ## Q5.Write user defined PYTHON function to perform the following analysis:

# In[50]:


def top_customers():
    prod = input("Enter product name : ")
    time = input("Enter year  : ")
    df2['Month'] = pd.to_datetime(df2['Month'])
    df2['year'] = df2['Month'].dt.year
    df2['Month'] = df2['Month'].values.astype(str)

    if((df2[df2['year']==time]) & (df2[df2['Product']==prod])):
        return df2.groupby(['Customer','City']).sum().sort_values("Amount",ascending = False).head(10) 
        


# In[51]:


top_customers()


# In[33]:





# In[ ]:





