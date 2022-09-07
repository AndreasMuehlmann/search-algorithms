def write_plot(xs, ys, file_path):
    with open(file_path, 'w') as file:
        file.write('x, y\n')

        for count, x in enumerate(xs):
            file.write(f'{x},{ys[count]}\n')


def write_search_times(search_times, lengths, file_path):
    with open(file_path, 'w') as file:
        file.write('x, y\n')

        for count, time in enumerate(search_times):
            file.write(f'{lengths[count]},{round(time * 10**6, 5)}\n')
