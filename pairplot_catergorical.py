import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = sns.load_dataset("tips")
pair_plot = sns.pairplot(data=data, hue="sex", palette="Blue")
