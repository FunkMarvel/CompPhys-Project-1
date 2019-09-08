# Project 1 FYS3150, Anders P. Åsbø
import data_generator as gen
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Specify number of data points N: "))
name = input("Name of data-set without file extension: ")

x = np.linspace(0, 1, N)  # array of normalized positions.
h = (x[0]-x[-1])/N  # defining step-siz.

gen.generate_data(x, name)  # generating data set.
anal_sol = np.loadtxt("analytical_solution_for_%s.dat" % name)

u = np.empty(N)  # array for unkown values.
d = np.full(N, 2)  # array for diagonal elements.
d_prime = np.empty(N)  # array for diagonal after decom. and sub.
a = np.full(N-1, -1)  # array for upper, off-center diagonal.
b = np.full(N-1, -1)  # array for lower, off-center diagonal.
g = np.loadtxt("%s.dat" % name)*h**2  # array for g in matrix eq. Au=g.
g_prime = np.empty(N)  # array for g after decomp. and sub.


def main():
    decomp_and_forward_sub()
    backward_sub()


def decomp_and_forward_sub():
    """Function that performs the matrix decomposition and forward
    substitution."""
    d_prime[0] = d[0]
    g_prime[0] = g[0]
    for i in range(1, len(u)):
        d_prime[i] = d[i] - b[i-1]*a[i-1]/d_prime[i-1]
        g_prime[i] = g[i] - b[i-1]*g_prime[i-1]/d_prime[i-1]


def backward_sub():
    """Function that performs the backward substitution."""
    u[0], u[-1] = 0, 0
    for i in reversed(range(1, len(u)-1)):
        u[i] = (g_prime[i]-a[i]*u[i+1])/d_prime[i]


def plot_solutions():
    pass


if __name__ == '__main__':
    main()
