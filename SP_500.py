# In this exercise, you will learn to read a csv file which contains the S&P 500 price data and store it in a dataframe which will be used for our analysis later. 

# Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# Read the data from CSV file
# Type your code below 
Df = pd.read_csv('../data/SPY.csv', index_col=0)
print(Df.head())
