# Project 1 FYS3150, Anders P. Åsbø
import pythonLibrary.computationalLib as cp
import numpy as np


def main():
    global N
    N = int(eval(input("Give value for N: ")))

    A = np.zeros((N, N))
    A = Afunc(A)

    solver = cp.pylib()


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
