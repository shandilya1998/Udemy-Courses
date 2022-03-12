import numpy as np

# Methods of creating NumPy Array

# List to NumPy Array
mylist = [1, 2, 3]
array_1 = np.array(mylist)

## Getting a range of numbers
## Default output type of np.arange is int, not float
array_2 = np.arange(start = 0, stop = 10, step = 2, dtype = np.float32)

## Array filled with zeros
## Default output type of almost all NumPy operations is float
array_3 = np.zeros(shape = (10, 5), dtype = np.float32)

## Array filled with ones
array_4 = np.ones(shape = (10, 5), dtype = np.float32)

### Set Random Seed
np.random.seed(101)

## Array filled with random integers
array_5 = np.random.randint(low = 0, high = 10, size = 5)

# Operations
maximum = array_1.max()
argmax = array_1.argmax()
minimum = array_1.min()
argmin = array_1.argmin()
mean = array_1.mean()
array_4.reshape((2, 25))

# Indexing
mat = np.arange(0, 100).reshape((10, 10))

## Extract Single Element
row = 0
col = 0
item = mat[row, col]
item = mat[row][col]

## Slicing
### All items in a row
row = mat[0, :]

### All items in a column
col = mat[:, 0]

### All items in a chunk
chunk = mat[0: 3, 0: 4]

# Copy Array
mynetarray = array_4.copy()

