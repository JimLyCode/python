"""
    module: function defined
    author: answer
    time: 2018-5-28 10:00:23
"""
sum = lambda arg1, args2: arg1 + args2
print(sum(args2=20, arg1=3))
def sub(arg1, arg2):
    return arg1 - arg2
print(sub(12, 1))

def printinfo(arg1, *params):
    print("arg1:", arg1)
    for param in params:
        print(param)
    return
printinfo(112)
printinfo(12, 13, 14, 15, 16)


