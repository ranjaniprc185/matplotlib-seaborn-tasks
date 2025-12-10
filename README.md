# matplotlib-seaborn-tasks
This repository contains data visualization projects using Python libraries:
Matplotlib and Seaborn.

Task 1: 
Using the World Bank’s World Development Indicators dataset (wdi.csv):

1. Extract the annual GDP values for a specific country (e.g., India).
2️. Randomly delete 20% of GDP entries to simulate missing values.
3️. Fill missing values using linear interpolation.
4️. Plot two line charts on the same graph:
Original GDP values (with missing points)
Interpolated GDP values
Goal → Compare the GDP trend before and after interpolation

Skills Demonstrated:
Handling missing data
Interpolation
Line plot visualization

Files:
task1_gdp_interpolation.py
Dataset: datasets/wdi.csv
Output: outputs/task1_output.png



Task 2: GDP vs Life Expectancy Scatter Plot

Using gdp_life_pop.csv:
1.Filter data for year 2007
2.x-axis → GDP per capita (log scale)
3.y-axis → Life expectancy
4.Bubble size → population
5.Add labels, legend, and title
Goal → Understand how wealth relates to life expectancy

Skills Demonstrated:
Data filtering
Scatter plot
Bubble sizing & log scale

Files:
task2_scatter_plot.py
Dataset: datasets/gdp_life_pop.csv
Output: outputs/task2_output.png



Task 3: Efficient Tipping Day

Using tips.csv:
1.Calculate tip percentage = (tip / total bill) × 100
2.Group by day
3.Determine which day has the highest average tip percentage
4.Plot a chart showing average tip % by day
Goal → Identify the most efficient tipping day

Skills Demonstrated:
Grouping & aggregation
Custom calculated columns
Bar chart visualization

Files:
task3_tip_behavior.py
Dataset: datasets/tips.csv
Output: outputs/task3_output.png



Task 4: Penguin Body Mass Heatmap

Using Seaborn’s penguins dataset:

1.Group by species and island
2.Find mean body mass (g)
3.Create a heatmap to represent the values
Goal → Compare body mass differences visually across islands & species

Skills Demonstrated:
Seaborn heatmap
Data aggregation
Color-mapping visual analytics

Files:
task4_penguin_heatmap.py
Dataset: Loaded from Seaborn (sns.load_dataset("penguins"))
Output: outputs/task4_output.png



Task 5: Global Video Game Sales by Platform

Using vgsales.csv:
1.Group by platform
2.Calculate total global sales
3.Create a bar plot showing sales by platform
Goal → Identify highest-earning gaming platforms

Skills Demonstrated:
Grouping by category
Bar chart visualization

Files:
task5_game_sales.py
Dataset: datasets/vgsales.csv
Output: outputs/task5_output.png
