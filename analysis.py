# Fisher Iris Data Set
# Author: Regina Fennessy

import numpy as np
import pandas as pd
import seaborn as sb

f = open('Fisher Iris Data Set.csv', 'r')
lines = f.readlines()

data = []
label = []

for line in lines[ 1: ]:
    line = line.replace('\n', '').split(',')
    
    # Convert string data into float form
    data.append( list(map(float, line[ :-1 ])) )
    label.append( line[-1] )
    
print(data)
print()
print(label)