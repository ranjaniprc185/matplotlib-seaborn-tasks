import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
penguins = sns.load_dataset("penguins")
pivot_data = penguin.pivot_table(values='body_mass_g',index='species',columns='island',
                                  aggfunc='mean')
plt.figure(figsize=(8,5))
sns.heatmap(pivot_data, annot=True)
plt.title("Average Body Mass (g) by Penguin Species & Island")
plt.show()
