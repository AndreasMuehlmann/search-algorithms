import time

import numpy as np

from multiple_searches import linear_multiple_search, \
    multiple_value_search, binary_multiple_search


def main():
    numbers = np.round(np.sort(np.random.uniform(size=1000000)), decimals=3)
    searched_numbers = np.round(np.sort(np.random.uniform(size=100000)), decimals=3)

    start = time.time()
    results = linear_multiple_search(numbers, searched_numbers)
    print(time.time() - start)

    start = time.time()
    results = multiple_value_search(numbers, searched_numbers)
    print(time.time() - start)

    start = time.time()
    results = binary_multiple_search(numbers, searched_numbers)
    print(time.time() - start)
if __name__ == '__main__':
    main()
