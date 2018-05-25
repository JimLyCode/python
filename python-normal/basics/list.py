"Python list的使用手册: http://www.runoob.com/python/python-lists.html"
list = ["vfc"]  # 空列表
list.insert(0, "baidu")
list.append("tenxun")
list.append("alibaba")
print(list)
del list[0]

print(list)
print(len(list))
print(list * 2)
print('baidu' in list)
print(list.count('baidu'))

for company in list:
    print(company)

print(list.reverse())



