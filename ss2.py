import requests, json
from bs4 import BeautifulSoup

# https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid=102890163566176729&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=1&n=5&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0
for i in range(0, 10):
    dict = {
        'aggr': 0,
        'catZhida': 1,
        'ct': 24,
        'format': 'json',
        'g_tk': 5381,
        'g_tk_new_20200303': 5381,
        'hostUin': 0,
        'inCharset': 'utf8',
        'loginUin': 0,
        'lossless': 0,
        'n': 5,
        'needNewCode': 0,
        'notice': 0,
        'outCharset': 'utf-8',
        'p': i,
        'platform': 'yqq.json',
        'qqmusic_ver': 1298,
        'remoteplace': 'txt.yqq.lyric',
        'searchid': 102890163566176729,
        'sem': 1,
        't': 7,
        'w': '%E4%BA%94%E6%9C%88%E5%A4%A9'
    }
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&remoteplace=txt.yqq.lyric&searchid=102890163566176729&aggr=0&catZhida=1&lossless=0&sem=1&t=7&p=1&n=5&w=%E4%BA%94%E6%9C%88%E5%A4%A9&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
    data = requests.get(url=url, headers=headers, params=dict)
    # data.encoding = data.apparent_encoding
    json_data = data.json()
    song = json_data['data']['lyric']['list']
    for i in song:
        b = i['content'].replace('\\n', '\n') + '\n'
        print(b)
