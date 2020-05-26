# 定义一个菜单列表，其中的元素为字典
menu_list = [
    {"id": 1, "name": "1.糖醋里脊", "price": 24, "$": "元"},
    {"id": 2, "name": "2.糖醋鱼", "price": 28, "$": "元"},
    {"id": 3, "name": "3.大盘鸡", "price": 65, "$": "元"},
    {"id": 4, "name": "4.水煮肉片", "price": 26, "$": "元"},
    {"id": 5, "name": "5.梅菜扣肉", "price": 21, "$": "元"}
    ]
# 定义一个空列表存放点餐结果
Order_list = []
print('==========================欢迎光临开课吧食堂,祝您用餐愉快====================================')
print('今日菜单:')
# 遍历菜单打印出来，方便用户观看
for menu in menu_list:
    # 字典 的get() 函数返回指定键的值（与中括号作用一样）
    print(menu.get('name'), menu.get('price'), menu.get('$'))

# 定义一个循环让用户进行操作
while True:
    print('=' * 50)
    print("1.用户点餐\n2.取消点餐\n3.确认菜单\n4.结账")
    # 让用户输入，在下面根据输入内容判断进行什么操作
    server = int(input("请选择服务:"))
    # 输入为1 进入点菜
    if server == 1:
        # 定义一个循环，可以多次点菜
        while True:
            # 定义菜名编号或输入y退出
            menu_add = input("请输入菜名编号或输入Y结束点菜:")
            # 如果不是Y就开始点菜
            if menu_add.upper() != 'Y':  # upper() 方法将字符串中的小写字母转为大写字母
                for m in menu_list:
                    if m.get('id') == int(menu_add):
                        Order_list.append(m)
                        break
            # 输入Y就结束点菜并打印已点菜单
            else:
                print('==================已点菜=====================')
                total_price = 0
                # 遍历点菜菜单
                for order in Order_list:
                    print(order.get('name'), order.get('price'), order.get('$'))     # 计算总价
                    total_price += int(order.get('price'))
                # 打印总价
                print('                           小计:{}元'.format(total_price))
                break
    # 如果用户输入2，取消点菜
    elif server == 2:
        # 输入要取消的菜名
        menu_del = input("请输入要取消的菜名:")
        # 在点餐列表中查找要取消的菜名
        for order in Order_list:
            if order.get('id') == int(menu_del):
                Order_list.remove(order)
        # 取消点菜后打印剩余的已点菜
        print('==================已点菜=====================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'), order.get('price'), order.get('$'))
            total_price += int(order.get('price'))
        print('                           小计:{}元'.format(total_price))
    # 输入3表示确认已点菜单
    elif server == 3:
        # 打印已点菜单以及价格
        print('==================已点菜=====================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'), order.get('price'), order.get('$'))
            total_price += int(order.get('price'))
        print('                           小计:{}元'.format(total_price))
    # 输入4结账
    elif server == 4:
        print('=================您的消费菜单=======================')
        total_price = 0
        for order in Order_list:
            print(order.get('name'), order.get('price'), order.get('$'))
            total_price += int(order.get('price'))

        print('           总计消费:{}元'.format(total_price))

        print('==================欢迎您再次光临,再见!=====================')
        # 3 结账后用break退出循环（退出点餐系统）
        break
