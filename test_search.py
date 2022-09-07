import time
import os

import numpy as np

from searches import linear_search, \
binary_search, interpolation_search, interpolated_binary_search

from writing import write_search_times


def create_random_test(length, distribution_method):
    numbers = distribution_method(size=length)
    sorted_numbers = np.sort(numbers)
    return sorted_numbers


def time_seach(search_method, numbers, searched):
    start = time.time()
    search_method(numbers, searched)
    return time.time() - start


def avg_time_search(length_numbers, length_searched, search_method, distribution_method):
    new_numbers = 2
    searches_per_number = 100

    results = []
    for new_number in range(new_numbers):
        numbers = create_random_test(length_numbers, distribution_method)
        for search_per_number in range(searches_per_number):
            if numbers.any():
                number = np.random.uniform(numbers[0], numbers[-1], size=length_searched)
            else:
                number = 0

            time = time_seach(search_method, numbers, number)
            results.append(time)

    avg_time = np.mean(results)
    print(f'length_numbers: {length_numbers}, avg_time: {round(time * 10**6, 5)}')
    return avg_time


def test_searches(searches):
    for search in searches:
        search_times = [avg_time_search(length, search['search_method'],
                                        search['distribution_method']) for search_method in lengths['value']]

        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = f'{search["name"]}_{distribution["name"]}_{lengths["name"]}.csv'
        file_path = os.path.join(current_dir, 'times', file_name)
        write_search_times(search_times, lengths['value'], file_path)


def main():
    start = time.time()
    while True:
        if time.time() - start > 5:
            break

    small_number_range = range(5, 501, 1)
    large_number_range = range(50000, 3000001, 50000)
    searches = [
        {'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
         'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
         'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
         'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
        {'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
         'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
         'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
         'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},

        {'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
         'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
         'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
         'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
        {'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
         'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
         'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
         'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},

        {'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
         'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
         'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
         'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
        {'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
         'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
         'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
         'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},

        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
    ]

    test_searches()

if __name__ == '__main__':
    main()
