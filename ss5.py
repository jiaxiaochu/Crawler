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
    datas = soup.find_all('article')  # , class_="material-card Pink"
    # print(soup.prettify())
    for data in datas:
        teacher_name = data.find('span').text
        recommend = data.find('strong').text.strip()
        introduction = data.find('div', class_="mc-description").text.replace(" ", "")  # .strip()
        # print(introduction)
        print(teacher_name, recommend, introduction)

else:
    print("{} 请求失败！".format(response.status_code))
