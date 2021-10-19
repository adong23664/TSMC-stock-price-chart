import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('台灣證券.db')

plt.figure(figsize=(15,5),dpi = 300)
plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'

sql = 'Select * from 股票 where 證券代號 = "2330" ' 

df = pd.read_sql(sql,conn)

df = df.sort_values(by = '日期')
plt.plot(df['日期'],df['收盤價'],label = df['證券名稱'][0])

plt.legend()
plt.grid()
plt.title('台積電股價走勢圖',fontsize = 30)
plt.xticks(np.linspace(0, len(df)-1, 13))
plt.savefig('4-4台積電一年股價.png')
