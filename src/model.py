import numpy as np
import pandas as pd

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

clf_d = DecisionTreeRegressor()
clf_d.fit(X_train, y_train)
mean_absolute_error(y_val, clf_d.predict(X_val)), mean_squared_error(y_val, clf_d.predict(X_val))

predict = clf_d.predict(test)
submission['count'] = predict