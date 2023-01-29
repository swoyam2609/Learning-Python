import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

# pandas.DataFrame() is a constructor function in the pandas library for creating a DataFrame, which is a 2-dimensional labeled data structure with columns of potentially different types. It can be thought of as a table in a relational database or an Excel spreadsheet, with rows and columns. The DataFrame can be created from various input data such as NumPy ndarrays, lists, or even from a CSV file. The DataFrame is a powerful tool for data manipulation and analysis in Python.

print(myvar)