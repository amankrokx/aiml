import csv
import math


class Node:
    def __init__(self, attribute):
        self.attribute = attribute
        self.children = []
        self.answer = ""

def load_csv(filename):
    with open(filename, 'r') as file:
        dataset = list(csv.reader(file))
        headers = dataset.pop(0)
    return dataset, headers

def subtables(data, col, delete):
    coldata = [row[col] for row in data]
    attr = list(set(coldata))
    dic = {val: [row[:] for row in data if row[col] == val] for val in attr}
    if delete:
        for rows in dic.values():
            for row in rows:
                del row[col]
    return attr, dic

def entropy(S):
    attr = list(set(S))
    if len(attr) == 1:
        return 0
    counts = [S.count(a) / len(S) for a in attr]
    return -sum(cnt * math.log(cnt, 2) for cnt in counts)

def compute_gain(data, col):
    attr, dic = subtables(data, col, delete=False)
    total_size = len(data)
    entropies = [entropy([row[-1] for row in dic[a]]) for a in attr]
    total_entropy = entropy([row[-1] for row in data])
    total_entropy -= sum((len(dic[val]) / total_size) * ent for val, ent in zip(attr, entropies))
    return total_entropy

def build_tree(data, features):
    lastcol = [row[-1] for row in data]
    if len(set(lastcol)) == 1:
        node = Node("")
        node.answer = lastcol[0]
        return node
    gains = [compute_gain(data, col) for col in range(len(data[0]) - 1)]
    split = gains.index(max(gains))
    node = Node(features[split])
    fea = features[:split] + features[split + 1:]
    attr, dic = subtables(data, split, delete=True)
    for a in attr:
        child = build_tree(dic[a], fea)
        node.children.append((a, child))
    return node

def print_tree(node, level):
    if node.answer != "":
        print(" " * level, node.answer)
        return
    print(" " * level, node.attribute)
    for value, n in node.children:
        print(" " * (level + 1), value)
        print_tree(n, level + 2)

def classify(node, x_test, features):
    if node.answer != "":
        print(node.answer)
        return
    pos = features.index(node.attribute)
    for value, n in node.children:
        if x_test[pos] == value:
            classify(n, x_test, features)

dataset, features = load_csv("4_train.csv")
node1 = build_tree(dataset, features)
print("The decision tree for the dataset using ID3 algorithm is")
print_tree(node1, 0)
testdata, features = load_csv("4_test.csv")
for xtest in testdata:
    print("The test instance:", xtest)
    print("The label for test instance:", end=" ")
    classify(node1, xtest, features)
