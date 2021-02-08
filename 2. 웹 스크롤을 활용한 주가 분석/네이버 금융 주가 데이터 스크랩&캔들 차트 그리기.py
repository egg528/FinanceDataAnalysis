from bs4 import BeautifulSoup
import pandas as pd
import requests
import mplfinance as mpf

# 가장 오래된 시세 페이지 찾기
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
html = BeautifulSoup(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, 'lxml')
pgrr = html.find('td', class_='pgRR')
s = str(pgrr.a['href']).split('=')
last_page = s[-1]



# 네이버 금융 모든 시세 데이터 가져오기(지정 종목)
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

for page in range(1, 5):
    page_url = '{}&page={}'.format(sise_url, page)
    df = df.append(pd.read_html(requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text)[0])
    print(page)

#차트 출력을 위한 DF 가공
df = df.dropna()
df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'})
df = df.sort_values(by='Date')
df.index = pd.to_datetime(df.Date)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

#한국 캔들 차트 출력
kwargs = dict(title='Celltrion candle chart', type='candle', mav=(2,4,6), volume=True, ylabel='ohlc candles')
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df, **kwargs, style=s)

#github.com/matplotlib/mplfinance


#