'''
-panda refers to -'panel data' or 'python data analysis'
-used for working with datasets
-it has functions for analysing, cleaning, exploring and manipulating data
-read and write data structures and diff formats-csv,text,xml,json,zip,etc

three data structures-
1. series:one dimensional labeled arrays pd.series(data)
2. dataframes: two dimensional data structure with columns,much like a table
3. panel:a panel is a 3D container of data

importance of pandas in python
1. allows us to analise big data and make conclusions based on statistical theories
2. can clean messy datasets and make them readable and relevent
3. easy handling of missing data(represented as NaN) in floating point as well as non floating point data
4. size mutability: columns can be inserted and deleted from dataframe and higher dimensional objects
5. dataset merging and joining flexible reshaping and pivoting of datasets proves time series functionality

'''
'''
1. Series-1D array that is capable of storing various datatypes

-import pandas as pd
 a=pd.series()
 print(a)

'''
import pandas as pd
x = [3, 4, 5, 6]
var = pd.Series(x)  # example for series
print(var)
print(type(var))  # finding type of var
print(var[3])  # values by index
# to change index,datatype,name
var1 = pd.Series(x, index=['a', 'b', 'c', 'd'], dtype='float', name='python')
print(var1)

# we can pass dictionary also
dic = {'name': ['python', 'c', 'c++', 'java'],
       'por': [12, 13, 14, 15],
       'rank': [1, 4, 3, 2]}
var2 = pd.Series(dic)
print(var2)

# to create series of same data
var3 = pd.Series(12, index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(var3)

'if u add 2 series of diff length then,for remaining data it will give NaN-not a number,wont give any error'
var4 = pd.Series(12, index=[0, 1, 2, 3, 4])
print(var3+var4)  # adding 2 series

'2. Dataframe'
y = [1, 2, 3, 4, 5, 6]
var5 = pd.DataFrame(y)  # example for dataframe
print(var5)
print(type(var5))

# all arrays must be of same length
dic1 = {"a": [1, 2, 3, 4, 5], "b": [1, 2, 3, 4, 5]}
var6 = pd.DataFrame(dic1)  # passing dictionary in dataframe
print(var6)
