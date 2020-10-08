#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

dunk=pd.read_csv("fpl - Dunk.csv")


# In[2]:


X=dunk.iloc[:,[4,9,11,15,17]].values
Y=dunk["yellow_cards"]


# In[3]:


from sklearn.model_selection import train_test_split


# In[4]:


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42)


# In[7]:


from sklearn.linear_model import LogisticRegression
model_yellow=LogisticRegression()


# In[8]:


model_yellow.fit(X_train,Y_train)


# In[10]:


predictions=model_yellow.predict(X_test)


# In[11]:


from sklearn.metrics import classification_report
classification_report(Y_test,predictions)


# In[12]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,predictions)


# In[13]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_test,predictions)


# In[16]:


x=model_yellow.predict_proba(X_test)
print(x)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




