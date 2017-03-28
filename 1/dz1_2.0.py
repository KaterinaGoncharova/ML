
# coding: utf-8

# In[56]:




import numpy as np
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import classification_report, f1_score
from IPython.display import Image
get_ipython().magic(u'matplotlib inline')

titanic=pandas.read_csv('titanic.csv')

titanic.describe()

df = titanic[['Survived' , 'Pclass', 'Sex']]

N=3 #мест для групп

m=df[df['Sex']=='male']
m1=m[m['Pclass']==1]#мужчин 1 класса
m2=m[m['Pclass']==2]#мужчин 2 класса
m3=m[m['Pclass']==3]#мужчин 3 класса
m1surv=m1[m1['Survived']==1]# муж. 1 класса выжило
m2surv=m2[m2['Survived']==1]#муж. 2 класса выжило
m3surv=m3[m3['Survived']==1]#муж. 3 класса выжило

w = df[df['Sex']=='female']
w1 = w[w['Pclass']==1]#женщин 1 класса
w2 = w[w['Pclass']==2]#женщин 2 класса
w3 = w[w['Pclass']==3]#женщин 3 класса
w1surv = w1[w1['Survived']==1]#жен.1 класса выжило
w2surv = w2[w2['Survived']==1]#жен. 2 класса выжило
w3surv = w3[w3['Survived']==1]#жен. 3 класса выжило
len(m1),  len(m2), len(m3), len(w1),  len(w2), len(w3),'&', len(m1surv), len(m2surv),len(m3surv), len(w1surv),len(w2surv),len(w3surv)


# In[57]:

from __future__ import division
m1_success=(45/122)#вероятность выживания муж. из 1 класса
m2_success=(17/108)#вероятность выживания муж. из 2 класса
m3_success=(47/347)#вероятность выживания муж. из 3 класса
m_success=(m1_success, m2_success, m3_success)#общее из предыдущего

w1_success=(91/94)#вероятность выживания жен. из 1 класса
w2_success=(70/76)#вероятность выживания жен. из 2 класса
w3_success=(72/144)#вероятность выживания жен. из 3 класса
w_success=(w1_success, w2_success, w3_success)#общее из предыдущего
#знаю,что очень криво так считать, но по-другому Питон не спаравлялся почему-то.

ind = np.arange(N)
width = 0.35 #ширина полос

fig, ax = plt.subplots()
rects1 = ax.bar(ind, m_success, width, color='#B2182B')
rects2 = ax.bar(ind + width, w_success, width, color='#2166AC')

ax.set_ylabel('The probability of survival')
ax.set_title('The probability of survival depending on social status and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('First class', 'Second class', 'Third class'))

ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
plt.show()

#Список вероятности выживания от самой высокой до самой низкой:
#women 1 class
#women 2 class
#women 3 class
#men 1 class
#men 2 class
#men 3 class

