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

# 指定第二个元素进行排序
def takeSencode(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素进行排序并降序
random.sort(key=takeSencode, reverse=True)
print(random)


