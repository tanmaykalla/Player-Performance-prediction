#!/usr/bin/env python
# coding: utf-8

# In[50]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

vvd=pd.read_csv("fpl - VVD.csv")


# In[51]:


X=vvd.iloc[:,[1,7,9,15]].values
Y=vvd["clean_sheets"]


# In[52]:


from sklearn.model_selection import train_test_split


# In[53]:


X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=42)


# In[54]:


from sklearn.linear_model import LogisticRegression


# In[55]:


model_clean_sheets=LogisticRegression()


# In[56]:


model_clean_sheets.fit(X_train,Y_train)


# In[57]:


predictions=model_clean_sheets.predict(X_test)


# In[58]:


from sklearn.metrics import classification_report
classification_report(Y_test,predictions)


# In[59]:


from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,predictions)


# In[60]:


from sklearn.metrics import accuracy_score
accuracy_score(Y_test,predictions)


# In[61]:


x=model_clean_sheets.predict_proba(X_test)
print(x)


# In[ ]:





# In[ ]:





# In[ ]:




