import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex", data=data, markers=["o", "^"],
           scatter_kws={"s": 100, "linewidth": 0.5, "edgecolor": "w"},
           height=8, aspect=0.8)

# sns.lmplot(x="total_bill", y="tip", col="sex", row="time", markers=["o", "^"],
#            scatter_kws={"s": 100, "linewidth": 0.5, "edgecolor": "w"})