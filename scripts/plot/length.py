"""Module to show length distribution"""

import pandas as pd
import matplotlib.pyplot as plt


def distribution_length(data):
    """
    Generates and saves a histogram of the distribution of question lengths
    from the provided dataset.

    Args:
        data (pandas.DataFrame): A DataFrame containing a column named "question"
                                 with text data.

    Returns:
        None: The function saves the histogram as an image file
              in the "./figures/" directory with the name "distribution_length.jpeg".
    """
    questions = data["question"]
    questions = data.map(len)
    questions.hist()
    plt.savefig("./figures/distribution_length.jpeg")


tags = pd.read_csv("./data/preprocess/tags.csv")
distribution_length(tags)
