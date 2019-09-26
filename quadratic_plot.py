from matplotlib import pylab as plt
import numpy as np


def f(x):
    A, B, C = -1.49674972e+01, 5.98259947e+04, -5.97805224e+07
    return A * x * x + B * x + C


def main():
    time = np.linspace(2002, 2014, 500)
    mass = f(time)
    plt.plot(time, mass)
    plt.show()


if __name__ == '__main__':
    main()
