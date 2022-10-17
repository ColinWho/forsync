# The array to store the data
import numpy as np
import pandas as pd

with open('data.txt') as f:
    data = []
    lines = f.readlines()
    for i in lines:
        data.append(i.strip())

data1 = []
for i in data:
    for j in i:
        data1.append(int(j))

data = np.array(data1).reshape(1000)

def mul(x):
    res = 1
    for i in x:
        res *= i
    return res

data = pd.DataFrame(data)
data['mul'] = data.rolling(13).agg(mul)
data[data['mul']==data['mul'].max()]
largest = list(data.iloc[210-13:210][0])

print( f'largest 13 adjacent numbers: {largest}' )