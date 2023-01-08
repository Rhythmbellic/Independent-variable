#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer
#Initiallising
data=pd.read_csv('Raw_Housing_Prices3.csv')
data.head(10)
#for independent variable we can deal missing values by imputing
#we can impute as following
#for continous data by mean or median
# for onject data by mode
#first we will make a list of all continous columns
numerical_column=['No of Bedrooms','No of Bathrooms','Flat Area (in Sqft)','Lot Area (in Sqft)',
                  'Area of the House from Basement (in Sqft)','Latitude','Longitude',
                  'Living Area after Renovation (in Sqft)']
imputer=SimpleImputer(missing_values=np.nan,strategy='median')
data[numerical_column]=imputer.fit_transform(data[numerical_column])
#we have done numerical now we will do catagarical imputation
column= data['Zipcode'].values.reshape(-1,1)
imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
data['Zipcode']=imputer.fit_transform(data['Zipcode'])
data.info()
#we will see data tranformation in next repo
