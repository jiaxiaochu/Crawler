# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


# 生成词云图
def create_word_cloud(filename):
    # 读取文件内容
    text = open("{}.txt".format(filename), encoding='utf-8').read()

    # 注释部分采用结巴分词
    # wordlist = jieba.cut(text, cut_all=True)
    # wl = " ".join(wordlist)

    # 设置词云
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数
        max_words=2000,
        # 这种字体都在电脑字体中，window在C:\Windows\Fonts\下，mac下可选/System/Library/Fonts/PingFang.ttc 字体
        font_path='C:\\Windows\\Fonts\\simfang.ttf',
        height=500,
        width=500,
        # 设置字体最大值
        max_font_size=60,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=30,
    )

    myword = wc.generate(text)  # 生成词云 如果用结巴分词的话，使用wl 取代 text， 生成词云图
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('signature.png')  # 把词云保存下

create_word_cloud("sign")
