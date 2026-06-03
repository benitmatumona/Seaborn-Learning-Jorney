import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def adjust_style(figsize: tuple, style: str, contex: str):
    plt.figure(figsize=figsize)
    sns.set_style(style=style)
    sns.set_context(context=contex)

def main():
    adjust_style((8, 5), "white", "talk")
    data = sns.load_dataset["dataset.csv"]

    print(
        "This program displays a stripplot age vs salary with",
        "any of the folowing below: \n",
        "customer_id \nexperience_years \ndepartment \n",
        "performance_score \nremote_work_days \nsatisfaction"
    )
    topics = input("which topic(s) would you like the graph to displayed? "
                   ).strip().lower()
    for topic in topics.split():
        try:
            sns.stripplot(
                x="age", y="salary", data=data, 
                hue=topic, jitter=True, palette="blues"
                )
        except Exception as e:
            print(f"Invalid input {topic}")


if __name__ == "__main__":
    main()