import sys

import log21


def main(size: int = 5, from_center: bool = False, counter_clockwise: bool = False):
    """Draw a square of numbers.

    Args:
        size: The size of the square.
        from_center: If True, the square will be drawn from the center.
        counter_clockwise: If True, the square will be drawn counter-clockwise.
    """
    if from_center and size % 2 == 0:
        log21.critical(
            'The size of the square must be odd if you want to draw from the center.'
        )
        sys.exit(1)

    array = [[0] * size for _ in range(size)]

    n = 1
    modifier = 1
    x, y = 0, 0
    if from_center:
        n = size * size
        modifier = -1

    if not counter_clockwise and not from_center or counter_clockwise and from_center:
        while not all(all(row) for row in array):
            # Right
            while x < size and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                x += 1
            x -= 1
            y += 1
            # Down
            while y < size and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                y += 1
            y -= 1
            x -= 1
            # Left
            while x >= 0 and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                x -= 1
            x += 1
            y -= 1
            # Up
            while y >= 0 and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                y -= 1
            y += 1
            x += 1
    elif counter_clockwise and not from_center:
        while not all(all(row) for row in array):
            # Down
            while y < size and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                y += 1
            y -= 1
            x += 1
            # Right
            while x < size and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                x += 1
            x -= 1
            y -= 1
            # Up
            while y >= 0 and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                y -= 1
            y += 1
            x -= 1
            # Left
            while x >= 0 and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                x -= 1
            x += 1
            y += 1
    elif not counter_clockwise:
        x = size - 1
        while not all(all(row) for row in array):
            # Left
            while x >= 0 and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                x -= 1
            x += 1
            y += 1
            # Down
            while y < size and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                y += 1
            y -= 1
            x += 1
            # Right
            while x < size and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                x += 1
            x -= 1
            y -= 1
            # Up
            while y >= 0 and array[y][x] == 0:
                array[y][x] = n
                n += modifier
                y -= 1
            y += 1
            x -= 1

    for row in array:
        for item in row:
            length = len(str(size * size))
            print(f'{item:<{length}}', end=' ')
        print()


if __name__ == '__main__':
    log21.argumentify(main)
