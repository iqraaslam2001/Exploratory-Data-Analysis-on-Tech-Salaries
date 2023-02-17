#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[18]:


import warnings


# In[19]:


warnings.filterwarnings('ignore')


# In[20]:


salary=pd.read_csv("C:/Users/IQRA/Desktop/Projects/salary.csv")


# In[21]:


salary.head()


# In[22]:


salary.tail()


# In[23]:


salary.shape


# In[24]:


salary.columns


# In[25]:


salary.info()


# In[26]:


salary.isna().sum()


# In[31]:


salary.nunique()


# In[33]:


salary1 = salary[['title', 'gender', 'Masters_Degree', 'Bachelors_Degree', 'Doctorate_Degree',
                 'Highschool', 'Some_College', 'Race_Asian', 'Race_White','Race_Two_Or_More', 
                 'Race_Black', 'Race_Hispanic', 'Race', 'Education']]


# In[34]:


for i in salary1.columns:
     print(salary1[i].unique())


# In[35]:


for i in salary1.columns:
     print(salary1[i].value_counts())


# In[38]:


for i in salary1.columns:
    plt.figure(figsize = (15,6))
    sns.countplot(salary1[i], data = salary1)
    plt.xticks(rotation=90)
    plt.show()


# In[39]:


for i in salary1.columns:
    plt.figure(figsize = (15,6))
    salary1[i].value_counts().plot(kind = 'pie', autopct = '%1.1f%%')
    plt.xticks(rotation = 90)
    plt.show()


# In[41]:


salary2 = salary[['company', 'title', 'totalyearlycompensation','location',
                      'yearsofexperience', 'yearsatcompany', 'gender','Race', 'Education']]


# In[42]:


salary2 = pd.DataFrame(salary2)


# In[43]:


salary2.head()


# In[44]:


salary2['title'].value_counts()


# In[45]:


salary2.info()


# In[46]:


salary2.fillna({'company':'NA', 'gender':'NA','Race': 'NA', 'Education': 'NA'}, inplace = True)


# In[47]:


salary2.isnull().sum()


# In[50]:


job_titles = salary2[['company','title', 'totalyearlycompensation']].groupby(['title']).mean().round(2).sort_values('totalyearlycompensation',ascending = False)


# In[59]:


plt.figure(figsize = (15,6))
job_titles.plot.bar()
plt.title('Highest Average Annual Compensation by Job Title', size=17)
plt.xlabel('Job Title', size = 15)
plt.ylabel('Average Annual Compensation ($)', size = 15)
plt.show()


# In[60]:


top_jobs = salary2['title'].value_counts()
plt.figure(figsize = (15,6))
top_jobs.plot.bar()
plt.title("Number of Workers in Each Job Title", size=17)
plt.xlabel('Number of Workers', size = 15)
plt.ylabel('Job Title', size = 15)
plt.show()


# In[64]:


plt.figure(figsize = (15,6))
companies_with_most_tech_workers = salary2['company'].value_counts()[:10].plot.bar();
plt.title('Top 10 companies with the highest number of tech workers', size=17)
plt.xlabel('Number of Workers', size = 15)
plt.ylabel('Company', size = 15)
plt.show()


# In[65]:


plt.figure(figsize = (15,6))
highest_paying_companies = salary2[['company','title','totalyearlycompensation']].groupby(['company']).max().sort_values('totalyearlycompensation',ascending = False).head(20).plot.bar();
plt.title('Top 10 Companies that paid the highest compensation', size=10)
plt.xlabel('Compensation in Millions ($)', size = 15)
plt.ylabel('Company', size = 15)
plt.show()


# In[66]:


salary2['gender'].replace('Title: Senior Software Engineer', 'NA', inplace = True)


# In[68]:


pay_scale_by_gender = salary2[['totalyearlycompensation', 'gender']].groupby(['gender']).mean().round(2)
plt.figure(figsize = (15,6))
pay_scale_by_gender.sort_values('totalyearlycompensation', ascending = False).head(10).plot.bar(legend = False)
plt.title('Compensation by Gender', size=20)
plt.xlabel('Compensation ($)', size = 15)
plt.ylabel('Gender', size = 15)
plt.show()


# In[69]:


male_salaries = salary2[salary2.gender == 'Male'].copy()
top4_male_salaries = male_salaries.nlargest(4,'totalyearlycompensation')
plt.figure(figsize = (15,6))
top4_male_salaries.plot.bar(x = 'title', y = 'totalyearlycompensation', legend = False)
plt.title('Top 4 Male Salaries', size=20)
plt.xlabel('Compensation in Millions ($)', size = 15)
plt.ylabel('Title', size = 15)
plt.show()


# In[77]:


female_salaries = salary2[salary2.gender == 'Female'].copy()
top4_female_salaries = female_salaries.nlargest(4,'totalyearlycompensation')
plt.figure(figsize = (15,6))
top4_female_salaries.plot.bar(x = 'title', y = 'totalyearlycompensation', legend = False)
plt.title('Top 4 Female Salaries', size=20)
plt.xlabel('Compensation in Millions ($)', size = 15)
plt.ylabel('Title', size = 15)
plt.show()


# In[71]:


plt.figure(figsize = (15,6))
gender_distribution = salary2['gender'].value_counts().plot.bar(figsize = (15,6))
plt.title('Gender Distribution', size=20)
plt.xlabel('Count', size = 15)
plt.ylabel('Gender', size = 15)
plt.show()


# In[73]:


plt.figure(figsize = (15,6))
pay_by_education = salary2[['totalyearlycompensation','Education']].groupby(['Education']).mean().round().sort_values('totalyearlycompensation', ascending = False).plot.bar(figsize=(12,8))
plt.title('Compensation By Education', size=20)
plt.xlabel('Compensation ($)', size = 15)
plt.ylabel('Education', size = 15)
plt.show()


# In[78]:


plt.figure(figsize = (15,6))
education_distribution = salary2['Education'].value_counts().plot.bar()
plt.title('Distribution of Education', size=20)
plt.xlabel('Count', size = 15)
plt.ylabel('Education', size = 15)
plt.show();


# In[79]:


plt.figure(figsize = (15,6))
years_of_experience = salary2[['title', 'totalyearlycompensation','yearsofexperience']].groupby(['yearsofexperience'])                                                                                             .mean()                                                                                             .round(2)                                                                                             .sort_values('totalyearlycompensation', ascending = False)                                                                                             .head(20).plot.bar()
plt.title('Years of Experience VS Compensation', size=17)
plt.xlabel('Compensation ($)', size = 15)
plt.ylabel('Years of Experience', size = 15)
plt.show();


# In[80]:


plt.figure(figsize = (15,6))
location = salary2['location'].value_counts().iloc[:20].plot.bar()
plt.title('Top 20 locations of tech jobs', size=17)
plt.xlabel('Number of workers', size = 15)
plt.ylabel('Company', size = 15)
plt.show();


# In[ ]:




