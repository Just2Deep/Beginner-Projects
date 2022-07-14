# Visualize Linear Relationship using Python

import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/Instagram.csv", encoding='latin1')
data = data.dropna()

# print(data.head())


plt.figure(figsize=(10, 8))
plt.style.use('fivethirtyeight')
plt.title("Relationship Bewtween Likes & Impressions")
sns.regplot(x="Impressions", y="Likes", data=data)
plt.show()
