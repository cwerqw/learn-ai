# 如果没有安装 numpy，先在 PyCharm 终端运行：pip install numpy
import numpy as np  # 导入 numpy，给它起个别名 np

# 先把普通列表变成向量
a = np.array([1, 2, 3])  # 把列表变成向量 a
b = np.array([4, 5, 6])  # 把列表变成向量 b


print("========== 一、运算符 ==========")
print(a + b)    # 对应位置相加，结果是 [5 7 9]
print(a - b)    # 对应位置相减，结果是 [-3 -3 -3]
print(a * b)    # 对应位置相乘，结果是 [ 4 10 18]
print(a / b)    # 对应位置相除，结果是 [0.25 0.4  0.5 ]
print(a ** 2)   # 每个元素求平方，结果是 [1 4 9]
print(a @ b)    # 点积：1*4 + 2*5 + 3*6，结果变成 32 一个数
print(a == b)   # 逐个比较，结果是 [False False False]


print("========== 二、基础运算函数（和符号等价） ==========")
print(np.add(a, b))       # 跟 a + b 一样，结果是 [5 7 9]
print(np.subtract(a, b))  # 跟 a - b 一样，结果是 [-3 -3 -3]
print(np.multiply(a, b))  # 跟 a * b 一样，结果是 [ 4 10 18]
print(np.divide(a, b))    # 跟 a / b 一样，结果是 [0.25 0.4  0.5 ]


print("========== 三、向量专属运算 ==========")
print(np.dot(a, b))       # 点积，跟 a @ b 一样，结果是 32
print(np.cross([1,0,0], [0,1,0]))  # 叉积（三维向量才有），结果是 [0 0 1]
print(np.linalg.norm([3, 4]))      # 求向量长度（勾股定理），3的平方+4的平方开根号，结果是 5.0
print(a.T)                # 转置，一维向量看不出变化，矩阵才明显


print("========== 四、统计与聚合 ==========")
print(np.sum(a))      # 把所有元素加起来，1+2+3 = 6
print(np.mean(a))     # 求平均值，(1+2+3)/3 = 2.0
print(np.max(a))      # 找最大值，结果是 3
print(np.min(a))      # 找最小值，结果是 1
print(np.argmax(a))   # 最大值在哪个位置？下标是 2
print(np.argmin(a))   # 最小值在哪个位置？下标是 0


print("========== 五、逐元素数学函数 ==========")
print(np.sqrt(a))     # 每个数开平方，结果是 [1.  1.414 1.732]
print(np.exp(a))      # 每个数求 e 的次方，结果是 [ 2.718  7.389 20.085]
print(np.log(a))      # 每个数求自然对数，结果是 [0.  0.693 1.099]
print(np.sin(a))      # 每个数求正弦
print(np.cos(a))      # 每个数求余弦
print(np.abs([-1, -2]))  # 每个数求绝对值，结果是 [1 2]


print("========== 六、形状操作 ==========")
print(a.shape)            # 看形状，结果是 (3,)，表示 3 个元素的一维向量
print(a.reshape(3, 1))    # 变成 3 行 1 列：
                          # [[1]
                          #  [2]
                          #  [3]]
print(np.concatenate((a, b)))  # 把两个向量拼在一起，结果是 [1 2 3 4 5 6]
print(np.stack((a, b)))   # 把两个向量叠成矩阵：
                          # [[1 2 3]
                          #  [4 5 6]]
print(np.zeros(3))        # 造 3 个 0 的向量，结果是 [0. 0. 0.]
print(np.ones(3))         # 造 3 个 1 的向量，结果是 [1. 1. 1.]


print("========== 七、原生列表的坑（千万别搞错） ==========")
list_a = [1, 2, 3]  # 普通列表
list_b = [4, 5, 6]  # 另一个普通列表
print(list_a + list_b)  # 结果是 [1, 2, 3, 4, 5, 6]，是拼接，不是数学加法！
print(list_a * 2)       # 结果是 [1, 2, 3, 1, 2, 3]，是重复，不是数学乘法！