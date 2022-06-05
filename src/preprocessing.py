import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

base_path = 'C:/Users/592k/Documents/dev/Seoul_Bike/data/'
train = pd.read_csv(base_path+'/train.csv', encoding='cp949')
test = pd.read_csv(base_path+'/test.csv', encoding='cp949')
submission = pd.read_csv(base_path+'/submission.csv', encoding='cp949')

train.info()
train.corr()