import requests
from bs4 import BeautifulSoup

"""
http://show.ybccode.com/getcomment/?teacherName=%E6%9D%8E%E6%98%9F%E5%8E%9F&page=0
http://show.ybccode.com/getcomment/?teacherName=%E6%9D%8E%E6%98%9F%E5%8E%9F&page=1
http://show.ybccode.com/getcomment/?teacherName=%E6%9D%8E%E6%98%9F%E5%8E%9F&page=3
"""
start_url = "http://show.ybccode.com/getcomment/?teacherName=%E6%9D%8E%E6%98%9F%E5%8E%9F&page=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}
params = {
    "teacherName": "李星原",
    "page": "0"
}
response = requests.get(url=start_url, headers=headers)
response.encoding = response.apparent_encoding  # 将获取到的响应信息编码设置为网址的编码
if response.status_code == 200:
    print("{} 请求成功！".format(response.status_code))
    print(response.apparent_encoding)
    response.encoding = response.apparent_encoding
    # print(response.text)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # datas = soup.find_all('article')  # , class_="material-card Pink"
    # print(soup.prettify())
    # for data in datas:
    json_response = response.json()
    # print(json_response)
    datas = json_response['msg']
    for data in datas:
        comment_rate = data['comment_rate']
        name = data['name']
        tags = data['tags']
        comment_text = data['text']
        comment_time = data['time']
        print(comment_rate, name, tags, comment_text, comment_time)
else:
    print("{} 请求失败！".format(response.status_code))
