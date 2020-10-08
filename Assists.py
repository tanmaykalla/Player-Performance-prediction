#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

vardy=pd.read_csv("fpl - Jamie Vardy.csv")


# In[11]:


vardy.info()

vardy.isnull()
# In[15]:


X=vardy.iloc[:,[1,3,8,9,15]].values
Y=vardy["assists"]


# In[17]:


from sklearn.model_selection import train_test_split


# In[19]:


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42)


# In[20]:


from sklearn.linear_model import LogisticRegression


# In[21]:


model_assists=LogisticRegression()


# In[22]:


model_assists.fit(X_train,Y_train)


# In[23]:


predictions=model_assists.predict(X_test)


# In[24]:


from sklearn.metrics import classification_report


# In[26]:


classification_report(Y_test,predictions)


# In[27]:


from sklearn.metrics import confusion_matrix


# In[28]:


confusion_matrix(Y_test,predictions)


# In[29]:


from sklearn.metrics import accuracy_score


# In[31]:


accuracy_score(Y_test,predictions)


# In[32]:


import pickle
assists=pickle.dumps(model_assists)


# In[ ]:





# In[ ]:





# In[ ]:




