#一、 数据结构与创建
import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3], index=['a', 'b', 'c']) # 一维数据（Series）
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})   # 二维表格（DataFrame）
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b']) # 用列表创建并指定列名
# %%
#二、 读取与保存数据
df = pd.read_csv('data.csv')      # 读取 CSV 文件
df = pd.read_excel('data.xlsx')   # 读取 Excel 文件
df = pd.read_sql('select * from table', conn) # 读取 SQL 数据库

df.to_csv('out.csv', index=False) # 保存为 CSV（不保存索引）
df.to_excel('out.xlsx', index=False) # 保存为 Excel
# %%
#三、 查看数据基本信息（最常用）
df.head(3)        # 查看前 3 行（默认 5 行）
df.tail(3)        # 查看后 3 行
df.shape          # 查看行数、列数 (行, 列)
df.info()         # 查看数据类型、非空值数量、内存占用
df.describe()     # 查看数值列的统计信息（均值、标准差等）
df.dtypes         # 查看每一列的数据类型
df.columns        # 查看列名
df.index          # 查看行索引
df.values         # 查看底层数值（返回 Numpy 数组）
# %%
#四、 数据清洗与处理（空值、重复值、替换）
df.isnull()                   # 判断哪里有空值（返回布尔表）
df.notnull()                  # 判断哪里非空
df.dropna()                   # 删除包含空值的行
df.dropna(axis=1)             # 删除包含空值的列
df.dropna(how='all')          # 只删除全为空的行
df.fillna(0)                  # 将空值填充为 0
df.fillna({'A': 0, 'B': '未知'}) # 按列分别填充空值

df.duplicated()               # 判断重复行
df.drop_duplicates()          # 删除重复行

df.replace(1, -1)             # 将所有的 1 替换成 -1
df['A'].astype('float')       # 修改某列的数据类型
df.rename(columns={'A': 'A_new'}) # 重命名列
# %%
#五、 数据筛选、切片与修改（行与列）
df['A']               # 提取单列（返回 Series）
df[['A', 'B']]        # 提取多列（返回 DataFrame）
df[df['A'] > 1]       # 条件筛选（找出 A 列大于 1 的行）

df.loc[0, 'A']        # 按【标签】提取（第0行，A列）
df.iloc[0, 0]         # 按【位置】提取（第0行，第0列）
df.iloc[0:2, 0:2]     # 切片提取（前2行，前2列）

df['新列'] = 1        # 新增一列，全部赋值为1
df.insert(0, '序列', range(1, len(df) + 1)) # 在第0列插入自增序号
df.drop(columns=['A']) # 删除 A 列
df.drop(index=[0, 1])  # 删除 0 和 1 行
# %%
#六、 排序与索引重置
df.sort_values(by='A', ascending=False) # 按 A 列降序排列（默认升序）
df.sort_index()                         # 按索引排序

df.reset_index(drop=True)   # 重置索引（drop=True 删除原索引，不变成新列）
df.reset_index(drop=False)  # 重置索引（原索引会变成一个新列保留）
df.set_index('A')           # 将 A 列设为新的索引
# %%
#七、 合并与连接
pd.concat([df1, df2])             # 上下拼接（纵向堆叠）
pd.concat([df1, df2], axis=1)     # 左右拼接（横向拼接）
pd.merge(df1, df2, on='key')      # 按 key 列合并（默认 inner 交集）
pd.merge(df1, df2, how='left', on='key') # 左连接（保留左表所有数据）
pd.merge(df1, df2, how='outer', on='key')# 外连接（并集）
# %%
#八、 分组聚合与数据透视表
df.groupby('A')['B'].mean()       # 按 A 列分组，求 B 列的均值
df.groupby('A').agg({'B': 'sum', 'C': 'max'}) # 按 A 分组，对 B 求和，对 C 求最大值

pd.pivot_table(df, values='B', index='A', columns='C', aggfunc='mean') # 数据透视表（类似 Excel 透视表）
# %%
#九、 常用统计与计算
df['A'].sum()          # 求和
df['A'].mean()         # 求均值
df['A'].max() / min()  # 最大值 / 最小值
df['A'].count()        # 非空值数量
df['A'].value_counts() # 查看唯一值及出现频次（常用于统计类别）
df['A'].unique()       # 查看唯一值
df.cumsum()            # 累计求和
df.corr()              # 计算相关系数矩阵
df.median()            #中位数
# %%
#十、 应用函数（Apply / Map）
df['A'].apply(lambda x: x * 2)    # 对 A 列每个元素乘以 2
df['A'].map({1: '男', 2: '女'})    # 将 A 列的值按字典映射替换
df.apply(lambda row: row['A'] + row['B'], axis=1) # 按行进行复杂计算
# %%
#补充笔记：Pandas 文本/字符串处理（.str）
# 1. 包含特定文字（模糊搜索）
数据[数据['备注'].str.contains('新鲜', na=False)] # 找备注里带“新鲜”的行
# ⚠️ 防坑：如果列里有空值（None/NaN），必须加 na=False，否则会报错崩溃！

# 2. 以特定文字开头/结尾
数据[数据['姓名'].str.startswith('张', na=False)]  # 找姓张的
数据[数据['地址'].str.endswith('市', na=False)]    # 找以“市”结尾的

# 3. 去除首尾空格（清洗数据神器）
数据['姓名'] = 数据['姓名'].str.strip()  # 把“ 张三 ” 变成 “张三”

# 4. 字符串替换
数据['备注'] = 数据['备注'].str.replace('打折', '促销') # 把“打折”换成“促销”

# 5. 按长度筛选
数据[数据['姓名'].str.len() == 2] # 名字只有2个字的
# %%
#
# 1. 统计频次：每种水果出现了多少次
数据['水果'].value_counts()   # 这不是 groupby，但常用于统计频次！

# 2. 分组求和：按“类别”分组，算“总金额”的总和
数据.groupby('类别')['总金额'].sum()

# 3. 分组求平均：按“水果”分组，算“单价”的平均值
数据.groupby('水果')['单价'].mean()
