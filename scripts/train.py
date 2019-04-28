import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier


mnist_df = pd.read_csv('data/train.csv')

print(mnist_df.shape)

mnist_df = mnist_df.dropna()

print(mnist_df.shape)

# mnist_labels = mnist_df['label']
# mnist_values = mnist_df[mnist_df.columns.tolist()[1:]]

# s = mnist_df['pixel4'].isna().sum()
# print (s)

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(mnist_df[mnist_df.columns.tolist()[1:]], mnist_df['label'])
