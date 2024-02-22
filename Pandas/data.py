import pandas as pd

df = pd.read_csv('C:/Users/ITC-LAB-T/Desktop/OOP-Python/Pandas/data.csv')

# print(df) 

print(df.to_string()) 

#print(pd.options.display.max_rows) 

pd.options.display.max_rows = 9999

#pd.options.display.max_rows = 10