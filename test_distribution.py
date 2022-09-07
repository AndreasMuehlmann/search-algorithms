import os

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from writing import write_plot


def count_values_step(array, start_index, step, step_size):
    for count, value in enumerate(array[start_index:]):
        if not (step <= value < step + step_size):
            break
    return count


def main():

    array = np.random.uniform(size=1000)
    # array = np.random.normal(size=1000)
    # array = np.random.exponential(size=1000)

    array = np.sort(array)

    max_val = array[-1]
    min_val = array[0]
    step_size = (max_val - min_val) / 50
    max_val += 5 * step_size
    min_val -= 5 * step_size

    xs = []
    ys = []

    step = min_val
    index = 0
    while step < max_val:
        count = count_values_step(array, index, step, step_size)
        index += count

        step += step_size
        print(f'index: {index}, step: {step}')

        xs.append(step)
        ys.append(count)


    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = 'uniform.csv'
    file_path = os.path.join(current_dir, 'distributions', file_name)
    write_plot(xs, ys, file_path)

    '''
    sns.histplot(array)
    plt.show()
    '''


if __name__ == '__main__':
    main()
