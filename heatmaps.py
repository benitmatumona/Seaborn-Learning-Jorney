import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset["dataset.csv"]


def adjust_style(figsize: tuple, str, contex: str, scale: float):
    plt.figure(figsize=figsize)
    sns.set_context(context=contex, font_scale=scale)

def main():
    adjust_style((8, 6), "paper", 1.4)
    matrix = data.corr()
    sns.heatmap(
        data=matrix, annot=True, cmap="blues", 
        linecolor="white", linewidths=1
        )


if __name__ == "__main__":
    main()