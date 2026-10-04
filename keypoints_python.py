# 关键字
if 10 > 5:              # 如果 10 大于 5
    print("大")         # 就打印“大”
elif 10 == 5:           # 不然如果 10 等于 5
    print("相等")       # 就打印“相等”
else:                   # 否则
    print("小")         # 就打印“小”

for i in range(3):      # 从 0 到 2，一个个来
    print(i)            # 打印 i

while True:             # 只要条件是真的，就一直循环
    break               # 碰到 break，不循环了，直接跳出

def add(a, b):          # 定义一个函数，叫 add
    return a + b        # 把 a+b 交出去，然后函数下班

try:                    # 试着运行下面的代码
    a = int("abc")      # 把 abc 转成整数，会出错
except ValueError:      # 抓到 ValueError 这种错
    print("转不了")     # 就打印“转不了”
finally:                # 不管出不出错
    print("结束")       # 最后都打印“结束”

import math             # 导入 math 模块
from math import sqrt   # 从 math 里只导入 sqrt
import math as m        # 导入 math，并起个别名 m

class Dog:              # 定义一个类，叫 Dog
    pass                # 先占个位，啥也不做

f = lambda x: x + 1     # 写个匿名小函数，给 x 加 1
print(f(2))             # 打印 3

with open("a.txt", "w") as f:  # 打开文件，自动帮你关
    f.write("hello")           # 写点东西进去

x = 10                  # 普通变量
print(x is None)        # 看看 x 是不是 None，不是
print(1 in [1, 2, 3])   # 1 在列表里吗？在
print(True and False)   # 真并且假，结果是假
print(True or False)    # 真或者假，结果是真的
print(not True)         # 不真，就是假
# %%
#内置函数
if 10 > 5:              # 如果 10 大于 5
    print("大")         # 就打印“大”
elif 10 == 5:           # 不然如果 10 等于 5
    print("相等")       # 就打印“相等”
else:                   # 否则
    print("小")         # 就打印“小”

for i in range(3):      # 从 0 到 2，一个个来
    print(i)            # 打印 i

while True:             # 只要条件是真的，就一直循环
    break               # 碰到 break，不循环了，直接跳出

def add(a, b):          # 定义一个函数，叫 add
    return a + b        # 把 a+b 交出去，然后函数下班

try:                    # 试着运行下面的代码
    a = int("abc")      # 把 abc 转成整数，会出错
except ValueError:      # 抓到 ValueError 这种错
    print("转不了")     # 就打印“转不了”
finally:                # 不管出不出错
    print("结束")       # 最后都打印“结束”

import math             # 导入 math 模块
from math import sqrt   # 从 math 里只导入 sqrt
import math as m        # 导入 math，并起个别名 m

class Dog:              # 定义一个类，叫 Dog
    pass                # 先占个位，啥也不做

f = lambda x: x + 1     # 写个匿名小函数，给 x 加 1
print(f(2))             # 打印 3

with open("a.txt", "w") as f:  # 打开文件，自动帮你关
    f.write("hello")           # 写点东西进去

x = 10                  # 普通变量
print(x is None)        # 看看 x 是不是 None，不是
print(1 in [1, 2, 3])   # 1 在列表里吗？在
print(True and False)   # 真并且假，结果是假
print(True or False)    # 真或者假，结果是真的
print(not True)         # 不真，就是假
# %%
#字符串方法（用“字符串.方法()”）
s = "apple,banana,apple"

print(",".join(["我", "爱", "Python"]))  # 用逗号把一堆字符串串起来：我,爱,Python
print(s.replace("apple", "orange"))      # 把 apple 换成 orange
print(s.find("banana"))                  # 找 banana 的位置，结果是 6
print(s.count("apple"))                  # 数 apple 出现几次，结果是 2

print(s.split(","))                      # 按逗号切开，结果是 ['apple', 'banana', 'apple']
print("  hi  ".strip())                  # 去掉两边空格，结果是 "hi"
print("ABC".lower())                     # 全变小写，结果是 "abc"
print("abc".upper())                     # 全变大写，结果是 "ABC"
print("hello world".title())             # 每个单词首字母大写，结果是 "Hello World"
print("hello".capitalize())              # 整句首字母大写，结果是 "Hello"

