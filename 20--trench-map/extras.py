def show(image):
    border_width = image.outer_width + 4
    border_height = image.outer_height + 4
    border_inner_width = image.outer_width + 2
    border_inner_height = image.outer_height + 2

    print(image.background * border_width)
    print(image.background + (' ' * border_inner_width) + image.background)

    for row in image.pixels:
        print(image.background + ' ', end='')
        print(''.join(row), end='')
        print(' ' + image.background, end='')
        print()

    print(image.background + (' ' * border_inner_width) + image.background)
    print(image.background * border_width)


if __name__ == '__main__':
    from s import Image

    f = open('example')
    f.readline()
    f.readline()
    raw_image = [line.rstrip('\n') for line in f.readlines()]
    image = Image(raw_image, 4)
    show(image)
