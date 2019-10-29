"""
utility functions for working with DataFrames
"""
import pandas
TEST_DF = pandas.DataFrame([1,3,4,5,6])
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

iris = pandas.read_csv(url, header=None)
