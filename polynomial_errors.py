import math
import numpy as np
import pandas as pd
from scipy import interpolate, poly1d
import matplotlib.pyplot as plt
import warnings
 
 
def rmse(targets, predictions):
    return np.sqrt(((targets - predictions) ** 2).mean())
   
 
def model(xs, ys, n=3):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', np.RankWarning)
        coefficients = np.polyfit(xs, ys, n)
        polynomial = poly1d(coefficients)
        return polynomial(xs)


def main():
    df = pd.read_csv('greenland-mass-change.csv')
    train = df[df['year'] < 2012]
    test  = df[df['year'] >= 2012]
    train_xs = train['year']
    train_ys = train['mass change']
    test_xs  = test['year']
    test_ys  = test['mass change']
 
    diffs = [rmse(train_ys, model(train_xs, train_ys, n))
             for n in range(1, 41)]
    plt.plot(range(1, 41), diffs, '.')
   
    plt.title('Error by polynomial degrees')
    plt.xlabel('Degrees')
    plt.ylabel('Error')
    plt.grid(True)
    plt.gca().set_xlim(0)
    plt.savefig('polynomial_errors.png')
    plt.show()
 
 
if __name__ == '__main__':
    main()

