#!/usr/bin/env python
# coding: utf-8

# In[91]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

vardy=pd.read_csv("fpl - Jamie Vardy.csv")
vardy.head(10)
print


# In[92]:


vardy["goals_scored"].plot.hist()



# In[59]:


sns.countplot(x="goals_scored",data=vardy)


# In[60]:


vardy.info()


# In[93]:


vardy.isnull()


# In[62]:


vardy.isnull().sum()


# In[104]:


X=vardy.iloc[[0-45],[1,4,12,15,18]].values
y=vardy["goals_scored"]
x1=vardy.iloc[[47],[1,4,12,15,18]].values


# In[107]:


from sklearn.model_selection import train_test_split


# In[108]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)


# In[ ]:





# In[98]:


from sklearn.linear_model import LogisticRegression


# In[101]:


model1=LogisticRegression(C=1e5,solver='lbfgs')


# In[100]:


model1.fit(X_train,y_train)


# In[69]:


predictions=model1.predict(X_test)


# In[70]:


from sklearn.metrics import classification_report


# In[71]:


classification_report(y_test,predictions)


# In[72]:


from sklearn.metrics import confusion_matrix


# In[73]:


confusion_matrix(y_test,predictions)


# In[ ]:





# In[74]:


from sklearn.metrics import accuracy_score


# In[75]:


accuracy_score(y_test,predictions)


# In[ ]:





# In[77]:





# In[78]:





# In[79]:





# In[80]:





# In[81]:


plt.plot(X_test,predictions)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[83]:


from scipy.special import expit
loss=expit(X_test*model1.coef_+model1.intercept_).ravel()


# In[82]:


plt.plot(X_test,loss)


# In[ ]:





# In[ ]:




