def day1_pt2():
    position = 50
    cntr = 0

    file = 'input'

    with open(file, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            direction = line[0]
            steps = int(line[1:])

            if direction == "L":
                for _ in range(steps):
                    position = (position - 1) % 100
                    if position == 0:
                        cntr += 1
            else:  # "R"
                for _ in range(steps):
                    position = (position + 1) % 100
                    if position == 0:
                        cntr += 1

    print(cntr)


if __name__ == "__main__":
    day1_pt2()
