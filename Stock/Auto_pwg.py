import datetime as dt
import pandas
import csv
from pandas import *
import time
import os
import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore")

def pwg():
    d = dt.datetime.now().strftime ("%d-%m")
    ex = 'pwg'+dt.datetime.now().strftime ("%d-%m")
    df = pandas.read_excel(ex+'.xls')
    df['OPHI'] = ((df['Open'] - df['High'])/df['High'])*100
    df['OPLO'] = ((df['Open'] - df['Low'])/df['Low'])*100
    df['CUOP'] = ((df['Current'] - df['Open'])/df['Open'])*100
    df['CULO'] = ((df['Current'] - df['Low'])/df['Low'])*100
    df['CUCL'] = ((df['Current'] - df['Close'])/df['Close'])*100
    df['CUHI'] = ((df['Current'] - df['High'])/df['High'])*100
    df.to_csv(ex+'_done.csv', sep=',',index = False, encoding='utf-8')
    return

