from datetime import date
from nsepy.history import get_price_list
from nsepy import get_history
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, neighbors

def find_trend(stock):
	his = hist(stock)
	his = his.reset_index()
	# ind = his.index
	# ind = ind[5:]
	gain = his['Gain']
	loss = his['Loss']
	rsi = []
	for i in range(len(his)):
		g = []
		l = []
		g = gain[-5:]
		l = loss[-5:]
		avg_gain = sum(g)/5.0
		avg_loss = sum(l)/5.0
		if avg_loss!=0:
			rs = avg_gain/avg_loss
		else:
			rs = 0.0
		r = 100 - (100/(1+rs))
		gain = gain[:-1]
		loss = loss[:-1]
		rsi.append(r)
	#print(rsi) #['Date', 'Symbol', 'Prev Close', 'Open', 'High', 'Low', 'Last', 'Close', 'Change', 'Gain', 'Loss']
	his['RSI'] = rsi[::-1]
	print(his)
	return

def gain_and_loss(data):
	gain = []
	loss = []
	for i in range(len(data)):
		if data['Change'][i] > 1:
			gain.append(data['Change'][i])
		else:
			gain.append(0)
	for i in range(len(data)):
		if data['Change'][i] < 1:
			loss.append(abs(data['Change'][i]))
		else:
			loss.append(0)
	return gain, loss

def hist(stock):
	s = get_history(symbol=stock, start=date(2018,12,1), end=date(2019,1,4))
	s.drop(['Series'], 1, inplace=True)
	s.drop(['VWAP'], 1, inplace=True)
	s.drop(['Volume'], 1, inplace=True)
	s.drop(['Turnover'], 1, inplace=True)
	s.drop(['Trades'], 1, inplace=True)
	s.drop(['Deliverable Volume'], 1, inplace=True)
	s.drop(['%Deliverble'], 1, inplace=True)
	s['Change'] = s['Close'] - s['Prev Close']
	s['Gain'], s['Loss'] = gain_and_loss(s)
	return s

def rsi_of_stock(stock):
	h = hist(stock)
	gain = h['Gain'][-5:]
	loss = h['Loss'][-5:]
	avg_gain = sum(gain)/5.0
	avg_loss = sum(loss)/5.0
	if avg_loss!=0:
		rs = avg_gain/avg_loss
	else:
		rs = 0.0
	rsi = 100 - (100/(1+rs))
	return rsi

def select_stock(data):
	for i in range(len(data)):
		try:
			if data['CLOSE'].loc[i] <= 50.0:
				data.drop(i, axis=0, inplace = True)
			elif data['CLOSE'].loc[i] >= 10000.0:
				data.drop(i, axis=0, inplace = True)
		except:
			continue
	return data

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = get_price_list(dt=date(2019,1,4))
data.drop(['SERIES'], 1, inplace=True)
data.drop(['LAST'], 1, inplace=True)
data.drop(['TOTTRDQTY'], 1, inplace=True)
data.drop(['TOTTRDVAL'], 1, inplace=True)
data.drop(['TIMESTAMP'], 1, inplace=True)
data.drop(['TOTALTRADES'], 1, inplace=True)
data.drop(['ISIN'], 1, inplace=True)

data = select_stock(data)
rsi = []
predicts = []
# for i in range(len(data)):
data = data[:15]
for i in range(15):
	try:
		rsi.append(rsi_of_stock(data['SYMBOL'][i]))
	except:
		rsi.append(0)
	print(i)
data = data.reset_index(drop=True)
data['RSI'] = rsi
for i in range(len(data)):
	if data['RSI'].loc[i] == 0.0:
		data.drop(i, axis=0, inplace = True)
data = data.reset_index(drop=True)
# for i in range(len(data)):
# 	predicts.append(find_trend(data['SYMBOL'][i]))
# data['TREND'] = predicts
t = find_trend(data['SYMBOL'][1])
#print(data)
# data.to_csv('Stock_data.csv', sep=',',index = False, encoding='utf-8')