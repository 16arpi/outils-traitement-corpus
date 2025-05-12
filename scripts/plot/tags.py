import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import math

def distribution_tags(data):
    tags = data["tag"]
    counts = tags.value_counts().sort_values(ascending=False)
    counts.plot(kind='bar', xticks=[])
    # plt.yscale("log")
    plt.savefig("./figures/distribution_tags.jpeg")

tags = pd.read_csv("./data/preprocess/tags.csv")
distribution_tags(tags)
