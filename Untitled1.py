#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
sns.set_theme(style="whitegrid")
tips = sns.load_dataset("tips")
ax = sns.boxplot(x=tips["total_bill"])


# In[2]:


import numpy
pyplot.subplot(121)
pyplot.boxplot([[1, 2, 3, 4, 5, 13], [6, 7, 8, 10, 10, 11, 12], [1, 2, 3]])


# In[3]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid='True')


# In[11]:


import pandas as pd
import numpy as np
columns=[1, 2, 3, 4, 5, 6, 7, 8]
columns.plot.box


# In[15]:


import matplotlib.pyplot as plt
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,18]
plt.boxplot(x)
plt.show()


# In[ ]:




