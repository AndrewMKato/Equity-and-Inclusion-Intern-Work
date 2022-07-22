from msilib.schema import File
import matplotlib.pyplot as plt
import pandas as pd, numpy as np
import csv

with open('chapter06data2021.csv', 'r') as file:
    rd = csv.reader(file)
    for row in rd:
        print(row)