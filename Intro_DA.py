import pandas as pd

# Data importing 
data = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv")

# Get first 5 values of data set
# print(data.head(5))

# get data at specific index here will show data at index 0 of column and 0th in row
# print(data.iloc[0,0])

# checking about data set information
# print(data.info())

# Checking if null values existing or not
# print(data.dropna(inplace=True))

# checking dataset content
# print(data.describe())

#             Index   Height(Inches)"   "Weight(Pounds)"
# count  200.000000        200.000000         200.000000
# mean   100.500000         67.949800         127.221950
# std     57.879185          1.940363          11.960959
# min      1.000000         63.430000          97.900000
# 25%     50.750000         66.522500         119.895000
# 50%    100.500000         67.935000         127.875000
# 75%    150.250000         69.202500         136.097500
# max    200.000000         73.900000         158.960000

#checking null values
# print(data.isnull().sum())

#changing column data type 
# data['Index'] = data['Index'].astype(int)

# checking correlations
# print(data.corr())

data.columns = data.columns.str.strip().str.replace('"', '').str.replace("'", "") # Remove extra spaces and quotes
print(data.columns)  # Check updated column names


# plotting of data
# import matplotlib.pyplot as plt
# data.plot(kind='scatter', x="Height(Inches)", y="Weight(Pounds)")
# plt.show() 


