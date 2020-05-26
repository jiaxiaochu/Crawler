# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# @blog : www.jiazhixiang.xyz
# @Author : Jiazhixiang
# -*- coding:utf-8 -*-
menu_list = [{"id": 1, "name": "1.蛋炒面", "price": "12", "¥": "元"},
             {"id": 2, "name": "2.回勺面", "price": "15", "¥": "元"},
             {"id": 3, "name": "3.刀削面", "price": "8", "¥": "元"},
             {"id": 4, "name": "4.饸饹面", "price": "9", "¥": "元"}]
order_list = []
print('===========公司食堂开业啦，欢迎大家============')
print('今日菜单')
for menu in menu_list:
    print(menu.get("name"), menu.get("price"), menu.get("¥"))
while True:
    print('=' * 50)
    print('1.点餐\n2.取消点菜\n3.确认菜单\n4.结账')
    choose = int(input('1请选择服务：'))
    if choose == 1:
        while True:
            menu_add = input('请输入菜名编号或输入n结束：')
            try:
                if menu_add.upper() != 'N':
                    if int(menu_add) in [1, 2, 3, 4]:
                        for m in menu_list:
                            if m.get('id') == int(menu_add):
                                print(m)
                                order_list.append(m)
                                print("order_list:{}".format(order_list))
                                break
                        else:
                            print('输入错误1')
            except Exception:
                print("输入有误,请重新输入")
