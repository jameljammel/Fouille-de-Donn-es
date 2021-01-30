#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import*
import numpy 
import matplotlib.pyplot 
iris = datasets.load_iris()


# In[29]:


print(iris.feature_names)


# In[3]:


print(iris)


# In[7]:


print(iris.target)


# In[8]:


print(iris.target_names)


# In[9]:


print(iris.feature_names)


# In[10]:


moyenne = iris.data.mean(0)
print(moyenne)


# In[11]:


moyenned = iris.data.mean(1)
print(moyenned)


# In[13]:


ecart = iris.data.std(0)
print(ecart)


# In[14]:


ecart = iris.data.std(1)
print(ecart)


# In[22]:


max = iris.data.max(0)
print(max)


# In[23]:


max = iris.data.max(1)
print(max)


# In[24]:


min = iris.data.min(1)
print(min)


# In[25]:


size = iris.target.size
print(size)


# In[32]:


shape = iris.target.shape
print(shape)


# In[1]:


from sklearn.datasets import fetch_mldata
mnist = fetch_mldata('MNIST original', data_home=custom_data_home)


# In[ ]:




