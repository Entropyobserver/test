"""

    Open the .csv-file in your favorite editor. Look at the data.
    What are they? Integers? Booleans? Confer this file:

data_types_statistics.txt 

    to get a hunch of what you are dealing with. Discuss with a
    classmate or two.

    Write a program that reads the file as a pandas dataframe.

"""
import pandas as pd
#path = '/home/yaxi4987/exercises6/Ecommerce Dataset.csv'
path = 'Ecommerce Dataset.csv'
data = pd.read_csv(path)
print(data.head())