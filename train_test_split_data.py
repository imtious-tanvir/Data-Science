import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model import train_test_split

X, y = make_classification(n_samples = 1000, n_features = 10, n_classes = 2, random_state = 42)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)

print(X_train)
