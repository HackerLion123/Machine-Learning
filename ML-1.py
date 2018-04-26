import pandas as pa
import quandl
import math
import numpy as np

#Linear Regression
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

#Stock Exchange data analysis
df = quandl.get("WIKI/GOOGL")
print (df.head())

#High - Low Percentage
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100
#Percentage Change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open']*100

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

#forecast variable to do any change later
forecast_col = 'Adj. Close'
#To replace all nand and null values by a value here -1
df.fillna(-1,inplace=True)

#0.01 forecast for tommorrow
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.head())

#Features
x = np.array(df.drop(['label'],1))
#labels
y = np.array(df['label'])






