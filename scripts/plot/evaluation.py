"""Module to give some evaluation metrics to the model"""

import pandas as pd
import matplotlib.pyplot as plt

from datasets import load_dataset
from transformers import AutoTokenizer
from transformers.pipelines import pipeline
from sklearn.metrics import classification_report

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")


def inference(pipe, x_test):
    """
    Perform inference on a list of test inputs using a given pipeline.

    Args:
        pipe (Callable): A callable pipeline (e.g., a machine learning model or NLP pipeline)
                         that processes an input and returns a list of dictionaries with
                         inference results. Each dictionary is expected to have a "label" key.
        X_test (Iterable): An iterable of test inputs to be processed by the pipeline.

    Yields:
        int: The processed label for each input in X_test, converted to an integer by
             removing the "LABEL_" prefix from the label string.
    """
    for x in x_test:
        result = pipe(x)
        label = result[0]["label"]
        label = int(label.replace("LABEL_", ""))
        print(label)
        yield label


def training():
    """
    Reads evaluation metrics from a CSV file, plots the metrics, and saves the plot as an image.

    The function performs the following steps:
    1. Reads a CSV file located at './data/evaluation/metrics.csv' containing evaluation metrics.
    2. Plots the metrics with x-axis ticks ranging from 0 to 9.
    3. Saves the resulting plot as a JPEG image in the './figures/'
       directory with the filename 'metrics.jpeg'.

    Note:
    - Ensure that the required CSV file exists at the specified path before calling this function.
    - The './figures/' directory must exist, or the function will raise an error
      when attempting to save the plot.

    Dependencies:
    - pandas (imported as pd)
    - matplotlib.pyplot (imported as plt)
    """
    in_metrics = pd.read_csv("./data/evaluation/metrics.csv")
    in_metrics.plot(xticks=range(0, 10))
    plt.savefig("./figures/metrics.jpeg")


def metrics():
    """
    Evaluate the performance of a text classification model on a test dataset.

    This function loads a dataset from a CSV file, splits it into training and
    testing sets, and evaluates a pre-trained text classification model on the
    test set. It prints a classification report comparing the true labels with
    the predicted labels.

    Steps:
    1. Load the dataset from a CSV file.
    2. Split the dataset into training and testing sets.
    3. Convert the test set into a pandas DataFrame.
    4. Use a pre-trained text classification pipeline to predict labels for the test set.
    5. Print a classification report comparing the true and predicted labels.

    Note:
    - The dataset is expected to have a "label" column for true labels and a
      "text" column for the input text.
    - The model used is "16arpi/stackoverflow", and the tokenizer must be
      defined elsewhere in the code.

    Raises:
        KeyError: If the dataset does not contain the required "label" or "text" columns.
        ValueError: If the dataset file path is incorrect or the model pipeline fails.

    """
    dataset = load_dataset("csv", data_files="./data/clean/dataset.csv")
    dataset = dataset["train"].train_test_split(test_size=0.2)
    dataset = pd.DataFrame(dataset["test"])

    y_real = dataset["label"]
    pipe = pipeline(
        "text-classification", model="16arpi/stackoverflow", tokenizer=tokenizer
    )
    y_pred = list(inference(pipe, dataset["text"]))

    print(classification_report(y_real, y_pred))


metrics()
