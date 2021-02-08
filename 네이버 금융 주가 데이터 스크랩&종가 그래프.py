from bs4 import BeautifulSoup
import pandas as pd
import requests
from matplotlib import pyplot as plt


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
df = df.dropna()

# 종가 차트 그리기
df = df.sort_values(by='날짜')

plt.rc('font', family='Malgun Gothic') # 한글 폰트
plt.rcParams['figure.figsize'] = (18, 10) #그래프 크기 설정
plt.title('Celltrion (종가 기준)')
plt.xticks(rotation=45)
plt.plot(df['날짜'], df['종가'], 'co-')
plt.grid(color='gray', linestyle='--')
plt.show()
