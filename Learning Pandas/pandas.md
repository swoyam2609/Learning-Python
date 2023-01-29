# Python Pandas
Pandas is a Python library used for working with data sets.
## What can Pandas do ?
Pandas gives you answers about the data. Like:

- Is there a correlation between two or more columns?
- What is average value?
- Max value?
- Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

## Installing Pandas
> ```pip install pandas``` (For Windows)

> ```pip3 install pandas``` (For Linux)

## Importing Pandas
```py
import pandas as pd
```

# Pandas Series
`pandas.Series()` is a constructor function in the pandas library for creating a Series, which is a one-dimensional labeled array capable of holding any data type. It can be thought of as a single column of a DataFrame, with a label (index) for each row. The Series can be created from various input data such as NumPy ndarrays, lists, or even from a scalar value. The Series is a powerful tool for data manipulation and analysis in Python and it also used for one-dimensional data analysis.
### Example
```py
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
```
## Labels
If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.
### Example
```py
print(myvar[0])
```
## Create Labels
With the `index` argument, you can name your own labels.
### Example
```py
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
```
>Now for acessing the elements in `myvar`, you can use custom index<br>```print(myvar["x"])```

## Passing Dictionaries (Key-Value pairs) to the series( ) function
```py
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
```
In this case, the keys of the dictionary become the labels for the series
### **Selecting some key-value pairs from the dictionary**
```py
import pandas as pd
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)
```
This will create a pandas series with only two indexes ('day1' and 'day2')

# Pandas DataFrames