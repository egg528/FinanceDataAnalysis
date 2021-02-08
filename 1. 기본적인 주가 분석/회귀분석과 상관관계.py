from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()


#단순비교

nasDaq = pdr.get_data_yahoo('^IXIC', '2000-01-04')
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')

import matplotlib.pyplot as plt
plt.figure(figsize=(9,5))
plt.plot(nasDaq.index, nasDaq.Close, 'r--', label='NASDAQ')
plt.plot(kospi.index, kospi.Close, 'b', label='KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()


#지수화 비교 ( 특정 시점 종가 대비 오늘의 변동률)
N = (nasDaq.Close / nasDaq.Close.loc['2000-01-04']) * 100
K = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100

plt.figure(figsize=(9,5))
plt.plot(N.index, N, 'r--', label='NASDAQ')
plt.plot(K.index, K, 'b', label='KOSPI')
plt.grid(True)
plt.legend(loc='best')
plt.show()

#산점도 분석

# 데이터 개수 조정
import pandas as pd

df = pd.DataFrame({'NASDAQ':nasDaq['Close'], 'KOSPI': kospi['Close']})
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

plt .figure(figsize=(7,7))
plt.scatter(df['NASDAQ'], df['KOSPI'], marker='.')
plt.xlabel('NASDAQ Average')
plt.ylabel('KOSPI')
plt.show()


from scipy import stats
regr = stats.linregress(df['NASDAQ'], df['KOSPI'])
regr

#상관계수
df.corr()
df['NASDAQ'].corr(df['KOSPI'])

#결정계수
r_value = df['NASDAQ'].corr(df['KOSPI'])
r_squared = r_value**2

df = pd.DataFrame({'X':nasDaq['Close'], 'Y': kospi['Close']})
regr_line = f'Y = {regr.slope:.2f} * X + {regr.intercept:.2f}'

plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, '.')
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['NASDAQ * KOSPI', regr_line])
plt.title(f'NASDAQ x KOSPI (R = {regr.rvalue:.2f}')
plt.xlabel('NASDAQ')
plt.ylabel('KOSPI')
plt.show()

