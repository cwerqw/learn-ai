import pandas as pd
路径='d:/代码练习/da.xlsx'
读取数据=pd.read_excel(路径,index_col='序号')
#print(读取数据.shape)
#print(读取数据.columns)
#print(读取数据.dtypes)
总分=pd.Series([175,170],index=['张三','李四'],name='两门总分')
#print(总分)
#空值行=读取数据[读取数据['语文'].isnull()]
#print(空值行)
语文均数=读取数据['语文'].mean()
数学均数=读取数据['数学'].mean()
读取数据['语文']=读取数据['语文'].fillna(语文均数)
读取数据['数学']=读取数据['数学'].fillna(数学均数)
读取数据['总分']=读取数据['语文']+读取数据['数学']
#print(读取数据)
读取数据.sort_values(by='总分', ascending=False,inplace=True)
读取数据.reset_index(drop=True,inplace=True)
#print(读取数据)
结果=读取数据.loc[读取数据['姓名'].isin(['张三','李四']),['城市','总分']]
#print(结果)
结果=读取数据.query('城市=="北京" and 总分>170')
#print(结果)
import pandas as pd
数据 = pd.DataFrame({
    '商品': ['苹果', '香蕉', '苹果', '橘子', '香蕉', '葡萄'],
    '单价': [5, 3, 5, 4, 3, 8],
    '数量': [10, 20, None, 15, 30, 10],
    '备注': ['新鲜', '打折', '新鲜', None, '打折', '进口']
})
#print(数据.shape)
#print(数据.columns)
#print(数据.head(2))
数量均值=数据['数量'].mean()
数据['数量'] = 数据['数量'].fillna(数量均值)
#print(数据.dropna())
数据['总价']=数据['单价']*数据['数量']
#print(数据)
数据.sort_values(by='总价', ascending=False,inplace=True)
#print(数据)
#数据.reset_index(drop=True,inplace=True)
#print(数据)
练手 = pd.DataFrame(
    [[10, 20], [30, 40], [50, 60]],
    columns=['语文', '数学'],
    index=['张三', '李四', '王五']
)
#print(练手)
#print(练手.iloc[:,0])
#print(数据.query('单价 >= 3 and 备注 == "打折"'))
#print(数据[(数据['商品'] == '苹果') & (数据['单价'] > 4)])
# %%
#import pandas as pd

数据 = pd.DataFrame({
    '订单号': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    '水果': ['苹果', '香蕉', '橘子', '苹果', '香蕉', '葡萄', '苹果', '橘子'],
    '类别': ['仁果类', '热带水果', '柑橘类', '仁果类', '热带水果', '浆果类', '仁果类', '柑橘类'],
    '单价': [5, 3, 4, 5, 3.5, 8, 5.2, 4.2],
    '数量': [10, 20, 15, 8, 12, 5, 15, 10],
    '备注': ['新鲜', '打折', None, '新鲜', '打折', '进口', '新鲜', None]
})
数据.set_index('订单号', inplace=True) # 把订单号设为索引
#print(数据.fillna('未知'))
数据['销售额']=数据['单价']*数据['数量']
数据.rename(columns={'销售额': '总金额'}, inplace=True)
#数据.sort_values(by='总金额', ascending=False,inplace=True)
#数据.reset_index(drop=False,inplace=True)
#print(数据.query('类别=="热带水果" and 单价>3'))
print(数据)
#print(数据.loc[1003:1006,['水果','总金额']])
#print(数据.iloc[1:4,0:3])
print(数据[数据['水果'].str.startswith('苹',na=False)])
