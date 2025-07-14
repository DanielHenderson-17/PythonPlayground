# myhelpers.py
from pandas import DataFrame as dataframe
from numpy import array as make_array

# Or wrap them directly
def create_dataframe(*args, **kwargs):
    return DataFrame(*args, **kwargs)

def create_array(*args, **kwargs):
    return array(*args, **kwargs)


from myhelpers import create_dataframe, create_array

df = create_dataframe(data)
arr = create_array([1, 2, 3])
