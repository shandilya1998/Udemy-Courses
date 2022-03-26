import numpy as np
import sklearn
import pandas as pd

df = pd.read_csv('data/boston_housing/housing.data', delim_whitespace=True, header = None)
col_name = ['CRIM', 'ZN' , 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.columns = col_name
print(df.head())


