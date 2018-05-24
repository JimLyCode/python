import keyword
import sys
print("Python key words: " + ','.join(keyword.kwlist))
print("Hello, Python!")

# 注释1
'''
注释2-多行注释
'''
"""
注释3-多行注释
"""

num = 3
if num == 1:
    print("true")
elif num == 3:
    print("num is: "); print(12 + num)  # 同一行中使用多条语句，语句之间使用分号(;)分割
else:
    print("false");print(" False")

paragraph = """this is a paragraph,
this is a paragraph.
"""
print(paragraph)

# input("按下 enter 键退出，其他任意键显示...\n")

print("123 ", "456")

# 打印脚本传入参数, sys.argv[0] 代表文件本身路径, 所带参数从 sys.argv[1] 开始
print(sys.argv)
