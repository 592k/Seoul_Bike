import numpy as np
import pandas as pd


base_path = '../data/'
train = pd.read_csv(base_path+'/train.csv', encoding='cp949')
test = pd.read_csv(base_path+'/test.csv', encoding='cp949')
submission = pd.read_csv(base_path+'/submission.csv', encoding='cp949')

# drop train.na
train = train.drop(train[train.hour_bef_temperature.isnull()==True].index)

# concat train & test
df = pd.concat([train.drop(columns=['count']), test])

# train.fillna
def fill_nan(dafa, col):
    dafa[col].fillna(df[col].median(), inplace=True)

# test.fillna
def test_fill(a):
    test.loc[653,a] = df[df.hour==19][a].median() 


col_list = ['hour_bef_pm2.5','hour_bef_pm10','hour_bef_ozone', 'hour_bef_windspeed']


for i in col_list:
    fill_nan(train, i)

for t in col_list[:-1]:
    fill_nan(test, t)

test_fill(['hour_bef_humidity','hour_bef_temperature','hour_bef_precipitation','hour_bef_windspeed','hour_bef_visibility'])

# id drop
train.drop(columns=['id'], inplace=True)
test.drop(columns=['id'], inplace=True)
