import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = sns.load_dataset("tips")
grid = sns.PairGrid(data=data, hue="sex", palette="Blue")
grid.map(plt.scatter)
grid.map_offdiag(plt.hist)
grid.map_upper(sns.kdeplot)
grid.map_lower(plt.stackplot)

grid2 = sns.PairGrid(data=data, hue="sex",
                     x_vars=["experience_years", "department"],
                     y_vars=["salary", "salary"]
                     )

# grid.map(plt.scatter)
# grid.add_legend()