# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
"""
使用JSON.dumps将字典转成JSON字符串

result = json.dumps(json_dict)
使用JSON.loads将JSON字符串转成字典

test_dict = json.loads('{"age": 18, "name": "laowang"}')
return json.dumps(json_dict)
jsonify会指定响应内容的数据格式(告诉客户端我返回给你的数据格式是什么)

return jsonify(json_dict)`
"""
import json

# a = {"title": "今天是学习爬虫的第1天！", "date": "2019.10.1", "content": "今天是学习爬虫的第1天！我学习了爬虫基础啦！"}
a = {"name": "xiaoming"}
print(a, type(a))
new_a = json.dumps(a)
print(new_a, type(new_a))
b = json.loads(new_a)
print(b, type(b))
