import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}


def get_img_url():
    start_url = "https://www.douyu.com/g_yz"
    response = requests.get(start_url, headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    yz_list = soup.select('div[class="DyImg avatar"]')
    for yz in yz_list:
        y_list = yz.select('li')
        for li in y_list:
            yield li.img['src']


if __name__ == '__main__':
    img_url = get_img_url()
    for num, img in enumerate(img_url):
        img_response = requests.get(img)
        # print(img_response)
        img = img_response.content
        # img_path = './pic/%s.png' % num
        # with open(img_path, "wb") as file:
        #     file.write(img)
