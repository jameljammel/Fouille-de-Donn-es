#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
dict1={
    "name":["John","Jack","Angelica","Isac","pierre","mary","Asma","habib","Ines","Elias","Emna","Donald"],
    "Last Name":["scott", "Azerty","Mcuiop", "Qsdfgh", "luc","moss","lala","lolo","lili","lulu","lele","Trump"],
    "Age":[23,25,29,30,40,45,22,46,18,19,22,62],
    "Role":["AI","Web","Data science", "manager","consultant","AI","AI","Web","AI","AI","Web","manager"],
    "Home adress":["Paris", "Florida", "Berlin", "Madrid","London","Nice","London","Paris","Paris","Paris","Madrid","Florida"],
    "Salary":[1000,1500,2500,1350,2500,1000,1550,1600,1700,1400,1500,800],
    "Promoted":["yes","no","yes","yes","yes","yes","no","yes","no","no","no","yes"]
                   }
data= pd.DataFrame(dict1)
data.to_csv('Data.csv')
new_data=pd.read_csv('Data.csv')
new_data


# In[5]:


from sklearn.preprocessing import LabelEncoder
Encoder=LabelEncoder()

new_data["Promoted"]= Encoder.fit_transform(new_data["Promoted"])
#new_data["Promoted"]
new_data[["Role","Promoted"]].groupby(["Role"],as_index=True).mean()


# In[6]:


plt.title("histogram og differents ages")
plt.xlabel('Age')
new_data['Age'].plot.hist()


# In[7]:


import seaborn as sns
sns.distplot(new_data["Age"],bins=10,hist=True,kde=True,color="red")


# In[8]:


sns.countplot(x="Role",data=new_data)
plt.xticks(rotation=45)


# In[9]:


new_data1=new_data.drop(["Unnamed: 0","name","Last Name","Role","Promoted","Home adress"],axis=1)
sns.boxplot(data=new_data1)


# In[10]:


#la normalization 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
new_data1["Age"]=scaler.fit_transform(new_data1[["Age"]].values)
new_data1["Salary"]=scaler.fit_transform(new_data1[["Salary"]].values)
new_data1

sns.boxplot(data=new_data1)


# In[11]:


g=sns.FacetGrid(new_data,col="Promoted")
g.map(plt.hist,"Age",bins=20)


# In[12]:


grid=sns.FacetGrid(new_data,row="Home adress",col="Promoted",size=2.2,aspect=1.6)

grid.map(sns.barplot,"Role","Salary",alpha=.5,ci=None)

grid.add_legend()


# In[13]:


new_data[["Home adress","Promoted"]].groupby(["Home adress"],as_index=True).mean()
new_data[["Role","Promoted"]].groupby(["Role"],as_index=True).mean()


# In[ ]:




