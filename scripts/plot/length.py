import pandas as pd
import matplotlib.pyplot as plt

# Visualisations :
# - distribution longueur des prompts
# - distribution des labels (ordonnée)


def distribution_length(data):
    questions = data["question"]
    questions = data.map(lambda a: len(a))
    fig = questions.hist()
    plt.savefig("./figures/distribution_length.jpeg")

tags = pd.read_csv("./data/preprocess/tags.csv")
distribution_length(tags)
