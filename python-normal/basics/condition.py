import sys
sys.path.append(r"E:\GitHub\python\python-normal")
import common

"""
    if
    while   while ... else
    for     for ... else
"""

num = 100
if num >= 90:
    print("score", num, "is A.")
elif 60 <= num < 90:
    print("score", num, "is B.")
else:
    print("score", num, "is C.")
print(common.delimiter)
del num


cnt = 0
while (cnt < 5):
    print("the cnt is", cnt)
    cnt += 1
print("the value of the final cnt: ", cnt)
print(common.delimiter)

'while ... else'
while (cnt > 0):
    print("the cnt is", cnt)
    cnt -= 1
else:
    print("the value of the final cnt: ", cnt)
print(common.delimiter)
del cnt


for letter in 'Python':
    print("current letter is:", letter)
print(common.delimiter)

fruits = ["orange", "apple", "banane"]
for fruit in fruits:
    print("current fruit is:", fruit)
print(common.delimiter)

for index in range(len(fruits)):        # len(fruits) 列表fruits的元素个数
    print("current fruit is:", fruits[index])
print(common.delimiter)

'''
    在 python 中, for … else 表示这样的意思
    for 中的语句和普通的没有区别, else 中的语句会在循环正常执行完(即 for 不是通过 break 跳出而中断的)的情况下执行, while … else 也是一样
'''
for num in range(10, 20):               # 迭代 10 到 20 之间的数字
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d = %d * %d" % (num, i, j))
            break
    else:
        print(num, "是一个质数")
print(common.delimiter)

'Python pass是空语句, 是为了保持程序结构的完整性. pass 不做任何事情, 一般用做占位语句'
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)
print("Good bye!")






