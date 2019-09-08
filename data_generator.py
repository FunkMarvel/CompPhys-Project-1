# create data set for numerical testing
import numpy as np
import os

dir = os.path.dirname(os.path.realpath(__file__))


def main():
    test_generate_data()
    test_generate_tridiagonal()


def generate_data(x, name):
    """Function that generates a set of u''(x) data, as well as the
    corresponding, analytical u(x). The data is saved to text"""
    data = 100*np.exp(-10*x)
    path = "%s/data_files/%s.dat" % (dir, name)
    np.savetxt(path, data, fmt="%f")

    x_prime = np.linspace(x[0], x[-1], 1000)
    analytical_solution = 1-(1-np.exp(-10))*x_prime-np.exp(-10*x_prime)
    anal_name = "%s/data_files/anal_solution_for_%s.dat" % (dir, name)
    np.savetxt(anal_name, analytical_solution, fmt="%f")


def generate_tridiagonal(N):
    """Function that generates a Nx3 array with each column corresponding to
    the non-zero elements in a tridiagonal matrix.
    "b" (mat_data[:,0]) is the lower diagonal,
    "d" (mat_data[:,1]) is the diagonal,
    and "a" (mat_data[:,2]) is the upper diagonal."""
    mat_data = np.random.randint(1, 100, size=(N, 3))
    np.savetxt("b-d-a_tridiagonal.dat", mat_data, fmt="%f")


def test_generate_data():
    """Generates test data if run as stand-alone program."""
    x = np.linspace(0, 1, 1001)
    test_name = "Test_data"
    generate_data(x, test_name)


def test_generate_tridiagonal():
    """Generates test data for tridiagonal."""
    generate_tridiagonal(100)
    print(np.loadtxt("b-d-a_tridiagonal.dat"))


if __name__ == '__main__':
    main()
