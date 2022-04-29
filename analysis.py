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

#This helps you ensure that your code takes all the data into consideration by showing you many columns and rows are there.
print(data.shape)
data.describe()

#This creates a txt file that contais a summary of the dataset.
with open("Summary.txt","a") as f:
      print((data.describe()),file = f)




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


#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "sepal_length", "sepal_width" ) \
.add_legend()  
plt.title("Scatter Plot Sepal")  
plt.show()   

#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "petal_length", "petal_width" ) \
.add_legend()  
plt.title("Scatter Plot Petal")  
plt.show() 

#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "petal_length", "sepal_length" ) \
.add_legend()  
plt.title("Scatter length")  
plt.show() 

#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "petal_width", "sepal_width" ) \
.add_legend()  
plt.title("Scatter Plot Width")  
plt.show() 