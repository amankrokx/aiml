import csv
import math
import random


def load_csv(filename):
    with open(filename, "r") as file:
        lines = csv.reader(file)
        dataset = [list(map(float, line)) for line in lines]
    return dataset

def split_dataset(dataset, split_ratio):
    train_size = int(len(dataset) * split_ratio)
    random.shuffle(dataset)
    return dataset[:train_size], dataset[train_size:]

def mean(numbers):
    return sum(numbers) / len(numbers)

def stdev(numbers):
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

def summarize_by_class(dataset):
    separated = {}
    for vector in dataset:
        class_value = vector[-1]
        if class_value not in separated:
            separated[class_value] = []
        separated[class_value].append(vector)
    summaries = {class_value: [(mean(attribute), stdev(attribute)) for attribute in zip(*instances)][:-1]
                 for class_value, instances in separated.items()}
    return summaries

def calculate_probability(x, mean, stdev):
    exponent = math.exp(-((x - mean) ** 2) / (2 * (stdev ** 2)))
    return (1 / ((2 * math.pi) ** (1 / 2) * stdev)) * exponent

def predict(summaries, input_vector):
    probabilities = {class_value: 1 for class_value in summaries}
    for class_value, class_summaries in summaries.items():
        for i, (mean_val, stdev_val) in enumerate(class_summaries):
            x = input_vector[i]
            probabilities[class_value] *= calculate_probability(x, mean_val, stdev_val)
    return max(probabilities, key=probabilities.get)

def get_predictions(summaries, test_set):
    return [predict(summaries, test_vector) for test_vector in test_set]

def get_accuracy(test_set, predictions):
    correct = sum(1 for i in range(len(test_set)) if test_set[i][-1] == predictions[i])
    return (correct / len(test_set)) * 100.0

filename = '6.csv'
split_ratio = 0.67
dataset = load_csv(filename)
training_set, test_set = split_dataset(dataset, split_ratio)
summaries = summarize_by_class(training_set)
predictions = get_predictions(summaries, test_set)
print("\nPredictions:\n", predictions)
accuracy = get_accuracy(test_set, predictions)
print("Accuracy:", accuracy)
