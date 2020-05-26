# coding = utf-8
import requests
import csv

with open('limiao2.txt', 'w', newline='') as f:
    # 写入文件的标头
    file = csv.writer(f)
    header = ['文章标题', '摘要', '链接']
    file.writerow(header)
    # for i in range(3):
    for i in range(5):
        url = 'https://www.zhihu.com/api/v4/members/lisanshui1230/articles'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        # 将参数封装为字典
        param = {
            'include': 'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,'
                       'comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,'
                       'voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
            'offset': str(i * 20),
            'limit': '20',
            'sort_by': 'created'
        }
        # 获取数据
        res_article = requests.get(url, params=param, headers=headers)
        res_article.encoding = res_article.apparent_encoding
        # 解析数据
        json_article = res_article.json()
        list_article = json_article['data']
        # 定义一个空列表，存储数据
        list_all = []
        for i in list_article:
            # 文章标题
            title = i['title']
            # 文章摘要
            novel = i['excerpt']
            # 链接
            link = i['url']
            list_all = [title, novel, link]
            file.writerow(list_all)
print('爬取完成')
