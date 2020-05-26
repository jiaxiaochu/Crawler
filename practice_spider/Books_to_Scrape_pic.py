import requests, re, time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
response = requests.get("http://books.toscrape.com/")
content = response.text

reg = r'src="(.+?\.jpg)"'
img_pic = re.compile(reg)
pic_url_list = re.findall(img_pic, content)
for pic_url in pic_url_list:
    # print(pic_url,type(pic_url))
    # url = "https//:" + pic_url
    pic = requests.get(pic_url)
    data = pic.content
    pic_name = '%f.jpg' % time.time()
    with open('.image/book_scrape' + pic_name, 'wb') as file:
        file.write(data)
