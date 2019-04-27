import pandas as pd


mnist_df = pd.read_csv('data/train.csv')
mnist_df = mnist_df.dropna()
mnist_df.to_csv('data/cleaned_train.csv')
