# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DangdangPipeline(object):
#     def process_item(self, item, spider):
#         return item
import openpyxl


class DangdangBookPipeline(object):
    def __init__(self):
        # 初始化函数 当类实例化时这个方法会自启动
        self.wb = openpyxl.Workbook()
        # 创建工作薄
        self.ws = self.wb.active
        # 定位活动表
        self.ws.append(['图书名', '作者', '价格'])
        # 用append函数往表格添加表头

    def process_item(self, item, spider):
        # process_item是默认的处理item的方法，就像parse是默认处理response的方法
        line = [item['name'], item['author'], item['price']]
        # 把图书名、作者和书的价格都写成列表的形式，赋值给line
        self.ws.append(line)  # 用append函数把图书名、作者和书的价格等数据都添加进表格
        return item  # 将item丢回给引擎，如果后面还有这个item需要经过的itempipeline，引擎会自己调度

    def close_spider(self, spider):
        # close_spider是当爬虫结束运行时，这个方法就会执行
        self.wb.save('./dangdang_book.xlsx')  # 保存文件
        self.wb.close()  # 关闭文件
