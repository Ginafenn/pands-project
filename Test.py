

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#Read the csv data set
data = pd.read_csv('Fisher Iris Data Set.csv')
data.head()


Name = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species']
print(data.shape)
data.describe()

with open("dataset.txt","a") as f:
      print((data.describe()),file = f)

# Scatterplot PETAL (seaborn)
#plt.figure()
#sns.scatterplot(x="pl", y="pw")
#plt.title("Petal")


#Create histogram for Sepal Width using black edging/creating a title/and labels for x and y axis
plt.hist(x='sepal_width', edgecolor='black' )
plt.title('Histogram - Sepal Width')
plt.ylabel('Count')
plt.xlabel('Sepal Width')
plt.show()

#Create histogram for Petal Length using black edging/creating a title/and labels for x and y axis
plt.hist(x='petal_length', edgecolor='black' )
plt.title('Histogram - Petal Length')
plt.ylabel('Count')
plt.xlabel('Petal Length')
plt.show()

#Create histogram for Petal Width using black edging/creating a title/and labels for x and y axis
plt.hist(x='petal_width', edgecolor='black' )
plt.title('Histogram - Petal Width')
plt.ylabel('Count')
plt.xlabel('Petal Width')
plt.show()

