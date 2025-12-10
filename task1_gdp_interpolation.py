import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
w=pd.read_csv("C:\\Users\\ranja\\New folder (4)\\wdi.csv")
print(w.head())
country="India"
gdp=w[w['Country Name']==country].set_index("Year")["GDP"]
print('\n\n',gdp)
gdp=pd.to_numeric(gdp,errors="coerce")
np.random.seed(42)
idx=np.random.choice(gdp.index,size=int(0.2*len(gdp)),replace=False)
m=gdp.copy()
m.loc[idx]=np.nan
i=m.interpolate(method="linear")
print('\n\n',i)
plt.figure(figsize=(12,6))
plt.scatter(m.index,m.values,label="original GDP(with missing values)",marker="o")
plt.scatter(i.index,i.values,label="interpolated GDP",marker="*")
plt.title(f"GDP Trend for {country} (with missing & interpolated values)")
plt.xlabel("Year")
plt.ylabel("GDP")
plt.legend()
plt.show()
