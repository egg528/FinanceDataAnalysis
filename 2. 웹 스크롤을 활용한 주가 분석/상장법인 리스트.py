import pandas as pd

krx_list = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')[0]
krx_list['종목코드'] = krx_list['종목코드'].map('{:06d}'.format)
krx_list = krx_list.sort_values(by='종목코드')
print(krx_list)