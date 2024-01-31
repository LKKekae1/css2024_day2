# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 08:25:06 2024

@author: KEKAELK1
"""

import pandas as pd

file  = pd.read_csv("data_02/iris.csv")

"""
Absolute Path: Gives a full location of the file
    
 C:/Users/kekaelk1/css2024_day2/data_02/iris.csv

Relative Path: Gives you the location you currently are
    
data_02/iris.csv
"""

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = "https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv"

file = pd.read_csv(url)    
    
column_names = ['sepal_length', 'sepal_width','petal_length','petal_width','class']

file = pd.read_csv(url, header=None, names = column_names)
    
file = pd.read_csv("data_02/Geospatial Data.txt", sep=";")

file = pd.read_excel("data_02/residentdoctors.xlsx")

file = pd.read_json("data_02/student_data.json")

print(file)

"""

url = 

"""

# url = 

# df = dataframe

# df = pd.read_csv(url)

# print(df.info())
# print(df.describe())

"""
Transformation
"""

df = pd.read_csv("data_02/country_data_index.csv", index_col=0)

file = pd.read_excel("data_02/residentdoctors.xlsx")

print(df.info())

# df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')
# df["UPPER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

print(df.info())

# df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

print(df.info())


"""
working with dates: most case we read dates as a string
30-01-2024 UK
01-30-2024 US
"""
df = pd.read_csv("data_02/time_series_data.csv",index_col=0)

print(df.info())

# df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

print(df.info())

df['Year'] = df['Date'].dt.year

"""
.str
.extract
.astype
"""

df = pd.read_csv("data_02/patient_data_dates.csv")

df = pd.read_csv("data_02/patient_data_dates.csv",index_col=0)

df["Date"] = pd.to_datetime(df["Date"],format="mixed")

df.drop(index=26, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

print(df.info())

avg_cal = df["Calories"].mean()

# df["Calories"].fillna(avg_cal,inplace = True)

"""
best practices
"""

"""
droping "Nan"
when you use drop command, it removes the whole row including the index,how to fix the index?
"""

df.dropna(inplace = True)


df = df.reset_index(drop=True)

# df.loc[7, 'Duration'] = 45
df['Duration']= df['Duration'].replace([450, 50])

print(df)

# pd.set_option('display.max_rows',None)

"""
going back to iris data
"""

df = pd.read_csv("data_02/iris.csv")

# print(df.columns)

col_names = df.columns.tolist()

print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)

"""
grouping by different catergories
"""

grouped = df.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()

print(mean_square_values)


"""
append & merge
"""

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

df = pd.concat([df1,df2], ignore_index=True)

"""
working with files with different column names
"""

df1 = pd.read_csv("data_02/person_education.csv")
df2 = pd.read_csv("data_02/person_work.csv")

# inner join

df_merge_inner = pd.merge(df1,df2,on="id")

#################

df = pd.read_csv("data_02/iris.csv")

print(df)

df["class"] = df["class"].str.replace("Iris-","")

# sepal length bigger than 5

df = df[df['sepal_length']>5]

df = df[df["class"]=="virginica"]

"""
filtering
"""

df.to_csv("pulsar.csv")

# df.to_csv("pulsar")



