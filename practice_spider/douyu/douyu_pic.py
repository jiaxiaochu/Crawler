'''
练习：把网络上的图片保存到本地
思考：

以什么方式打开文件
保存什么格式的内容
'''

import requests, re, time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"
}
start_url = "https://www.douyu.com/g_yz"
response = requests.get(start_url, headers)
'''
访问response响应对象有三种方法：
            text  一般文本
            content   以字节的方式响应对象，遇到图片的时候，我们可以使用
            json  它是requests内置的json解码器，将json字符串解码成为字典
'''

response = response.text  # 通过text得到文本
# print(response)

reg = r'src="(.+?\.jpg)"'
img_pic = re.compile(reg)  # 返回的是一个匹配对象，它单独使用就没有任何意义，需要和findall(), search(), match(）搭配使用。
pic_url_list = re.findall(img_pic, response)

# 通过遍历图片地址列表，获取每个图片的地址
for pic_url in pic_url_list:
    # print(pic_url)
    pic_1 = requests.get(pic_url, headers)
    pic = pic_1.content  # content   以字节的方式响应对象，遇到图片的时候，我们可以使用
    # 为了保证所有的图片名字不冲突，我们使用time.time()生成的浮点型时间戳来代替名字
    pic_name = '%f.jpg' % time.time()
    with open("../../source/source_pic/" + pic_name, "wb") as file:
        file.write(pic)
print("亲爱的，让你久等了，下载完毕，请查收 ~ ~ ~！")
