# ==============================================================================
# 🌟 数据可视化：Matplotlib + Seaborn 终极速查字典（防坑修正版）
# 💡 提示：本笔记为速查模板，变量名如 数据、x_data 需要替换为你自己的数据。
# ==============================================================================
jupyter lab

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# %%
# 一、 环境配置与防坑（顺序绝不能错！）
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# 1. 🚨 先美颜！set_theme 会重置 matplotlib 的所有配置，必须放在第一句！
sns.set_theme(style="whitegrid")

# 2. 后设置字体！解决中文标题和负号显示成方块的问题
# 💡 跨平台提示：Windows用'SimHei'，Mac用'Arial Unicode MS'，Linux/Colab用'WenQuanYi Micro Hei'
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# %%
# 二、 Matplotlib 基础结构（精装修与保存）
# 1. 画图三步走
plt.figure(figsize=(8, 5))        # 建立新画布（宽, 高），解决图表太挤的问题
plt.plot([1, 2, 3], [4, 5, 6], label='折线图') # 画折线图（label用于生成图例）
plt.title("图表标题")             # 加图表标题
plt.xlabel("X轴名字")             # 加横坐标名字
plt.ylabel("Y轴名字")             # 加纵坐标名字
plt.legend()                     # 根据label自动生成图例（💡统一用这种，不要用 legend(['图例1'])）

# ⚠️ 核心避坑：保存图片必须写在 show() 之前！
plt.savefig("my_chart.png", dpi=300, bbox_inches='tight') # dpi=300高清，tight裁掉白边
plt.show()                        # PyCharm必写，Jupyter可省略

# 💡 清空画布的正确时机：仅当你要在同一段代码里画下一张完全不同的图时，才在画新图前调用！
# plt.clf()                       # 清空当前画布，防止图叠在一起（写在 plt.figure() 之前或代替它）

# %%
# 三、 Seaborn 五大核心图（万能公式填空）
# 通用公式：sns.画图函数(data=数据, x='横坐标列', y='纵坐标列', hue='分类列')
# 💡 hue的作用：自动根据分类列，给点或线标不同颜色。

# 1. 折线图（看趋势，AI训练Loss曲线）
sns.lineplot(data=数据, x='时间列', y='数值列')
plt.show()

# 2. 散点图（看关系，hue自动按颜色分组）
sns.scatterplot(data=数据, x='特征1', y='特征2', hue='类别')
plt.show()

# 3. 柱状图（比大小，自动算平均值并画柱子）
sns.barplot(data=数据, x='分类列', y='数值列')
plt.show()

# 4. 单变量分布图（直方图，看数据分布形态）
sns.histplot(data=数据, x='数值列', bins=20, kde=True) # bins切20份，kde加平滑曲线
plt.show()

# 5. 双变量分布图（联合密度图，看两个特征交汇）
sns.kdeplot(data=数据, x='特征1', y='特征2', fill=True) # fill=True填充颜色
plt.show()

# 6. 热力图（AI特征相关性 EDA 必用！）
sns.heatmap(数据.corr(), annot=True, cmap='coolwarm') # annot=True显示数值，cmap冷暖色
plt.show()

# %%
# 四、 Seaborn 切图与样式（代替FacetGrid.map）
# 1. 简化版切图（强烈推荐！不要用底层的 FacetGrid.map()）
sns.relplot(data=数据, x='特征1', y='特征2', col='分类列') # 自动按分类列切成左右两张图
plt.show()

# 2. 样式设置（set_theme已替代了大部分样式设置）
# sns.set_style("darkgrid")       # 深色网格（默认是 whitegrid）
# sns.despine()                   # 隐藏上方和右侧的边框线

# %%
# 五、 AI 场景综合实战（双线对比图）
# 1. 双线对比（训练集 vs 验证集 Loss，💡统一规范写法）
plt.figure(figsize=(8, 5))
plt.plot(epochs, train_loss, label='Train Loss', color='blue', linestyle='-')  # 蓝色实线
plt.plot(epochs, val_loss, label='Val Loss', color='red', linestyle='--')      # 红色虚线
plt.title("Train vs Val Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend() # 自动根据label生成图例（💡不带参数最稳妥）
plt.show()

# %%
# 六、 补充：Matplotlib 子图（画多张图在同一行）
# 💡 适用场景：想一眼看四个不同特征的分布
fig, axes = plt.subplots(1, 2, figsize=(12, 4)) # 1行2列，宽12高4
sns.histplot(data=数据, x='特征1', ax=axes[0])  # ax=axes[0] 画在左边那个图
sns.scatterplot(data=数据, x='特征1', y='特征2', ax=axes[1]) # ax=axes[1] 画在右边
plt.tight_layout() # 自动调整子图间距，防止重叠
plt.show()
#%%
#笔记：
# 1.relplot是用来绘制关系数据图的，scatterplot和lineplot是relplot的一个封存
# 2.relpot在绘制的时候，不能直接给x和y指定具体的值，而应该使用data参数DataFrame中的列的名字
# 3.hue表示的是颜色，应该制定为某个列的名字。那么sns会自动的将指定的列的值的个数，取不同颜色
# 4.col表示分成几个图像，应该指定某个列的名字。那么sns会自动的将DataFrame中这个列的数据，分成多个图
# 5.style在绘制折线的时候，可以用来指定线条的样式
# 分类散点图
# stripplot和swarmplot
# swramplot采用了一定的算法，可以让点不会重叠
# 分类散点图特点是swarmplot，不太合适数据量特别大的
# 统计图
# 条形图：boxplot，他会自动进行统计(平均数，比例等)，也可以通过'estimator'参数来修改统计函数
# 柱状图：countplot，只能统计某个变量数据的个数，x和y只能传一个
# 点线图：pointplot，可以看出某个变量的变化关系
分布绘图
#单一变量绘图：用得上'distplot'，这个函数不仅仅可以绘制直方图，还可以绘制KDE曲线以及rug线，rug线越集中，说明数据越密集
#多变量绘图：用的是'jointplot'，这个函数比传统的散点图可以展示更多的信息，在右边和顶部展示两个直方图
