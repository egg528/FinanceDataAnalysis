import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

samsung = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
apple = pdr.get_data_yahoo('AAPL', start='2018-05-04')



#종가 단순 비교
plt.plot(samsung.index, samsung.Close, 'b', label="Samsung Electronics")
plt.plot(apple.index, apple.Close, 'r--', label="Apple")
plt.legend(loc="best")
plt.show()


# 일간 변동률(Daily Percent Change) DF 만들기
samsung_dpc = pd.DataFrame(columns = ['dpc'], index = samsung.index)
samsung_dpc['dpc'] = (samsung['Close'] / samsung['Close'].shift(1)-1)*100
samsung_dpc.iloc[0] = 0

apple_dpc = pd.DataFrame(columns = ['dpc'], index = apple.index)
apple_dpc['dpc'] = (apple['Close'] / apple['Close'].shift(1)-1)*100
apple_dpc.iloc[0] = 0


#일간 변동률 비교
plt.plot(samsung_dpc.index, samsung_dpc.dpc, 'b', label="Samsung Electronics")
plt.plot(apple_dpc.index, apple_dpc.dpc, 'r--', label="Apple")
plt.legend(loc="best")
plt.show()


# 일간 변동률 히스토그램
samsung_dcp = (samsung['Close']-samsung['Close'].shift(1)) / samsung['Close'].shift(1) * 100
samsung_dcp.iloc[0] = 0
plt.hist(samsung_dpc, bins=18)
plt.grid(True)
plt.show()


apple_dcp = (apple['Close']-apple['Close'].shift(1)) / apple['Close'].shift(1) * 100
apple_dcp.iloc[0] = 0
plt.hist(apple_dcp, bins=18)
plt.grid(True)
plt.show()

# 일간 변동률 누적합
samsung_dcp_cs = samsung_dcp.cumsum()
apple_dcp_cs = apple_dcp.cumsum()

plt.plot(samsung.index, samsung_dcp_cs, 'b', label='Samsung Electronics')
plt.plot(apple.index, apple_dcp_cs, 'r--', label='Apple')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')
plt.show()
