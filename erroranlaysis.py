# Project 1 FYS3150, Anders P. Åsbø.
import numpy as np
import os
import matplotlib as plt


def main():
    """This program calculates the log10 of the relative error for
    different data sets generated with "project_specialized.py", and saves
    it in a textfile table with the log10 of the step-size."""

    dir = os.path.dirname(os.path.realpath(__file__))
    # preping arrays:
    N = np.array([10, 100, 1000, 10000, 100000, 1000000, 10000000])
    h = np.empty(len(N))
    epsilon = np.empty(len(N))

    for i in range(len(N)):  # reading data:
        u_num = np.loadtxt("%s/data_files/test%i.dat" % (dir, 1+i))
        u_anal = np.loadtxt("%s/data_files/anal_solution_for_test%i.dat"
                            % (dir, 1+i))

        h[i] = np.log10(1/len(u_num))  # calculating log 10 of step-size.

        # calculating log10 of relative error:
        err = np.abs((u_num[1:-2]-u_anal[1:-2])/u_anal[1:-2])
        epsilon[i] = np.max(np.log10(err))

    # storing the results
    table = np.empty((len(N), 2))
    table[:, 0] = h
    table[:, 1] = epsilon
    np.savetxt("%s/data_files/error_table.dat" % dir, table, fmt="%f")


if __name__ == '__main__':
    main()

# example run:
"""
$ python3 erroranlaysis.py
erroranlaysis.py:17: RuntimeWarning: divide by zero encountered in log10
  epsilon[i] = np.max(np.log10(err))
erroranlaysis.py:16: RuntimeWarning: divide by zero encountered in true_divide
  err = np.abs((u_num[1:-2]-u_anal[1:-2])/u_anal[1:-2])
"""