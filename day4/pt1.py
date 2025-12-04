import numpy as np

def neighbor_counts(a: np.ndarray) -> np.ndarray:
    p = np.pad(a, 1, mode="constant", constant_values=0)

    counts = (
            p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +  # top-left, top, top-right
            p[1:-1, :-2]            +     p[1:-1, 2:] +  # left,      right
            p[2:, :-2] + p[2:, 1:-1] + p[2:, 2:]        # bottom-left, bottom, bottom-right
    )
    return counts


def day4_pt1():
    file = 'input'
    #file = 'test'

    grid = []

    with open(file, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()

            #print(line.split())
            for row in line.split():
                r = []
                for item in row:
                    if item == '.':
                        r.append(0)
                    elif item == '@':
                        r.append(1)
                grid.append(r)

    grid = np.array(grid)
    print(grid)

    counts = neighbor_counts(grid)
    print(counts)

    valid_rolls = grid * counts

    print(valid_rolls)

    cntr = 0
    for row in valid_rolls:
        for item in row:
            if 0 < item < 4:
                cntr += 1

    print(cntr)


if __name__ == '__main__':
    day4_pt1()

# [0 0 3 3 0 3 3 4 3 0]
# [3 6 6 0 4 0 4 0 5 4]
# [4 7 6 7 5 0 2 0 4 4]
# [4 0 6 7 7 6 0 0 4 0]
# [3 5 0 7 8 7 5 0 4 3]
# [0 4 6 5 7 6 6 5 0 4]
# [0 4 0 6 0 5 0 6 7 4]
# [2 0 6 6 6 0 6 7 7 4]
# [0 5 5 7 6 7 6 7 5 0]
# [1 0 3 0 4 5 4 0 2 0]

# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.


