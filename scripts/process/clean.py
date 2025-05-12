"""Module to clean the dataset from preprocessed one"""

import pandas as pd

dataset = pd.read_csv("./data/preprocess/tags.csv")
tags_set = list(set(dataset["tag"]))

dataset = dataset.rename(columns={"question": "text", "tag": "label"})

dataset["label"] = dataset["label"].apply(tags_set.index)

dataset.to_csv("./data/clean/dataset.csv", index=False)
