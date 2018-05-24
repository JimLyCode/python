import sys

print(sys.argv)
delimiter="========================="

'''
Python字符串
'''
string = 'Hello Python!'

print(string)            # 输出完整字符串
print(string[0])         # 输出字符串中的第一个字符
print(string[2:7])       # 输出字符串中第三个至第七个之间的字符串
print(string[2:])        # 输出从第三个字符开始的字符串
print(string * 2)        # 输出字符串两次
print(string + "TEST")   # 输出连接的字符串
print(delimiter)
del string

'''
Python列表
'''
list = ['python', 3.4, 520, 'java', 'script', 888]
tinylist = ['answer', 59.80]

print(list)             # 输出完整列表
print(list[0])          # 输出列表的第一个元素
print(list[2:3])        # 输出第三个至第四(不包括)个元素
print(list[2:])         # 输出从第三个开始至列表末尾的所有元素
print(list * 2)         # 输出列表两次
print(list + tinylist)  # 打印组合的列表
print(delimiter)
del list, tinylist

'''
Python元组
'''
tuple = ('python', 3.4, 520, 'java', 'script', 888)
tinytuple = ('answer', 59.80)

print(tuple)                # 输出完整元组
print(tuple[0])             # 输出元组的第一个元素
print(tuple[1:3])           # 输出第二个至第四(不包括)个的元素
print(tuple[2:])            # 输出从第三个开始至列表末尾的所有元素
print(tuple * 2)            # 输出元组两次
print(tuple + tinytuple)    # 打印组合的元组
print(delimiter)
del tuple, tinytuple

'''
Python 字典
'''
dict = {};
dict['key'] = "this is string value"
dict[1] = 'this is number value'
tinydict = {"name": "answer", "age": 21, "sex": 'man'}

print(dict['key'])          # 输出键为'key' 的值
print(dict[1])              # 输出键为 1 的值
print(tinydict.pop("name")) # 移除tinydict字段中键为name的键值对, 返回对应的value
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值
print(delimiter)
del dict, tinydict

'''
Python数据类型转换
'''
print(int('100'), int(100.5))   # 将x转换为一个整数
print(float("100.5"))           # 将x转换到一个浮点数
print(type(str(123)))           # 将对象 x 转换为字符串
print(repr("12345"))            # 将对象 x 转换为表达式字符串
print(eval("pow(2, 3)"))        # 用来计算在字符串中的有效Python表达式, 并返回一个对象
print(tuple({"name": "answer", 12: 23}))    # 将序列 s 转换为一个元组(针对字典会返回字典的key组成的tuple)
print(tuple([123, 'xyz', 'zara', 'abc']))
print(list((123, 'xyz', 'zara', 'abc')))    # 将序列 s 转换为一个列表
x = set("good")
y = set('root')
print(x, y)     # 重复的被删除
print(x & y)    # 交集
print(x | y)    # 并集
print(x - y)    # 差集
print(dict({"name": "answer", 12: 23}))                 # 创建一个字典. d 必须是一个序列 (key,value)元组.  (dict() # 创建空字典)
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))    # 映射函数方式来构造字典
print(dict([('one', 1), ('two', 2), ('three', 3)]))     # 可迭代对象方式来构造字典
print(frozenset(range(5)))                              # 转换为不可变集合, 冻结后集合不能再添加或删除任何元素
print(chr(97), chr(0x61))                               # 将一个整数转换为一个字符. 0x61是十六进制 0x61(十六进制)=97(十进制)
print(ord('a'))                                         # 将一个字符转换为它的整数值
print(hex(97))                                          # 将一个整数转换为一个十六进制字符串
print(oct(12))                                          # 将一个整数转换为一个八进制字符串










