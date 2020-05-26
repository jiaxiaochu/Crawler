# 计算1-100的偶数累加和

# sum = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)
############################
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i += 1
print(sum)
##############################
# encoding=utf-8

# i = 1
# sum = 0
# num_list1 = []
# num_list2 = []
#
# while i <= 100:
#     if i % 2 != 0:
#         num_list1.append(i)
#         sum = sum + i
#     else:
#         num_list2.append(i)
#         sum2 = sum + i
#     i += 1
# # print(sum)
# print("1~100的奇数累积和为:%d" % sum)
# print("1~100的偶数%s累积和为:%d" % (num_list2, sum))


sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)





