"""Module to show tags distribution"""

import pandas as pd
import matplotlib.pyplot as plt


def distribution_tags(data):
    """
    Generates a bar plot showing the distribution of tags in the given dataset.

    Parameters:
    data (pandas.DataFrame): A DataFrame containing a column named "tag"
                             which holds the tags to be analyzed.

    Behavior:
    - Counts the occurrences of each unique tag in the "tag" column.
    - Sorts the counts in descending order.
    - Plots the distribution as a bar chart without x-axis tick labels.
    - Saves the plot as a JPEG image in the "./figures/"
      directory with the filename "distribution_tags.jpeg".

    Note:
    - Ensure that the "tag" column exists in the input DataFrame.
    - The "./figures/" directory must exist, or the function will
      raise an error when saving the plot.
    """
    in_tags = data["tag"]
    counts = in_tags.value_counts().sort_values(ascending=False)
    counts.plot(kind="bar", xticks=[])
    plt.savefig("./figures/distribution_tags.jpeg")


tags = pd.read_csv("./data/preprocess/tags.csv")
distribution_tags(tags)
