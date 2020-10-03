#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pandas import DataFrame
import seaborn as sns
import datetime


# ## Q1. Import claims_data.csv and cust_data.csv which is provided to you and combine the two datasets appropriately to create a 360-degree view of the data.

# In[2]:


claims_data = pd.read_csv("claims.csv")
claims_data


# In[3]:


cust_data = pd.read_csv("cust_demographics.csv")
cust_data


# In[4]:


df = pd.merge(left =  cust_data,
              right = claims_data,
              left_on = "CUST_ID",
              right_on = "customer_id",
              how = "inner",
              indicator = True
             )
data = df
data


# In[5]:


data=df.drop(columns = '_merge')
data.dropna(inplace = True)


# ## Q2. Perform a data audit for the datatypes and find out if there are any mismatch within the current datatypes of the columns and their business significance.

# In[6]:


#Data Audit
d=data.dtypes[data.dtypes!='object'].index.values
data[d]=data[d].astype('float64')
mean=DataFrame({'mean':data[d].mean()})
std_dev=DataFrame({'std_dev':data[d].std()})
missing= DataFrame({'missing':data[d].isnull().sum()})
minimum=DataFrame({'min':data[d].min()})
maximum=DataFrame({'max':data[d].max()})
DA=pd.concat([mean,std_dev,missing,minimum,maximum],axis=1,sort = False)

c=data.dtypes[data.dtypes=='object'].index.values
Mean=DataFrame({'mean':np.repeat('Not Applicable',len(c))},index=c)
Std_Dev=DataFrame({'std_dev':np.repeat('Not Applicable',len(c))},index=c)
Missing=DataFrame({'missing':data[c].isnull().sum()})
Minimum=DataFrame({'min':np.repeat('Not Applicable',len(c))},index=c)
Maximum=DataFrame({'max':np.repeat('Not Applicable',len(c))},index=c)
Da=pd.concat([Mean,Std_Dev,Missing,Minimum,Maximum],axis =1,sort = False)
Dq = pd.concat([DA,Da])


# In[7]:


Dq.to_csv('DataAudit.csv')


# In[8]:


dq = pd.read_csv("DataAudit.csv")
dq.rename(columns = {'Unnamed: 0':''})


# ## Q3. Convert the column claim_amount to numeric. Use the appropriate modules/attributes to remove the sign.

# In[9]:


data['claim_amount'] = data['claim_amount'].astype(str)
data['claim_amount'] = data['claim_amount'].str.replace('$','')
data['claim_amount'] = pd.to_numeric(data['claim_amount'])
data


# ## Q4. Of all the injury claims, some of them have gone unreported with the police. Create an alert flag (1,0) for all such claims.

# In[10]:


data['Flag'] = np.where(data.police_report == 'Unknown',0,1)
data


# ## Q5. Retain the most recent observation and delete any duplicated records in the data based on the customer ID column.

# In[11]:


data.drop_duplicates(subset = 'CUST_ID',keep = 'last')


# ## Q6. Check for missing values and impute the missing values with an appropriate value.(mean for continuous and mode for categorical)

# In[12]:


#Categorical values
data['total_policy_claims'].replace(np.NaN,data['total_policy_claims'].mode())

#Continous values
data['claim_amount'].replace(np.NaN,data['claim_amount'].mean())

data


# ## Q7. Calculate the age of customers in years. Based on the age, categorize the customers :

# In[13]:


curr_year = pd.to_datetime('today').year
dob_year = pd.DatetimeIndex(data['DateOfBirth']).year          #extract year from DateOfBirth
x = dob_year-100                                               # for the years which belongs to 60's
v = curr_year - x
y = curr_year - dob_year
data['age'] = (np.where(dob_year > curr_year,v,y))
#Categorising
data.loc[(data.age < 18),'AgeGroup'] = 'Children'
data.loc[(data.age >=18) & (data.age <30),'AgeGroup'] = 'Youth'
data.loc[(data.age >=30) & (data.age <60),'AgeGroup'] = 'Adult'
data.loc[(data.age >=60),'AgeGroup'] = 'Senior'

data


#  ## Q8. What is the average amount claimed by the customers from various segments?

# In[14]:


data.groupby('Segment').mean()[['claim_amount']]


# ## Q9. What is the total claim amount based on incident cause for all the claims that have been done at least 20 days prior to 1st of October, 2018.

# In[16]:


# from datetime import date,timedelta  
# days_before = (date.today()-timedelta(days=20)).isoformat()


# ## Q10. How many adults from TX, DE and AK claimed insurance for driver related issues and causes?

# In[ ]:


count = data.loc[((data.State == 'TX') | (data.State == 'DE') | (data.State == 'AK')) & (data.incident_cause == 'Driver error') & (data.AgeGroup == 'Adult'),['AgeGroup']].count()
count


# ## Q11. Draw a pie chart between the aggregated value of claim amount based on gender and segment.

# In[ ]:


import matplotlib.pyplot as plt
# claim = data.groupby(['Segment','gender']).aggregate({'claim_amount':['sum']})
# claim
claim = pd.pivot_table(data, index =['Segment'],columns ='gender',values ='claim_amount')


claim.plot(kind='pie', 
            labels=['Platinum','Silver','Gold'],
            colors=['r', 'g', 'b'],
            autopct='%.1f%%', # to get percentage and round off appropriately
            fontsize=10,
            subplots='true')

plt.title('Pie Chart of claim amount',fontsize=20)

plt.axis('equal')
plt.show()




# ## Q12. Among males and females, which gender had claimed the most for any type of driver related issues? E.g. This metric can be compared using a bar chart

