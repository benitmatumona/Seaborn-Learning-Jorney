import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = sns.load_dataset("tips")

grid = sns.FacetGrid(data=data, col="time", row="smoker")

grid.map(plt.scatter, "total_bill", bin=8)
# grid.add_legend()