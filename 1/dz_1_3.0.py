
# coding: utf-8

# In[19]:

import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import classification_report, f1_score
from IPython.display import Image
get_ipython().magic(u'matplotlib inline')

titanic=pandas.read_csv('titanic.csv.csv')

titanic.head(10)


# In[30]:

titanic['Family'] = titanic["Parch"] + titanic["SibSp"] #кол-во членов семьи


# In[31]:

titanic.head(10)


# In[37]:

bro = titanic[titanic['Parch']==2]
bro_surv= bro[bro['Survived']==1]


# In[39]:

bro_surv= bro[bro['Survived']==0]
bro_surv
#действитель, у родителей с 2 детьми, шанс выхить был гораздо больше


# In[ ]:



