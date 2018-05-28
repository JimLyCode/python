import math as answermath   # math 模块提供了许多对浮点数的数学运算函数
import cmath                # cmath 模块包含了一些用于复数运算的函数
delimiter="========================="

print(dir(answermath))
print(delimiter)
print(answermath.pow(2, 5))
print(delimiter)
print(dir(cmath))
print(delimiter)

print(answermath.pi)
print(answermath.e)

print(r"\n")
print("\n")
print("\\n")
print(R"\n")

'Python字符串内建函数: http://www.runoob.com/python/python-strings.html'
print("asd".capitalize())


"""
引入common库

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import common
print(common.delimiter)
"""
