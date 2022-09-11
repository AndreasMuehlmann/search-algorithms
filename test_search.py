import time
import os

import numpy as np

from searches import linear_search, \
binary_search, interpolation_search, interpolated_binary_search

from multiple_searches import linear_multiple_search, multiple_value_search, binary_multiple_search

from write_plot import write_3d_plot


def create_random_test(length, distribution_method):
    numbers = distribution_method(size=length)
    sorted_numbers = np.sort(numbers)
    return sorted_numbers


def time_seach(search_method, numbers, searched_numbers):
    start = time.time()
    search_method(numbers, searched_numbers)
    return time.time() - start


def avg_time_search(length_numbers, length_searched, search_method, distribution_method):
    new_numbers = 2
    searches_per_number = 100

    results = []
    for new_number in range(new_numbers):
        numbers = create_random_test(length_numbers, distribution_method)
        for search_per_number in range(searches_per_number):
            if numbers.any():
                searched_numbers = np.random.uniform(numbers[0], numbers[-1], size=length_searched)
                searched_numbers = np.sort(searched_numbers)
            else:
                searched_numbers = 0

            time = time_seach(search_method, numbers, searched_numbers)
            results.append(time)

    avg_time = np.mean(results)
    mikro_avg_time = round(np.mean(results) * 10**6, 5)
    print(f'length_numbers: {length_numbers}, avg_time: {mikro_avg_time}')
    return mikro_avg_time


def test_search(search):
    points = []
    for length in search['range']:
        for length_searched in search['input_range']:
            search_time = avg_time_search(length, length_searched, search['search_method'],
                                          search['distribution_method'])
            point = [length_searched, length, search_time]
            points.append(point)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'times', f'{search["name"]}.csv')
    write_3d_plot(points, file_path)


def main():
    start = time.time()
    while True:
        if time.time() - start > 5:
            break

    small_number_range = range(5, 501, 1)
    large_number_range = range(50000, 3000001, 50000)
    searches = [
       #{'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
       # 'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
       #{'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
       # 'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
       #{'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
       # 'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
       #{'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
       # 'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
       #{'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
       # 'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
       #{'name': 'interpolated_binary_search_uniform_small_numbers', 'search_method': interpolated_binary_search,
       # 'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
       #
       #{'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
       # 'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
       #{'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
       # 'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
       #{'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
       # 'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
       #{'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
       # 'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
       #{'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
       # 'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
       #{'name': 'interpolation_search_uniform_small_numbers', 'search_method': interpolation_search,
       # 'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
       #
       #{'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
       # 'range': small_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
       #{'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
       # 'range': small_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
       #{'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
       # 'range': small_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
       #{'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
       # 'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': range(1, 2)},
       #{'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
       # 'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': range(1, 2)},
       #{'name': 'binary_search_uniform_small_numbers', 'search_method': binary_search,
       # 'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': range(1, 2)},
       #
        {'name': 'linear_multiple_search_uniform_small_numbers', 'search_method': linear_multiple_search,
         'range': range(2, 503, 50), 'distribution_method': np.random.uniform, 'input_range': range(0, 501, 100)},
        {'name': 'multiple_value_search_uniform_small_numbers', 'search_method': multiple_value_search,
         'range': range(2, 503, 50), 'distribution_method': np.random.uniform, 'input_range': range(0, 501, 100)},
        {'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
         'range': range(2, 503, 50), 'distribution_method': np.random.uniform, 'input_range': range(0, 501, 100)},
       #{'name': 'binary_multiple_search_normal_small_numbers', 'search_method': binary_multiple_search,
       # 'range': range(2, 503, 50), 'distribution_method': np.random.normal, 'input_range': range(0, 501, 100)},
       #{'name': 'binary_multiple_search_exponential_small_numbers', 'search_method': binary_multiple_search,
       # 'range': range(2, 503, 50), 'distribution_method': np.random.exponential, 'input_range': range(0, 501, 100)},
       #{'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
       # 'range': large_number_range, 'distribution_method': np.random.uniform, 'input_range': small_number_range},
       #{'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
       # 'range': large_number_range, 'distribution_method': np.random.normal, 'input_range': small_number_range},
       #{'name': 'binary_multiple_search_uniform_small_numbers', 'search_method': binary_multiple_search,
       # 'range': large_number_range, 'distribution_method': np.random.exponential, 'input_range': small_number_range},

    ]


    for search in searches:
        test_search(search)

if __name__ == '__main__':
    main()
