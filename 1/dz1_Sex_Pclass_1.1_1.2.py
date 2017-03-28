
# coding: utf-8

# In[38]:



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import date_range,Series,DataFrame,read_csv, qcut
from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
from numpy.random import randn
from pylab import *
from matplotlib import rcParams
import brewer2mpl

get_ipython().magic(u'matplotlib inline')

titanic = pd.read_csv('titanic.csv.csv')
#tclass = titanic.groupby(['Sex', 'Survived']).size().unstack()#-вероятность выжить для мужчин и женщин
tclass = titanic.groupby(['Pclass', 'Survived']).size().unstack()#-вероятность выжить для пассажиров разных социально-экономических классов (Pclass)
#print tclass

# In[40]:

titanic.describe()

# In[51]:

#tclass = titanic.groupby(['Sex', 'Survived']).size().unstack()#-вероятность выжить для мужчин и женщин
tclass = titanic.groupby(['Pclass', 'Survived']).size().unstack()#-вероятность выжить для пассажиров разных социально-экономических классов (Pclass)
print tclass



# In[56]:

dark2_colors = brewer2mpl.get_map('Dark2', 'Qualitative', 7).mpl_colors

plt.subplot(aspect=True)
plt.pie(t, labels=t.index.values, colors = dark2_colors[0:3], autopct='%i%%')
#plt.title("Sex")#-большим шансом на выживание обладала мужская половина. Муж-64%, Жен-35%
plt.title("Class")#-3 класс-55%, 2 класс 20%,1 класс 24%


plt.show()



