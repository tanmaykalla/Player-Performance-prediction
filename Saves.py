#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

patricio=pd.read_csv("fpl - patricio.csv")


# In[3]:


X=patricio.iloc[:,[1,3,4,5,9]].values
Y=patricio["saves"]


# In[4]:


from sklearn.model_selection import train_test_split


# In[5]:


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42)


# In[7]:


from sklearn.linear_model import LogisticRegression
model_saves=LogisticRegression()


# In[8]:


model_saves.fit(X_train,Y_train)


# In[9]:


predictions=model_saves.predict(X_test)


# In[10]:


from sklearn.metrics import classification_report
classification_report(Y_test,predictions)


# In[11]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,predictions)


# In[12]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_test,predictions)


# In[13]:


x=model_saves.predict_proba(X_test)
print(x)


# In[ ]:





# In[ ]:




