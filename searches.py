def linear_search(numbers, searched_number):
    for index, searched_number in enumerate(numbers):
        if number == searched_number:
            return index
    return -1


def binary_search(numbers, searched_number):
    low = 0
    high = len(numbers) - 1
    mid = 0

    if not numbers.any():
        return -1

    while low <= high:

        mid = (high + low) // 2

        if numbers[mid] < searched_number:
            low = mid + 1
        elif numbers[mid] > searched_number:
            high = mid - 1
        else:
            return mid

    return -1


def interpolation_search(numbers, searched_number, low, high):
    while low < high:
        if numbers[low] >= searched_number:
            return low
        if searched_number >= numbers[high]:
            return high

        interpolation = int(low + (searched_number - numbers[low]) \
            / (numbers[high] - numbers[low]) \
            * (high - low))

        if numbers[interpolation] < searched_number:
            low = interpolation + 1
        elif numbers[interpolation] > searched_number:
            high = interpolation - 1
        else:
            return interpolation

    return low


def interpolated_binary_search(numbers, searched_number):
    low = 0
    high = len(numbers) - 1

    if not numbers.any():
        return -1

    while low < high:
        if numbers[low] > searched_number or searched_number > numbers[high]:
            return -1

        interpolation = int(low + (searched_number - numbers[low]) \
            / (numbers[high] - numbers[low]) \
            * (high - low))

        if numbers[interpolation] > searched_number:
            mid = int((interpolation + high) / 2)

            if searched_number <= numbers[mid]:
                low = interpolation + 1
                high = mid
            else:
                low = mid + 1

        elif numbers[interpolation] < searched_number:
            mid = int((interpolation + low) / 2)

            if searched_number >= numbers[mid]:
                low = mid
                high = interpolation - 1
            else:
                high = mid - 1

        else:
            return interpolation

    return -1
