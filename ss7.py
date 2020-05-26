import requests
from bs4 import BeautifulSoup

start_url = "http://show.ybccode.com/teachers/teachers.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding  # 将获取到的响应信息编码设置为网址的编码
if response.status_code == 200:
    print("{} 请求成功！".format(response.status_code))
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    datas = soup.find_all('article', class_="material-card Pink")
    # print(soup.prettify())
    print("#"*20)
    print(soup.title)
    print(soup.h2)
    print(type(soup.h2.attrs))
    print(soup.h2.attrs['class'])
    # print(soup.div.name)

