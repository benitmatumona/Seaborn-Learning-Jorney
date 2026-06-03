import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("darkgrid")
plt.figure(figsize=(8, 4))
sns.set_context("notebook", font_scale=2)
pair_plot = sns.pairplot(sns.load_dataset["dataset.csv"])