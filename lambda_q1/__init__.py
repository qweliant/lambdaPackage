"""
lambdata - a collection of data science helper functions
"""
import pandas as pd
import numpy as np

#sample code

#sample datasets
ONES = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))

#sample functions
def increment(x):
    return(x + 1)

def check_null(X):
    print("Null Matrix")
    print(X.isnull().values)
    
    
'''
requires dataframe as the first arg
requires one dimensional list as second arg
returns a new dataframe that is the concat of list->DataFrame and the DataFrame
'''
def make_concat( frame,one_d_list ):
    list_to_dataframe = pd.DataFrame( one_d_list )
    dfsr = pd.concat([frame, one_d_list], ignore_index=True, axis=1)
    return df
