
# coding: utf-8

# In[31]:

import matplotlib.pyplot as plt
from pandas import date_range,Series,DataFrame,read_csv, qcut
from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
from numpy.random import randn
from pylab import *
from matplotlib import rcParams
import brewer2mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



titanic = read_csv('titanic.csv')


# In[32]:

#useful_columns = ['Fare', 'Pclass']
#titanic[useful_columns].head()


# In[30]:

sns.countplot(x='Pclass', hue='Fare', data=titanic);
plt.show()


# In[ ]:

#Самый дешевый 3 класс, дороже 2 класс, самый дорогой 1 класс. Больше всего билетов было куплено в 3 класс, меньше во второй и еще меньше в 1 класс.

