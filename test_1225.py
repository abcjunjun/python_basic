#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: 'longjh' time: 2018/12/25

"""
测试_1225
"""

d = {'A':1}
s = set([1, 2, 3, -1, 8])

l = [1,2,3,4,5]
l[2]
t = (1,2,3,4,5)
t[3]
s = "hello"
s[0]

10 // 3
10 % 3

# 集合运算
set1 = set("abc")
set2 = set("cde")
set1 | set2
set1 & set2
set1 - set2
set1 ^ set2

# type
type("abc")
type(123)
type(123.00)
type({3})

# 列表运算
[1,2,3] + [1,2,3]
"abc"+"cde"
[1,2,3] * 3

# 高级函数
# map
str(1)
map(str, [1, 2, 3])
list(map(str, [1, 2, 3]))
# filter 过滤
list(filter(lambda s: s%2 == 0 , range(10)))
# reduce 递归
from functools import reduce
reduce(lambda a, b: a + b, range(10))

[3] in [1, 2, 3, 4]
3 in [1, 2, 3, 4]

# 切片
aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
aList[3:7]
aList[7:3:-1]
aList[::-1]
aList[-2]

list(range(1,10))


# None
def fun():
    print("Hello!")
    return None

fun() is None

# zip
list(zip([1,2], [3,4]))
list(zip([1,2], [3,4], [5,6]))
for i, j, k in zip([1,2], [3,4], [5,6]):
    print(i, j, k)

# sort
l = list(range(10))[::-1]
sorted(l)   # 返回，本身不排序
l.sort(reverse=True)    # 本身排序

# 字典
x = {'a':'b', 'c':'d'}
'a' in x
'a' in x.keys()
'b' in x.values()

# 循环
for i in range(10):
    print(i)

    if i % 2:
        continue

    print(10*i)

    if i > 5:
        break

