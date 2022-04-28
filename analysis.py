# Fisher Iris Data Set
# Author: Regina Fennessy

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


#Read the csv data set
data = pd.read_csv('Fisher Iris Data Set.csv')
data.head()

# This is to identify headings of datasets
Name = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species']

#To prove how many columns and rows
print(data.shape)
data.describe()

#Create a text file that shows a summary of the dataset
with open("dataset.txt","a") as f:
      print((data.describe()),file = f)

#x = Name["sepal_length"]


#Create histogram for Sepal Length using black edging/creating a title/and labels for x and y axis
data.hist(column='sepal_length',edgecolor='black') 
plt.title('Sepal Length') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.savefig('Sepal_Length.png')
#plt.show()

#Create histogram for Sepal Width using black edging/creating a title/and labels for x and y axis
data.hist(column='sepal_width',edgecolor='black') 
plt.title('Sepal Width') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.savefig('Sepal_Width.png')

#Create histogram for Petal Length using black edging/creating a title/and labels for x and y axis
data.hist(column='petal_length',edgecolor='black') 
plt.title('Petal Length') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.savefig('Petal_Length.png')

#Create histogram for Petal Width using black edging/creating a title/and labels for x and y axis
data.hist(column='petal_width',edgecolor='black') 
plt.title('Petal Width') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.savefig('Petal_Width.png')


