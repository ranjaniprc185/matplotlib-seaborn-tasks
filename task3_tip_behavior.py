import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("datasets/tips.csv")
df['tip_bill']=df['tip']/df['total_bill']*100
avg=df.groupby('day')['tip_bill'].mean()
plt.bar(avg.index, avg.values, color='skyblue')
plt.ylabel('average tip')
plt.xlabel('day')
plt.show()
