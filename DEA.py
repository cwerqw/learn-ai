# ==============================================================================
# 🌟 第五周：引导式数据探索 (Guided EDA) 全流程模板
# 💡 说明：这是一个完整的代码框架，把你自己的数据套进来即可。
# 💡 变量名(df)可以随便改，列名必须和你文件里一模一样。
# ==============================================================================

# ================= 周一：环境配置与数据初探 =================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🔴 固定配置：绝对不能改
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ：这里换成你自己的文件路径和文件名
df = pd.read_csv('你的文件名.csv') # df也可以改成你自己的变量名，比如 data，但后面都要跟着改

# ：括号里换成你的列名（如果没有这列就删掉这一行）
print(df.head())          # 看前5行
print(df.shape)           # 看行数和列数
df.info()                 # 看数据类型和缺失情况
print(df.describe())      # 看数值列统计信息
print(df['你的分类列名'].value_counts()) # 看分类列分布

# ================= 周二：数据清洗与编码 =================
# ：替换为你要填充的列名
df['你的数字列名'] = df['你的数字列名'].fillna(df['你的数字列名'].median())
df['你的分类列名'] = df['你的分类列名'].fillna(df['你的分类列名'].mode()[0])

# ：替换为你需要独热编码的列名
df = pd.get_dummies(df, columns=['你的分类列名1', '你的分类列名2'], drop_first=True)

# ：替换为你不需要的列名（比如ID、姓名）
df.drop(columns=['你的无用列名'], inplace=True)

# ：保存清洗后的文件名
df.to_csv('你的清洗后文件名.csv', index=False)

# ================= 周三：分组聚合 (groupby) =================
print(df.groupby('你的分组列名')['你的计算列名'].mean()) # 单列分组

# 多列分组（⚠️ 必须加 reset_index()，否则画图找不到列）
df_stats = df.groupby(['你的分组列1', '你的分组列2'])['你的计算列名'].mean().reset_index()
print(df_stats)

df_stats2 = df.groupby('你的分组列名').agg({
    '你的指标列1': 'mean',
    '你的指标列2': 'sum',
    '你的计数列': 'count'
}).reset_index()
print(df_stats2)

# ================= 周四：可视化 =================
# 1. 柱状图
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='你的分类列', y='你的数值列')
plt.title("你的图表标题")
plt.show()

# 2. 箱线图
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='你的分类列', y='你的数值列')
plt.title("你的图表标题")
plt.show()

# 3. 热力图（自动挑选所有数值列，无需改列名）
num_cols = df.select_dtypes(include=['float64', 'int64', 'uint8'])
plt.figure(figsize=(10, 8))
sns.heatmap(num_cols.corr(), annot=True, cmap='coolwarm')
plt.title("特征相关性热力图")
plt.show()

# ================= 周五：生成报告与复盘日志 =================
# 🔴 固定写法：生成 README 报告
with open('README.md', 'w', encoding='utf-8') as f:
    f.write("# 我的 EDA 分析报告\n\n- 这里写你发现的结论1\n- 这里写你发现的结论2")

# ================= 周六：确保复现性 =================
# 🔴 固定写法：设置随机种子
np.random.seed(42)

# 🔴 固定写法：生成踩坑记录日志
with open('stuck_log.md', 'w', encoding='utf-8') as f:
    f.write("# 本周踩坑记录\n1. 忘记 reset_index()\n2. 忘记设置中文字体")

# ================= 周日：Git 提交 =================
# 🔴 固定写法：这些是终端命令，不要写在 Jupyter 里！
print("请打开终端，依次输入以下命令完成提交：")
print("git init")
print("git add .")
print("git commit -m '完成第五周 Guided EDA 项目'")
print("git remote add origin 你的仓库地址")
print("git push -u origin main")