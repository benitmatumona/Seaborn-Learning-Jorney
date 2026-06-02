import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset["dataset.csv"]


def main():
    try:
        print(
            "This program displays a joint plot of any of the folowing below: \n",
            "customer_id \nage \nsalary \nexperience_years \ndepartment \n",
            "performance_score \nremote_work_days \nsatisfaction"
        )
        kind = input("which type of graph would you like to be displayed? ").strip().lower()
        sns.jointplot(x="experience_years", y="salary", data=data, kind=kind)
    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()