import os
from math import log2

from write_plot import write_3d_plot

def binary_multiple_search(a, b):
    if a == 0 or b == 0:
        return 0

    front_part = (2 * a - 1) * log2(b)

    '''
    front_part = 0
    for i in range(int(log2(a)) + 1):
        front_part += (2 ** i) * log2(b)
    '''

    back_part = (a * log2(a) + log2(a) - a + 1)
    # =
    # back_part = (2 * a - 1) * log2(b) - (2 - log2(a) * 2 ** (log2(a)) + (log2(a) - 1) * 2 ** (log2(a + 1)) + log2(a) * 2 ** (log2(a)))

    # back_part = 0
    # for i in range(int(log2(a)) + 1):
    #     back_part += i * 2 ** i

    return front_part - back_part


def binary_multiple_search_summation(a, b):
    if a == 0 or b == 0:
        return 0

    result = 0
    for i in range(int(log2(a)) + 1):
        addon = (2 ** i) * log2(b) - i * 2 ** i # log2(2 ** (i * 2 ** i))
        if not addon < 0:
            result += addon

    return round(result, 3)

def plot_3d_function(function, function_name):
    domain = [0, 1500]
    step_size = 50

    points = []

    for a in range(domain[0], domain[1], int(step_size / 2)):
        for b in range(domain[0], domain[1], step_size):
            point = [a, b, function(a, b)]
            points.append(point)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'functions', f'{function_name}.csv')
    write_3d_plot(points, file_path)


def main():
    plot_3d_function(binary_multiple_search_summation, "binary_multiple_search_summation")
    plot_3d_function(binary_multiple_search, "binary_multiple_search")


if __name__ == '__main__':
    main()
