import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import seaborn as sns

california_housing = fetch_california_housing()

boston_df = pd.DataFrame(california_housing.data,
                         columns=california_housing.feature_names)
boston_df['PRICE'] = california_housing.target

Y = boston_df['PRICE']
X = boston_df.drop(['PRICE'], axis=1, inplace=False)

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.3, random_state=156)

lr = LinearRegression()

lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)

mse = mean_squared_error(Y_test, Y_predict)
rmse = np.sqrt(mse)

print('MSE : {0:.3f}, RMSE : {1:.3f}'.format(mse, rmse))
print('R^2(Variance score) : {0:.3f}'.format(r2_score(Y_test, Y_predict)))

print('Y 절편 값: ', lr.intercept_)
print('회귀 계수 값: ', np.round(lr.coef_, 1))

coef = pd.Series(data=np.round(lr.coef_, 2), index=X.columns)
coef.sort_values(ascending=False)

fig, axs = plt.subplots(figsize=(16, 16), ncols=3, nrows=5)

x_features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
              'Latitude', 'Longitude']

for i, feature in enumerate(x_features):
    row = int(i/3)
    col = i % 3
    sns.regplot(x=feature, y='PRICE', data=boston_df, ax=axs[row][col])

plt.show()
