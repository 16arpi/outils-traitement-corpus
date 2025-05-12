import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
import evaluate
import numpy as np
from datasets import load_dataset

tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-cased")
metric = evaluate.load("accuracy")

def tokenize(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    # convert the logits to their predicted class
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)

dataset = load_dataset("csv", data_files="./data/clean/dataset.csv")
dataset = dataset["train"].train_test_split(test_size=0.2)

dataset = dataset.map(tokenize, batched=True)
model = AutoModelForSequenceClassification.from_pretrained("google-bert/bert-base-cased", num_labels=120)

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
