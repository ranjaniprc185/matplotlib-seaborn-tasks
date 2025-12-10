import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("datasets/gdp_life_pop.csv")
d=df[df["Year"]==2007]
g=d["GDP_per_capita"]
l=d["Life_Expectancy"]
p=d["Population"]
c=d["Country"]
plt.figure(figsize=(12,6))
plt.scatter(g,l,s=p/1e6,alpha=0.5,edgecolor="w")
plt.xscale("log")
plt.xlabel("GDP per capita(log scale)")
plt.ylabel("life expectancy(years)")
plt.title("GDP per capita")
plt.show()
