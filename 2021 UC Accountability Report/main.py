import csv
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import sklearn.linear_model

# with open('chapter06data2021.csv', 'r') as file:
#     rd = csv.reader(file)
#     for row in rd:
#         print(row)

df: pd.DataFrame = pd.read_csv('chapter06data2021.csv')

X = np.c_[df['_']]
y = np.c_[df['_']]

df.plot(kind='scatter', x='_', y='_')
plt.show()

model = sklearn.linear_model.LinearRegression()

model.fit(X, y)
