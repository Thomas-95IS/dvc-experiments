import matplotlib
import matplotlib.pyplot as plt
import pandas as pd


mnist_df = pd.read_csv('data/train.csv')


def plot_digit(index):
    digit = mnist_df.iloc[index].values[1:].reshape(28, 28)
    print(digit)

    plt.imshow(digit, interpolation='nearest', cmap=matplotlib.cm.binary)
    return plt.show()
