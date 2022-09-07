from searches import interpolation_search


def linear_multiple_search(numbers, searched_numbers):
    return [interpolation_search(numbers, searched_number, 0, len(numbers) - 1) for searched_number in searched_numbers]

def multiple_value_search(numbers, searched_numbers):
    low = 0
    high = len(numbers) - 1

    results = []
    for searched_number in searched_numbers:
        index = interpolation_search(numbers, searched_number, low, high)
        if numbers[index] == searched_number:
            low = index
            results.append(index)
            continue

        results.append(index)
    return results

def binary_multiple_search(numbers, searched_numbers):
    return _binary_multiple_search(numbers, searched_numbers, 0,
                                   len(searched_numbers) - 1, 0, len(numbers) - 1)


def _binary_multiple_search(numbers, searched_numbers, low, high,
                            low_search_index, high_search_index):
    if not high >= low:
        return []

    mid = low + (high - low) // 2

    index = interpolation_search(numbers, searched_numbers[mid],
                                    low_search_index, high_search_index)
    result = index if numbers[index] == searched_numbers[mid] else -1

    if index == len(numbers) - 1:
        return _binary_multiple_search(numbers, searched_numbers, low, mid - 1, low_search_index, index) \
            + [result] + _binary_multiple_search(numbers, searched_numbers, mid + 1, high, index, high_search_index)
    elif index == 0:
        return _binary_multiple_search(numbers, searched_numbers, low, mid - 1, low_search_index, index + 1) \
            + [result] + _binary_multiple_search(numbers, searched_numbers, mid + 1, high, index, high_search_index)
    else:
        return _binary_multiple_search(numbers, searched_numbers, low, mid - 1, low_search_index, index + 1) \
            + [result] + _binary_multiple_search(numbers, searched_numbers, mid + 1, high, index - 1, high_search_index)
