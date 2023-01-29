# Python Pandas

Pandas is a Python library used for working with data sets.

## **_INDEX_**
- [Pandas Intro](##What-is-Pandas?)
- [Pandas Getting Started](##Installing-Pandas)
- [Pandas Serieds](#Pandas-Series)
- [Pandas DataFrames](#Pandas-DataFrames)
- [Reading data from a CSV File](#Reading-data-from-a-CSV-File)
- [Reading data from a JSON File](#Reading-data-from-a-JSON-File)
- [Analyzing Data](#Analyzing-Dataframes)

## What is Pandas?
Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

## What can Pandas do ?

Pandas gives you answers about the data. Like:

- Is there a correlation between two or more columns?
- What is average value?
- Max value?
- Min value?

Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

## Installing Pandas

> `pip install pandas` (For Windows)

> `pip3 install pandas` (For Linux)

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

> Now for acessing the elements in `myvar`, you can use custom index<br>`print(myvar["x"])`

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

`pandas.DataFrame()` is a constructor function in the pandas library for creating a DataFrame, which is a 2-dimensional labeled data structure with columns of potentially different types. It can be thought of as a table in a relational database or an Excel spreadsheet, with rows and columns. The DataFrame can be created from various input data such as NumPy ndarrays, lists, or even from a CSV file. The DataFrame is a powerful tool for data manipulation and analysis in Python.

### Example

```py
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
```

### **Output**

```
     calories  duration
  0       420        50
  1       380        40
  2       390        45
```

## Locating a particular row in a DataFrame

As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the `loc` attribute to return one or more specified row(s)

```py
print(df.loc[1])
```

### **Output**

```
  calories    420
  duration     50
  Name: 0, dtype: int64
```

## Named Indexes in DataFrame

With the `index` argument, you can name your own indexes.

### Example

```py
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
```

### **Output**

```
        calories  duration
  day1       420        50
  day2       380        40
  day3       390        45
```

<br>

### **Selecting some rows from the DataFrame**

```py
print(df.loc[["day2", "day3"]])
```

# Reading data from a CSV File

A simple way to store big data sets is to use CSV files (comma separated files).

CSV files contains plain text and is a well know format that can be read by everyone including Pandas.

In our examples we will be using a CSV file called 'data.csv'.

### **Example**

```py
import pandas as pd

df = pd.read_csv('data.csv')

print(df)
```

**_Note:_ If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows**

## `to_string()` method

**Tip:** use `to_string()` to print the entire DataFrame.

### **Example**

```py
import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())
```

## max_rows

The number of rows returned is defined in Pandas option settings.

You can check your system's maximum rows with the `pd.options.display.max_rows` statement.

**Meaning of `max_rows`:** The value of max_rows differs from system to system. If the dataframe has less number of rows than the value of max_rows, then the entire dataframe will be displayed. If the dataframe has more number of rows than the value of max_rows, then only the first five and last five rows rows will be displayed.

### Changing the value of `max_rows`

```py
import pandas as pd
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
```

# Reading data from a JSON File

Big data sets are often stored, or extracted as JSON.

JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

In our examples we will be using a JSON file called `'data.json'`.

### **Example**

Loading the JSON file into a data frame

```py
import pandas as pd
df = pd.read_json('data.json')
print(df)
```

## `to_string()` method

**Tip:** use `to_string()` to print the entire DataFrame.

### **Example**

```py
import pandas as pd
df = pd.read_json('data.csv')
print(df.to_string())
```

## Disctionary as JSON

JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.

### **Example**

```py
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
}

df = pd.DataFrame(data)

print(df)
```

# Analyzing DataFrames

## Viewing the Data

One of the most used method for getting a quick overview of the DataFrame, is the `head()` method.

The `head()` method returns the headers and a specified number of rows, starting from the top.

### **Example**

```py
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head(10))
# Get a quick overview by printing the first 10 rows of the DataFrame:
```

**Note:** if the number of rows is not specified, the head() method will return the top 5 rows.

<br>
<hr>
<br>

There is also a `tail()` method for viewing the last rows of the DataFrame.

The `tail()` method returns the headers and a specified number of rows, starting from the bottom.

### **Example**

```py
import pandas as pd
df = pd.read_csv('data.csv')
print(df.tail())
# Get a quick overview by printing the last 5 rows of the DataFrame:
```

## Info about the data

The DataFrames object has a method called `info()`, that gives you more information about the data set.

### **Example**

```py
import pandas as pd
df = pd.read_csv('data.csv')
print(df.info())
```

### **Output**

```py
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 169 entries, 0 to 168
#There are 169 rows in the data set, and 4 columns.
Data columns (total 4 columns):
#The `info()` method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   Duration  169 non-null    int64
 1   Pulse     169 non-null    int64
 2   Maxpulse  169 non-null    int64
 3   Calories  164 non-null    float64
dtypes: float64(1), int64(3)
memory usage: 5.4 KB
None
```