print(s.startswith("apple"))             # 是不是以 apple 开头，结果是 True
print(s.endswith("apple"))               # 是不是以 apple 结尾，结果是 True
print(s.index("banana"))                 # 找位置，找不到会报错，结果是 6
print(s.rfind("apple"))                  # 从右边开始找，结果是 13
print("123".isdigit())                   # 是不是全是数字，结果是 True
print("abc".isalpha())                   # 是不是全是字母，结果是 True
print("abc123".isalnum())                # 是不是字母或数字，结果是 True
print("   ".isspace())                   # 是不是全是空格，结果是 True

print("我叫{}".format("小明"))            # 格式化字符串，结果：我叫小明
print("abc".encode("utf-8"))             # 转成字节
print(b"abc".decode("utf-8"))            # 字节转回字符串
# %%
#列表方法（用“列表.方法()”）
nums = [1, 2, 3]

nums.append(4)          # 末尾加一个，变成 [1, 2, 3, 4]
nums.extend([5, 6])     # 末尾加一堆，变成 [1, 2, 3, 4, 5, 6]
nums.insert(0, 0)       # 在 0 位置插入 0，变成 [0, 1, 2, 3, 4, 5, 6]
nums.remove(3)          # 删掉值为 3 的那个
print(nums.pop())       # 弹出最后一个，并返回它
nums.clear()            # 全部清空
print(nums.index(2))    # 找 2 的位置
print(nums.count(2))    # 数 2 出现几次
nums.sort()             # 原地排序
nums.reverse()          # 原地反过来
new = nums.copy()       # 复制一份
# %%
#字典方法（用“字典.方法()”）
student = {"name": "小明", "age": 18}

print(student.get("name"))          # 拿 name 的值，结果是 小明
print(student.get("score", 0))      # 拿 score，没有就给默认 0
print(student.keys())               # 所有键
print(student.values())             # 所有值
print(student.items())              # 所有键值对

student.update({"age": 19})         # 更新 age
print(student.pop("age"))           # 弹出 age，并返回它的值
student.setdefault("score", 100)    # 有就拿，没有就设成 100
student.clear()                     # 清空
# %%
#集合方法
a = {1, 2, 3}
b = {3, 4, 5}

a.add(4)                # 加一个
a.remove(1)             # 删一个，没有会报错
a.discard(99)           # 删一个，没有也不报错
print(a.pop())          # 随便弹一个
a.clear()               # 清空

print({1, 2}.union({2, 3}))                 # 并集：{1, 2, 3}
print({1, 2}.intersection({2, 3}))          # 交集：{2}
print({1, 2}.difference({2, 3}))            # 差集：{1}
print({1, 2}.symmetric_difference({2, 3}))  # 对称差集：{1, 3}
# %%
#常见异常类型（写在 except 后面）
try:
    int("abc")              # 值不对
except ValueError:          # 抓住 ValueError
    print("值不对")         # 大白话：值不对

try:
    1 + "a"                 # 类型不对
except TypeError:           # 抓住 TypeError
    print("类型不对")       # 大白话：类型不对

try:
    [1, 2][5]               # 下标越界
except IndexError:          # 抓住 IndexError
    print("下标越界")       # 大白话：下标越界

try:
    {"a": 1}["b"]           # 字典没这个键
except KeyError:            # 抓住 KeyError
    print("没这个键")       # 大白话：没这个键

try:
    10 / 0                  # 除数为 0
except ZeroDivisionError:   # 抓住 ZeroDivisionError
    print("除数不能为 0")   # 大白话：除数不能为 0

try:
    open("不存在的文件.txt")  # 找不到文件
except FileNotFoundError:     # 抓住 FileNotFoundError
    print("找不到文件")       # 大白话：找不到文件

try:
    "abc".push()            # 字符串没有 push 方法
except AttributeError:      # 抓住 AttributeError
    print("没有这个属性")   # 大白话：没这个属性/方法

try:
    print(abc)              # 变量名没定义
except NameError:           # 抓住 NameError
    print("变量没定义")     # 大白话：变量没定义

try:
    import 不存在的模块      # 导入失败
except ImportError:         # 抓住 ImportError
    print("导入失败")       # 大白话：导入失败