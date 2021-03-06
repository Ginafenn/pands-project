# Fisher Iris Data Set
# Author: Regina Fennessy

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# Read the csv data set
data = pd.read_csv('Fisher Iris Data Set.csv')
data.head()

# This is to identify headings of datasets
Name = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'species']

# This helps you ensure that your code takes all the data into consideration by showing you many columns and rows are there.
print(data.shape)
data.describe()

# This creates a txt file that contais a summary of the dataset.
with open("Summary.txt","a") as f:
      print((data.describe()),file = f)


# Create histogram for Sepal Length using black edging/creating a title/and labels for x and y axis
# Displays chart 
# Saves to a png
data.hist(column='sepal_length',edgecolor='black') 
plt.title('Sepal Length') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.show()
# plt.savefig('Histogram Sepal_Length.png')

# Create histogram for Sepal Width using black edging/creating a title/and labels for x and y axis
# Displays chart 
# Saves to a png
data.hist(column='sepal_width',edgecolor='black') 
plt.title('Sepal Width') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.show()
#plt.savefig('Histogram Sepal_Width.png')

#Create histogram for Petal Length using black edging/creating a title/and labels for x and y axis
# Displays chart 
# Saves to a png
data.hist(column='petal_length',edgecolor='black') 
plt.title('Petal Length') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.show()
#plt.savefig('Histogram Petal_Length.png')

#Create histogram for Petal Width using black edging/creating a title/and labels for x and y axis
# Displays chart 
# Saves to a png
data.hist(column='petal_width',edgecolor='black') 
plt.title('Petal Width') 
plt.xlabel('Length (cm)') 
plt.ylabel('Quantity') 
plt.show()
#plt.savefig('Histogram Petal_Width.png')


#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
# Displays chart 
# Saves to a png
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "sepal_length", "sepal_width" ) \
.add_legend()  
plt.title("Scatter Plot Sepal")  
plt.show() 
#plt.savefig('Scatter Plot Sepal.png')  

#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
# Displays chart 
# Saves to a png
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "petal_length", "petal_width" ) \
.add_legend()  
plt.title("Scatter Plot ")  
plt.show() 
# plt.savefig('Scatter Plot Petal.png')  

#Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
# Displays chart 
# Saves to a png
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "petal_length", "sepal_length" ) \
.add_legend()  
plt.title("Scatter Plot length")  
plt.show()
# plt.savefig('Scatter Plot Length.png')   

# Creating a scatter Plot
# Using a white background/Grid
# Plots the lenght on x-axis and Width on Y-Axis
# Plot the variables length/width
# Adds a legend to show Species
# Adds a title to the chart 
# Displays chart 
sns.set_style("whitegrid") 
sns.FacetGrid(data, hue="species", height=6) \
.map(plt.scatter, "petal_width", "sepal_width" ) \
.add_legend()  
plt.title("Scatter Plot Width")  
plt.show() 
# plt.savefig('Scatter Plot Width.png') 

# Create a box Plot
# To create a variable that has more than one value
box_data = data
# Displys a white grid on the chart
sns.set_style("whitegrid")
# Plot the data using width of.4 and the marker size 5
sns.boxplot(data = box_data,width=0.4,fliersize=5)
# Display a title
plt.title("Box plot for all variables") 

# Saves to a png
# plt.savefig('Box Plot all Variables.png') 

# Displays chart 
plt.show() 

#Create box plot by Species by Variable
plt.figure(figsize=(12,10))
plt.subplot(2,2,2)
sns.boxplot(x="species",y="sepal_length",data=data) 
# Saves to a png
# plt.savefig('Box Plot Sepal Length.png') 
plt.show()


#Create box plot by Species by Variable
plt.figure(figsize=(12,10))
plt.subplot(2,2,2)
sns.boxplot(x="species",y="sepal_width",data=data) 
# Saves to a png
# plt.savefig('Box Plot Sepal Width.png') 
plt.show()

#Create box plot by Species by Variable
plt.figure(figsize=(12,10))
plt.subplot(2,2,2)
sns.boxplot(x="species",y="petal_width",data=data) 
# Saves to a png
# plt.savefig('Box Plot Pepal Width.png') 
plt.show()

#Create box plot by Species by Variable
plt.figure(figsize=(12,10))
plt.subplot(2,2,2)
sns.boxplot(x="species",y="petal_length",data=data) 
# Saves to a png
# plt.savefig('Box Plot Pepal Length.png') 
plt.show()