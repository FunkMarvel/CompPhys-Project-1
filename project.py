# Project 1 FYS3150, Anders P. Åsbø
from numba import jit
from data_generator import generate_data
import sys
import numpy as np
import matplotlib.pyplot as plt

N = int(input("Specify number of data points N: "))
name = input("Name of data-set without file extension: ")

x = np.linspace(0, 1, N)  # array of normalized positions.
generate_data(x, name)  # generating data set.
h = (x[-1]-x[0])/N  # defining step-siz.

u = np.empty(N-2)  # array for unkown values.
d = np.empty(N-2)  # array for diagonal elements.
d_prime = np.empty(N-2)  # array for diagonal after decom. and sub.
a = np.empty(N-3)  # array for upper, off-center diagonal.
b = np.empty(N-3)  # array for lower, off-center diagonal.
g = np.fromfile("%s.dat" % name)  # array for g in matrix eq. Au=g.
g_prime = np.empty(N)  # array for g after decomp. and sub.


def main():
    pass


@jit(nopython=True)
def decomp_and_forward_sub():
    """Function that performs the matrix decomposition and forward
    substitution."""
    for i in range(len(u)):
        d_prime[i] = d[i] - b[i-1]*a[i-1]/d_prime[i-1]
        g_prime[i] = g[i] - b[i-1]*g[i-1]/d_prime[i-1]


@jit(nopython=True)
def backward_sub():
    """Function that performs the backward substitution."""
    for i in range(len(u)):
        u[-i] = (g_prime[-i]-a[-i]*u[-(i+1)])/d_prime[-i]


if __name__ == '__main__':
    main()
