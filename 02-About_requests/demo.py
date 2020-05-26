# import requests
#
# response = requests.get('https://translate.google.cn/')
# print(response.text)
# print(response.content)
# print(response.request.headers)
# print(response.headers)
# print(response.content.decode())


'''
response.text 和response.content的区别

response.text
类型：str
解码类型： 根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
如何修改编码方式：response.encoding=”gbk”

response.content
类型：bytes
解码类型： 没有指定
如何修改编码方式：response.content.deocde(“utf8”)
获取网页源码的通用方式：

response.content.decode()
response.content.decode("GBK")
response.text
以上三种方法从前往后尝试，能够100%的解决所有网页解码的问题

所以：更推荐使用response.content.deocde()的方式获取响应的html页面
'''
import requests

response = requests.get('https://translate.google.cn/')
print(response.text)
print(response.content)
print(response.request.headers)
print(response.headers)
print(response.content.decode())
'''
访问response响应对象有三种方法：
            text  一般文本
            content   以字节的方式响应对象，遇到图片的时候，我们可以使用
            json  它是requests内置的json解码器，将json字符串解码成为字典
'''
