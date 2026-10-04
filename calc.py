# ==============================================================================
# 🌟 Pandas + 可视化 综合练习脚本（题目与答案合一版）
# 💡 提示：直接复制整段到 Jupyter 中运行，或者放到 PyCharm 里运行。
# ==============================================================================

# ================= 第一部分：环境配置与数据准备 =================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🚨 避坑：必须先美颜，再设置中文字体！
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['SimHei'] # 防止中文变方块
plt.rcParams['axes.unicode_minus'] = False   # 防止负号变方块

# 【题目1】：创建一个电商销售表格
# 建立一个包含 订单号、商品、单价、销量、备注 的数据表，其中备注有空值(None)
数据 = pd.DataFrame({
    '订单号': [101, 102, 103, 104, 105, 106, 107, 108],
    '商品': ['苹果', '香蕉', '苹果', '橘子', '香蕉', '葡萄', '苹果', '橘子'],
    '单价': [5.0, 3.0, 5.0, 4.0, 3.5, 8.0, 5.2, 4.2],
    '销量': [100, 200, 150, 80, 120, 50, 100, 120],
    '备注': ['新鲜', '打折', None, '新鲜', '打折', '进口', '新鲜', None]
})
print("--- 题目1：原始数据 ---")
print(数据.head())


# ================= 第二部分：Pandas 数据清洗与筛选 =================
# 【题目2】：把“备注”列里的空值（None）填成 '未知'
# 💡 方法：用 fillna()
数据['备注'] = 数据['备注'].fillna('未知')
print("\n--- 题目2：填补空值后 ---")
print(数据['备注'].head())

# 【题目3】：新增一列 '总金额'，计算公式为 单价 * 销量
# 💡 方法：直接相乘赋值给新列
数据['总金额'] = 数据['单价'] * 数据['销量']
print("\n--- 题目3：新增总金额列 ---")
print(数据[['商品', '单价', '销量', '总金额']].head())

# 【题目4】：找出“总金额”大于 500 并且“备注”是“新鲜”的所有行
# 💡 方法：条件筛选，务必加括号！中间用 &
条件筛选 = 数据[(数据['总金额'] > 500) & (数据['备注'] == '新鲜')]
# 💡 方法2：用 query 优雅写法（外单引号，内双引号，列名不加引号）
# 条件筛选 = 数据.query('总金额 > 500 and 备注 == "新鲜"')
print("\n--- 题目4：筛选结果 ---")
print(条件筛选)

# 【题目5】：按“商品”分组，计算每种商品的“总金额”总和，按金额从大到小排序
# 💡 方法：groupby分组求和，reset_index恢复普通表格，sort_values降序
分组结果 = 数据.groupby('商品')['总金额'].sum().reset_index()
分组结果.sort_values(by='总金额', ascending=False, inplace=True)
print("\n--- 题目5：商品销售总额排序 ---")
print(分组结果)


# ================= 第三部分：Matplotlib 与 Seaborn 画图 =================
# 【题目6】：用 Seaborn 画出 单价(x) 和 总金额(y) 的散点图，按'商品'区分颜色(hue)
# 💡 避坑：所有标点必须是英文！hue 参数自动帮你上色
plt.figure(figsize=(8, 5)) # 设置画布大小
sns.scatterplot(data=数据, x='单价', y='总金额', hue='商品')
plt.title("单价与总金额的关系散点图") # 加标题
plt.show()

# 【题目7】：利用 Pandas 的 plot 功能，画出 销量 的折线图
# 💡 避坑：True 首字母必须大写，绝对不能拼成 Ture！kind='line'
数据.plot(kind='line', y='销量', grid=True, figsize=(8, 4), title="销量折线图")
plt.show()

# 【题目8】：画出数据中数值列（单价, 销量, 总金额）的相关性热力图
# 💡 避坑：corr() 只能对数值列生效，所以要先筛选出数值列
数值列 = 数据[['单价', '销量', '总金额']]
sns.heatmap(数值列.corr(), annot=True, cmap='coolwarm') # annot=True显示数字
plt.title("特征相关性热力图")
plt.show()

# 【题目9】：把 2 个图同时画在一张画布上（1行2列）
# 左边画“各商品销量”的柱状图，右边画“总金额分布”的直方图(bins=5)
fig, axes = plt.subplots(1, 2, figsize=(12, 5)) # 1行2列

# 左图：柱状图 (ax=axes[0])
sns.barplot(data=数据, x='商品', y='销量', ax=axes[0])
axes[0].set_title("各商品销量")

# 右图：直方图 (ax=axes[1])
sns.histplot(data=数据, x='总金额', bins=5, ax=axes[1])
axes[1].set_title("总金额分布")

plt.tight_layout() # 极其重要！自动调整间距，防止两张图挤在一起

# ================= 第四部分：保存与收尾 =================
# ⚠️ 终极避坑：savefig 必须写在 show 之前，不然保存的是白纸！
plt.savefig("exercise_chart.png", dpi=300, bbox_inches='tight')
plt.show()

print("\n全部通关！快去当前目录看看保存的 exercise_chart.png 吧！")