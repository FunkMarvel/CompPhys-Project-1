# Project 1 FYS3150, Anders P. Åsbø
import pythonLibrary.computationalLib as cp
import data_generator as gen
import numpy as np
import timeit as time
import matplotlib.pyplot as plt
import os

dir = os.path.dirname(os.path.realpath(__file__))


def main():
    global N
    N = int(eval(input("Give value for N: ")))
    name = "LUtest%i" % N

    x = np.linspace(0, 1, N)
    h = (x[-1]-x[0])/N
    gen.generate_data(x, name)
    b = np.loadtxt("%s/data_files/%s.dat" % (dir, name))*h**2

    A = np.zeros((N, N))
    A = Afunc(A)

    solver = cp.pylib()
    start = time.default_timer()
    LU, a, d = solver.luDecomp(A)
    b = solver.luBackSubst(LU, a, b)
    end = time.default_timer()
    print("Time spent on LU %g" % (end-start))

    plt.figure()
    plt.plot(x, b)
    plt.show()


def Afunc(A):
    """Function that populates tridiagonal matrix."""
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i, j] = 2
            elif i == j+1:
                A[i, j] = -1
            elif j == i+1:
                A[i, j] = -1

    return A


if __name__ == '__main__':
    main()
