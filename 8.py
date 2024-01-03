import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset
iris_dataset = load_iris()

# Display the iris dataset
print("\nIRIS FEATURES TARGET NAMES:\n", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print("\n[{0}]:[{1}]".format(i, iris_dataset.target_names[i]))

print("\nIRIS DATA:\n", iris_dataset["data"])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"], random_state=0)

# Display train and test data
print("\nTRAINING DATA:\n", X_train)
print("\nTESTING DATA:\n", X_test)
print("\nTRAINING TARGETS:\n", y_train)
print("\nTESTING TARGETS:\n", y_test)

# Train the model
kn = KNeighborsClassifier(n_neighbors=5)
kn.fit(X_train, y_train)

# Predicting a sample value
x_new = np.array([[5, 2.9, 1, 0.2]])
prediction = kn.predict(x_new)
print("\nPredicted target value:", iris_dataset["target_names"][prediction][0])

# Predictions and evaluation on test set
predictions = kn.predict(X_test)
for i in range(len(X_test)):
    print("\nActual: {0} {1}, Predicted: {2} {3}".format(
        y_test[i], iris_dataset["target_names"][y_test[i]], predictions[i], iris_dataset["target_names"][predictions[i]]
    ))
print("\nTest Score (Accuracy): {:.2f}\n".format(kn.score(X_test, y_test)))
