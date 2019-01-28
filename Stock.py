import matplotlib.pyplot as plt
from matplotlib import style
import math
import numpy as np
from datetime import date
from nsepy.history import get_price_list
from nsepy import get_history
import pandas as pd
import datetime
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, neighbors

s = get_history(symbol='SBIN', start=date(2018,12,1), end=date(2019,1,4))
s.drop(['Series'], 1, inplace=True)
s.drop(['VWAP'], 1, inplace=True)
s.drop(['Volume'], 1, inplace=True)
s.drop(['Turnover'], 1, inplace=True)
s.drop(['Trades'], 1, inplace=True)
s.drop(['Deliverable Volume'], 1, inplace=True)
s.drop(['%Deliverble'], 1, inplace=True)
s.drop(['Symbol'], 1, inplace=True)
s['Change'] = s['Close'] - s['Prev Close']
RSI = []
gain = []
loss = []
avg_gain = []
avg_loss = []
for i in range(len(s)):
	if s['Change'][i] > 1:
		gain.append(s['Change'][i])
	else:
		gain.append(0)
for i in range(len(s)):
	if s['Change'][i] < 1:
		loss.append(abs(s['Change'][i]))
	else:
		loss.append(0)
s['Gain'] = gain
s['Loss'] = loss
rsi = []
for i in range(5, len(s)):
	avg_gain.append(sum(gain[i:-5])/5)
	#avg_loss.append(s[forecast_col_loss].shift(forecast_out))
print(avg_gain)
s.dropna(inplace=True)
#for i in range(len(s)):
	#rsi.append(100-(100/(1+(s['Avg Gain'][i]/s['Avg Loss'][i]))))
#s['RSI'] = rsi
# try:
# 	for i in range(len(s)):
# 		avg_gain.append((sum(s['Gain'][-5:])/5))
# 		avg_loss.append((sum(s['Loss'][-5:])/5))
# except:
# 	print()
# s['Avg Gain'] = avg_gain
# s['Avg Loss'] = avg_loss
print(s)
	#print(RSI)
# s['RSI'] = RSI

# forecast_col = 'RSI'
# forecast_out = int(math.ceil(0.01*len(s)))

# s['label'] = s[forecast_col].shift(-forecast_out)
# print(s)




# X = np.array(s.drop(['label'], 1))
# X = preprocessing.scale(X)
# X_lately = X[-forecast_out:]
# y = np.array(s['label'])

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1)

# clf = neighbors.KNeighborsClassifier()
# clf.fit(X_train, y_train)
# accuracy = clf.score(X_test, y_test)
# forecast_set = clf.predict(X_lately)
# print(forecast_set, accuracy, forecast_out)

# s['forecast'] = np.nan

# last_date = s.iloc[-1].name
# last_unix = last_date.timestamp()
# one_day = 86400
# next_unix = last_unix + one_day


# for i in forecast_set:
# 	next_date = datetime.datetime.fromtimestamp(next_unix)
# 	next_unix += one_day
# 	s.loc[next_date] = [np.nan for _ in range(len(s.columns)-1)] + [i]

# s['Adj. Close'].plot()
# s['forecast'].plot()
# plt.legend(loc = 2)
# plt.xlabel('')
# plt.ylabel('forecast')
# plt.show()




















# style.use('ggplot')
# s = pd.read_csv('Stock_data.csv')
# for i in range(len(s)):
# 	if s['RSI'].loc[i] == 0.0:
# 		s.drop(i, axis=0, inplace=True)
# for i in range(len(s)):
# 	try:
# 		if s['CLOSE'].loc[i] <= 50.0:
# 			s.drop(i, axis=0, inplace = True)
# 		elif s['CLOSE'].loc[i] >= 10000.0:
# 			s.drop(i, axis=0, inplace = True)
# 	except:
# 		continue
# # print(s)
# forecast = []
# s = s.reset_index(drop=True)
# for i in range(len(s)):
# 	if s['RSI'].loc[i] > 30.0 and s['RSI'].loc[i] <= 50.0:
# 		s.drop(i, axis=0, inplace = True)		
# 	elif s['RSI'].loc[i] >= 50.0 and s['RSI'].loc[i] < 80.0:
# 		s.drop(i, axis=0, inplace = True)
# s = s.reset_index(drop=True)
# for i in range(len(s)):
# 	if s['RSI'].loc[i] < 30.0:
# 		forecast.append(1)
# 	elif s['RSI'].loc[i] > 80.0:
# 		forecast.append(0)
# s['TREND'] = (forecast)
# #print(s)

# X = np.array(s.drop(['TREND', 'SYMBOL'],1))
# y = np.array(s['TREND'])

# X = preprocessing.scale(X)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1)

# clf = neighbors.KNeighborsClassifier()
# clf.fit(X_train, y_train)
# accuracy = clf.score(X_test, y_test)
# print(accuracy)

# plt.plot(s['SYMBOL'], s['TREND'])
# plt.legend(loc = 2)
# plt.xlabel('Stock_data')
# plt.ylabel('TREND')
# plt.show()