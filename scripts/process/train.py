"""Module to fine-tune a BERT model. Content taken from HuggingFace documentation. """

import evaluate
import numpy as np

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
)
from datasets import load_dataset

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
metric = evaluate.load("accuracy")


def tokenize(examples):
    """
    Tokenizes the input examples using the specified tokenizer.

    Args:
        examples (dict): A dictionary containing the input data.
                         It is expected to have a key "text" with the text to be tokenized.

    Returns:
        dict: A dictionary containing the tokenized output with padding set to "max_length"
              and truncation enabled.
    """
    return tokenizer(examples["text"], padding="max_length", truncation=True)


def compute_metrics(eval_pred):
    """
    Compute evaluation metrics for model predictions.

    Args:
        eval_pred (tuple): A tuple containing two elements:
            - logits (numpy.ndarray): The raw prediction scores or logits output by the model.
            - labels (numpy.ndarray): The ground truth labels corresponding to the predictions.

    Returns:
        dict: A dictionary containing the computed evaluation metrics, as returned by the `metric.compute` function.
    """
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


dataset = load_dataset("csv", data_files="./data/clean/dataset.csv")
dataset = dataset["train"].train_test_split(test_size=0.2)

dataset = dataset.map(tokenize, batched=True)
model = AutoModelForSequenceClassification.from_pretrained(
    "google-bert/bert-base-cased", num_labels=120
)

training_args = TrainingArguments(
    output_dir="./model/stackoverflow",
    eval_strategy="epoch",
    push_to_hub=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    compute_metrics=compute_metrics,
)
trainer.train()
