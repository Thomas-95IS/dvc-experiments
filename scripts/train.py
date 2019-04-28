import pickle

import numpy as np
import pandas as pd
from sklearn.linear_model import SGDClassifier


mnist_df = pd.read_csv('data/cleaned_train.csv')

sgd_clf = SGDClassifier(random_state=42)
sgd_clf.fit(mnist_df[mnist_df.columns.tolist()[1:]], mnist_df['label'])


with open('data/model.pkl', 'wb') as model_file:
    pickle.dump(sgd_clf, model_file)

model_file.close()
