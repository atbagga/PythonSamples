import sys
from colorama import init, deinit

def _delete_last_line():
    "Use this function to delete the last line in the STDOUT"
    init()
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')
    deinit()

def delete_last_n_lines(n):
    "Use this function to delete the last 'n' lines in the STDOUT"
    for _x in range(0, n):
        _delete_last_line()


def print_a_line(x):
    print('This is some randome line ({})'.format(x))


def print_n_lines(x, n):
    for _x in range(0, n):
        print_a_line(x)


for i in range(100000):
    print("Performing op on line ({})".format(i))
    print_n_lines(i, 1)
    delete_last_n_lines(1)

