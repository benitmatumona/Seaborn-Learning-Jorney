import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset["dataset.csv"]


def main():
    
    print(
        "This program displays a boxplot age vs salary with any of the folowing below: \n",
        "customer_id \nexperience_years \ndepartment \n",
        "performance_score \nremote_work_days \nsatisfaction"
    )
    topics = input("which topic(s) would you like the graph to displayed? ").strip().lower()
    for topic in topics.split():
        try:
            sns.boxplot(x="age", y="salary", data=data, hue=topic)
        except Exception as e:
            print(f"Invalid input {topic}")


if __name__ == "__main__":
    main()