import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset
from transformers import AutoModel, AutoTokenizer
from transformers.pipelines import pipeline
from sklearn.metrics import classification_report

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")


def inference(pipe, X_test):
    for x in X_test:
        result = pipe(x)
        label = result[0]["label"]
        label = int(label.replace("LABEL_", ""))
        print(label)
        yield label


def training():
    metrics = pd.read_csv("./data/evaluation/metrics.csv")
    metrics.plot(xticks=range(0, 10))
    plt.savefig("./figures/metrics.jpeg")


def metrics():
    dataset = load_dataset("csv", data_files="./data/clean/dataset.csv")
    dataset = dataset["train"].train_test_split(test_size=0.2)
    dataset = pd.DataFrame(dataset["test"])

    y_real = dataset["label"]
    pipe = pipeline(
        "text-classification", model="16arpi/stackoverflow", tokenizer=tokenizer
    )
    y_pred = [a for a in inference(pipe, dataset["text"])]

    print(classification_report(y_real, y_pred))


metrics()
