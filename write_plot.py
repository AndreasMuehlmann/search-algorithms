def write_2d_plot(points, file_path):
    with open(file_path, 'w') as file:
        file.write('x,y\n')

        for point in points:
            file.write(f'{point[0]},{point[1]}\n')


def write_3d_plot(points, file_path):
    with open(file_path, 'w') as file:
        file.write('x,y,z\n')

        for point in points:
            file.write(f'{point[0]},{point[1]},{point[2]}\n')