# In[ ]:


issue = data.loc[data['incident_cause'].isin(['Driver error','Other driver error'])]
group_gender = issue.groupby(['gender'])['claim_amount'].sum()
group_gender.nlargest(1)


# In[ ]:


# Comparing using a bar chart
group_gender.plot(kind = 'bar')


# ### As we can see from the above figure and the value we got, it is been clear that male has claimed the most for any type of driver related issues.

# ## Q13. Which age group had the maximum fraudulent policy claims? Visualize it on a bar chart.

# In[ ]:


issue1 = data.loc[data['fraudulent'] == 'Yes']
group_age = issue1.groupby(['AgeGroup'])['total_policy_claims'].sum()
group_age.plot(kind = 'bar')


# ## Q14. Visualize the monthly trend of the total amount that has been claimed by the customers. Ensure that on the “month” axis, the month is in a chronological order not alphabetical order.

# In[19]:


data['claim_date'] = pd.to_datetime(data['claim_date'])
data['Claim_date'] = data['claim_date'].dt.month
sns.set()
data.head()
pd.pivot_table(data, columns ='Claim_date',values="claim_amount").plot(kind='bar')
plt.ylabel('Total amount spend')
plt.show()


# ### Based on the conclusions from exploratory analysis as well as suitable statistical tests, answer the below questions. Please include a detailed write-up on the parameters taken into consideration, the Hypothesis testing steps, conclusion from the p-values and the business implications of the statements.
# ### 16. Is there any similarity in the amount claimed by males and females? 

# In[21]:


claim_male = data['claim_amount'].loc[data['gender']=="Male"]

claim_female = data['claim_amount'].loc[data['gender']=="Female"]


# In[22]:


print("The average amount claimed by males is {}".format(claim_male.mean()))

print("The average amount claimed by females is {}".format(claim_female.mean()))


# ### Two Sample t-Test(Independent)

import scipy.stats as stats
# 1. Two different assumptions : Amount Claimed by Males and Females have equal var
#                                : unqual variance

# 2. If t value is same in both the cases : variance in A and B is same

# 3. If t value in different : var in A != var B : 
#      consider the results from unequal variance

#H0 : Amount Claimed by Males == Amount Claimed By Females
#H1 : Amount Claimed by Males <> Amount Claimed by Females
# In[23]:



eq_var = stats.ttest_ind(a= claim_male,
                b= claim_female,
                equal_var=True)    # equal variance
eq_var.statistic


# In[24]:


uneq_var = stats.ttest_ind(a= claim_male,
                b= claim_female,
                equal_var=False)    # UnEqual variance
uneq_var.statistic


# In[25]:


# We'll cosider equal variance since the t score is not having a huge difference
uneq_var.statistic - eq_var.statistic


# In[26]:


t = eq_var.statistic

p = eq_var.pvalue

print(" For the above test, the t-score is {} and the p-value is {}".format(t,p))

if(p<0.05):
    print('We reject null hypothesis')
else:
    print('We fail to reject null hypothesis')


# * Since the significance value of the test is greater than 0.05, we can safely conclude that there is a similarity between amount claimed by males and females

# ### 17. Is there any relationship between age category and segment?

# ### Chi-Square Test

'''
H0 : Observed == Expected
    (No relation between category and segment)
    
Ha : Observed != Expected
    (There is a realtionship between category and segment)
'''
# In[28]:


agecat_seg_xtab = pd.crosstab(data.AgeGroup, data.Segment, margins = True)
agecat_seg_xtab


# In[29]:


x2test_17 = stats.chi2_contingency(observed= agecat_seg_xtab)

x2test_17


# In[30]:


print("The chi square stat is {} and the p value is {}".format(x2test_17[0],x2test_17[1]))


# * Since the significance value of the test is greter than 0.05, we fail reject the null hypothesis. Therefore there is no relationship between age category and segment

# ### 18. The current year has shown a significant rise in claim amounts as compared to 2016-17 fiscal average which was 10,000.

# In[ ]:





# ### 19. Is there any difference between age groups and insurance claims?

# ### F-Test/Anova
'''
H0  : mean(AgeGroup[Youth]) == mean(AgeGroup[Adult])
             (No difference between age groups and insurance claims or No influence of age groups on insurance claims)
                       
Ha  :  mean(AgeGroup[Youth]) != mean(AgeGroup[Adult])
                       (There is some difference between age groups and insurance claims or there is some influence of age groups on insurance claims)  
'''
# In[31]:


age_group_1 = data['total_policy_claims'].loc[data['AgeGroup']=="Youth"]
age_group_2 = data['total_policy_claims'].loc[data['AgeGroup']=="Adult"]
# Perfrom the Anova
anova = stats.f_oneway(age_group_1,age_group_2)
# Statistic :  F Value
f = anova.statistic
p = anova.pvalue
print("The f-value is {} and the p value is {}".format(f,p))
if(p<0.05):
    print('We reject null hypothesis')
else:
    print('We fail to reject null hypothesis')


# * Since the significance value of the test is greater than 0.05, we fail reject the null hypothesis. Therefore, there is no difference between age groups and insurance claims or No influence of age groups on insurance claims

# ### 20. Is there any relationship between total number of policy claims and the claimed amount?

# ### Correlation

# In[34]:


data.total_policy_claims.corr(other=data.claim_amount)


# * Hence total number of policy claims is inversely proportional to the claimed amount

# In[36]:


sns.lmplot(x = "total_policy_claims", y = "claim_amount",data = data)


# In[ ]:





