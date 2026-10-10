#%%
data = """BJ,5.5,20,45
SH,3.2,15,32
BJ,8.0,35,60
SZ,2.5,10,25
SH,6.0,25,50
BJ,4.2,18,38
SZ,None,12,28
SH,7.5,30,55
BJ,3.0,14,30
SZ,5.0,22,42"""

with open('order.txt', 'w', encoding='utf-8') as f: # open(打开) write(写入)
    f.write(data) # write(写入)
print("order.txt ready!") # ready(准备好)
l=[]
with open('order.txt','r',encoding='utf-8')as f:
    for line in f:
        p=line.strip().split(',')
        d={'city':p[0],'dist':float(p[1])if p[1]!='None' else None,'time':int(p[2]),'amount':int(p[3])}
print(f"Total:{len(l)}")
print(l[0])


import numpy as np
v_d=np.array([i['dist']for i in l if i['dist']is not None])
v_t=np.array([i['time']for i in l if i['dist']is not None])
print(f"Vector d:{v_d}")
print(f"Vector t:{v_t}")
dot_val=np.dot(v_d,v_t)
print(f"Dot Product(总距离时间积):{dot_val}")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
df=pd.DataFrame(l)
df['dist']=df['dist'].fillna(df['dist'].mean())
df['spend']=df['dist']/df['time']
high=df[(df['dist']>3)&(df['amount']>40)]
print("\nHigh orders(高价值订单):")
print(high[['city','amount','time']])


r=df.groupby('city').agg({
    'amount':'mean',
    'spend':'max',
}).reset_index()
print("\nGrouped Stats(分组统计):")
print(r)


np.random.seed(42)
nd=np.random.normal(loc=0,scale=1,size=10000)
w1=np.mean((nd>-1)&(nd<1))
print(f"\nStd1(±标准差比例):{w1:.2%}")


def loss(x):
    return(x-15)**2
x=0
lr=0.1
h=0.0001
print("\nGradient Descent(梯度下降):")
for i in range(10):
    g=(loss(x+h)-loss(x))/h
    x=x-lr*g
    print(f"Step{i+1}:x={x:.4f},loss={loss(x):.4f}")



