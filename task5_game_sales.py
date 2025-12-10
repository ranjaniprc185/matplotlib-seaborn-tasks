import pandas as pd
import matplotlib.pyplot as plt
vg = pd.read_csv("datasets/vgsales.csv")
sales_by_platform = vg.groupby("Platform")["Global_Sales"].sum().sort_values(ascending=False)
print(sales_by_platform)
plt.figure(figsize=(10,6))
sales_by_platform.plot(kind='bar')
plt.title("Total Global Sales by Platform")
plt.xlabel("Platform")
plt.ylabel("Global Sales (in Millions)")
plt.show()
