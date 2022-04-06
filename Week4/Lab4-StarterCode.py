import numpy as np
import matplotlib.pyplot as plt

"""
COLE BARDIN
14422557

ASSIGNMENT: COMPLETE fsc and fs functions below
"""

"""
ECE 105: Programming for Engineers 2
Created September 7, 2020
Steven Weber
Fourier series solution

This code plots the Fourier series representation of periodic signals
"""

"""
COMPLETE:
fsc takes five arguments:
1) natural number n: term index in the Fourier series
2) function g: the basis function (np.sin or np.cos)
3) function f: the periodic function to be approximated
4) list x of values from [-pi,+pi]
5) float dx: the length between values of x in interval [-pi,+pi]

Return: integral of f(xe) * g(n * xe) / pi over interval [-pi,+pi]
Integral approx. by Riemann sum, using divisions of width dx

Steps:
1. return the sum of f(xe) * g(n * xe) / pi * dx over xe in x
"""
# Fourier series coefficient n for f using basis function g
def fsc(n, g, f, x, dx):
    # 1. integral: (1/pi) f(xe) g(n xe) dx over all xe in x
    return np.sum([f(xe)*g(n*xe) for xe in x]) * dx / np.pi


# compute Fourier series coefficients: a0, a, b
def fsc_all(N_max, f, x, dx):
    a0 = fsc(0, np.cos, f, x, dx)
    a = [fsc(n, np.cos, f, x, dx) for n in range(1,N_max+1)]
    b = [fsc(n, np.sin, f, x, dx) for n in range(1,N_max+1)]
    return a0, a, b

"""
COMPLETE:
fs takes five arguments:
1) x: the value of x at which the Fourier series is to be computed
2) a0: the "DC term" a_0
3) a: the list of a_n coefficients for n=1,..
4) b: the list of b_n coefficients for n=1,..
5) N: the number of terms n to be used in the representation

Return: sum of a0/2 + the sum of the a_n and b_n over n=1,..,N

Steps:
1. compute a_sum: sum of a[n-1] * np.cos(n x) over n=1,...N
2. compute b_sum: sum of b[n-1] * np.sin(n x) over n=1,...N
3. return the target sum

Challenge: code should be vectorized
If x is a vector, it should return a vector
Use np.sum for the sums in Steps 1 and 2
Read about the axis named argument for np.sum
"""
# Fourier series representation at x using N terms
def fs(x, a0, a, b, N):
    # 1. sum the a_n coefficients from 1 to N
    a_sum = np.sum([a[n-1]*np.cos(n*x) for n in range(1,N+1)], axis=0)
    pass
    # 2. sum the b_n coefficients from 1 to N
    b_sum = np.sum([b[n-1]*np.sin(n*x) for n in range(1,N+1)], axis=0)
    pass
    # 3. return the Fourier series approximation
    return (a0 / 2) + a_sum + b_sum

# plot_fsr: 4 subplots: f(x) and Fourier series using N1, N2, N3 terms
def plot_fsr(f, N1, N2, N3, x, dx, name, filename):
    # get all Fourier series coefficients
    a0, a, b = fsc_all(max(N1,N2,N3), f, x, dx)
    plt.figure()
    ay,(ax1,ax2,ax3,ax4)=plt.subplots(nrows=4, sharex=True)
    plt.tight_layout()
    ax1.plot(x, f(x))
    ax2.plot(x, fs(x, a0, a, b, N1))
    ax3.plot(x, fs(x, a0, a, b, N2))
    ax4.plot(x, fs(x, a0, a, b, N3))
    ax1.set_title('{}: f(x)'.format(name))
    ax2.set_title('{}: Fourier series, N = {}'.format(name, N1))
    ax3.set_title('{}: Fourier series, N = {}'.format(name, N2))
    ax4.set_title('{}: Fourier series, N = {}'.format(name, N3))
    plt.savefig(filename)

# sample periodic functions (signals)
def f_square(x): return np.where(x >= 0, 1, 0)
def f_triangle(x): return np.where(x >=0, -x, x)
def f_sawtooth(x): return x
def f_rectifier(x): return np.where(x >= 0, x, 0)

# main function
if __name__ == "__main__":
    # specify dx: the distance between x-values over [-pi,+pi]
    dx = 1/100
    # number of points in [-pi, +pi] using width dx
    m = int(2 * np.pi / dx)
    # list of m x-axis values in [-pi, +pi]
    x = np.linspace(-np.pi, np.pi, m)

    # specify the three values of N (# terms in series)
    N1, N2, N3 = 2, 20, 200
    # call plot_fsr with four different signals defined above
    plot_fsr(f_square, N1, N2, N3, x, dx, 'square','Lab4-FSR-Square.pdf')
    plot_fsr(f_triangle, N1, N2, N3, x, dx, 'triangle', 'Lab4-FSR-Triangle.pdf')
    plot_fsr(f_sawtooth, N1, N2, N3, x, dx, 'sawtooth', 'Lab4-FSR-Sawtooth.pdf')
    plot_fsr(f_rectifier, N1, N2, N3, x, dx, 'rectifier', 'Lab4-FSR-Rectifier.pdf')
