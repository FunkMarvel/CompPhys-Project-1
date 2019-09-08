# create data set for numerical testing
import numpy as np


def main():
    """Generates test data if run as stand-alone program."""
    x = np.linspace(0, 1, 1001)
    test_name = "Test_data"
    generate_data(x, test_name)


def generate_data(x, name):
    """Function that generates a set of u''(x) data, as well as the
    corresponding, analytical u(x). The data is saved to text"""
    data = 100*np.exp(-10*x)
    np.savetxt("%s.dat" % name, data, fmt="%f")

    analytical_solution = 1-(1-np.exp(-10))*x-np.exp(-10*x)
    anal_name = "analytical_solution_for_%s.dat" % name
    np.savetxt(anal_name, analytical_solution)


if __name__ == '__main__':
    main()
