# Fisher Iris Data Set
# Author: Regina Fennessy

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# Read the csv data set
data = pd.read_csv('Fisher Iris Data Set.csv')
data.head()

Name = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species']

plt.figure(figsize=(12,10))
plt.subplot(2,2,2)
sns.boxplot(x="species",y="sepal_length",data=data) 
plt.show()