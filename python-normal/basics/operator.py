import sys
import os
sys.path.append(r"E:\GitHub\python\python-normal")
import common
print(os.getcwd())

'''
    Python算术运算符
'''
a, b = 10.0, 3
print("a + b = ", (a + b))      # 加 - 两个对象相加
print("a - b = ", (a - b))      # 减 - 得到负数或是一个数减去另一个数
print("a * b = ", (a * b))      # 乘 - 两个数相乘或是返回一个被重复若干次的字符串
print("a / b = ", (a / b))      # 除 - x除以y
print("a % b = ", (a % b))      # 取模 - 返回除法的余数
print("a ** b = ", (a ** b))    # 幂 - 返回x的y次幂
print("a // b = ", (a // b))    # 取整除 - 返回商的整数部分
print(common.delimiter)
del a, b

'''
    Python比较运算符
'''
a, b = 10, 20
print("a == b: ", (a == b))     # 等于 - 比较对象是否相等
print("a != b: ", (a != b))     # 不等于 - 比较两个对象是否不相等
print("a > b: ", (a > b))       # 大于 - 返回x是否大于y
print("a < b: ", (a < b))       # 小于 - 返回x是否小于y. 所有比较运算符返回1表示真, 返回0表示假. 这分别与特殊的变量True和False等价
print("a >= b: ", (a >= b))     # 大于等于 - 返回x是否大于等于y
print("a <= b: ", (a <= b))     # 小于等于 - 返回x是否小于等于y
print(common.delimiter)
del a, b

'''
    Python赋值运算符
'''
a, b, c = 10, 20, 100
a = b
print("a = ", a)            # 简单的赋值运算符  ->  c = a + b 将 a + b 的运算结果赋值为 c
c += a
print("+= c = %d" % c)      # 加法赋值运算符    ->  c += a 等效于 c = c + a
c -= a
print("-= c = %d" % c)      # 减法赋值运算符    ->  c -= a 等效于 c = c - a
c *= a
print("*= c = %d" % c)      # 乘法赋值运算符    ->  c *= a 等效于 c = c * a
c /= a
print("/= c = %d" % c)      # 除法赋值运算符    ->  c /= a 等效于 c = c / a
c %= a
print("%%= c = %d" % c)      # 取模赋值运算符    ->  c %= a 等效于 c = c % a
c **= a
print("**= c = %d" % c)     # 幂赋值运算符      ->  c **= a 等效于 c = c ** a
c //= a
print("//= c = %d" % c)     # 取整除赋值运算符  ->  c //= a 等效于 c = c // a
print(common.delimiter)
del a, b, c

'''
    Python位运算符
'''
a, b = 60, 13
print("a & b = ", (a & b))      # 按位与运算符: 参与运算的两个值, 如果两个相应位都为1, 则该位的结果为1, 否则为0
print("a | b = ", (a | b))      # 按位或运算符: 只要对应的二个二进位有一个为1时, 结果位就为1
print("a ^ b = ", (a ^ b))      # 按位异或运算符: 当两对应的二进位相异时, 结果为1
print("~a = ", (~a))            # 按位取反运算符: 对数据的每个二进制位取反, 即把1变为0, 把0变为1. ~x 类似于 -x-1
print("a << 2 = ", (a << 2))    # 左移动运算符: 运算数的各二进位全部左移若干位, 由 << 右边的数字指定了移动的位数, 高位丢弃, 低位补0
print("a >> 2 = ", (a >> 2))    # 右移动运算符: 把">>"左边的运算数的各二进位全部右移若干位, >> 右边的数字指定了移动的位数
print(common.delimiter)
del a, b

'''
    Python逻辑运算符
'''
a, b = 10, 20
print("a and b: ", (a and b))       # 布尔"与" - 如果 x 为 False, x and y 返回 False, 否则它返回 y 的计算值
print("a or b: ", (a or b))         # 布尔"或" - 如果 x 是非 0, 它返回 x 的值, 否则它返回 y 的计算值
print("not a: ", (not a))           # 布尔"非" - 如果 x 为 True, 返回 False. 如果 x 为 False, 它返回 True
print(common.delimiter)
del a, b


'''
    Python成员运算符
'''
a, b, mylist = 10, 5, [1, 2, 3, 4, 5]
print("a in mylist: ", a in mylist)             # 如果在指定的序列中找到值返回 True, 否则返回 False
print("a not in mylist: ", a not in mylist)     # 如果在指定的序列中没有找到值返回 True, 否则返回 False
print("b in mylist: ", b in mylist)
print("b not in mylist: ", b not in mylist)
print(common.delimiter)
del a, b, mylist


'''
    Python身份运算符
    
    is 与 == 区别: is 用于判断两个变量引用对象是否为同一个,  == 用于判断引用变量的值是否相等
'''
a, b = 20, 20
print("a is b: ", (a is b))             # is 是判断两个标识符是不是引用自一个对象
print("a is not b: ", (a is not b))     # is not 是判断两个标识符是不是引用自不同对象
print(common.delimiter)
del a, b


