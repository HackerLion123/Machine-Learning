import pandas as pa
import quandl
import math

#Linear Regression
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#Stock Exchange data analysis
df = quandl.get("WIKI/GOOG")
print (df.head())
