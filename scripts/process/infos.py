"""Module printing the number of tags in the dataset"""

import pandas as pd

tags = pd.read_csv("./data/preprocess/tags.csv")
tags = tags["tag"]
counts = tags.value_counts()
print(counts)
