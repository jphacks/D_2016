import datetime
import jpholiday
import requests

import urllib3
from bs4 import BeautifulSoup



DATE = datetime.datetime.today().strftime("%Y%m%d") # 日付は８桁文字列の形式

# ーーーーーーーーーー平日/休日を判定ーーーーーーーーーー
# プログラムを実行した日が平日なら1、土日祝日なら0を返す
def isBizDay(DATE):
    Date = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))
    if Date.weekday() >= 5 or jpholiday.is_holiday(Date):
        return 0
    else:
        return 1

# 確認用
ResultDate = isBizDay(DATE)
print(ResultDate)

# ーーーーーーーーーー天気を判定ーーーーーーーーーー
#アクセスするURL
url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

#URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
http = urllib3.PoolManager()
instance = http.request('GET', url)
#instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(instance.data, 'html.parser')

#CSSセレクターで天気のテキストを取得します。
#今日の天気
tenki_today = soup.select_one('#main > div.forecastCity > table > tr > td > div > p.pict')
print ("今日の天気は"+tenki_today.text)

#明日の天気
tenki_tomorrow = soup.select_one('#main > div.forecastCity > table > tr > td + td > div > p.pict')
print ("明日の天気は"+tenki_tomorrow.text)

# #一瞬で画面が消えないよう入力されるまで待機
# input()

