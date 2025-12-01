
def day1_pt1():
    start = 50
    cntr = 0
    with open("input", "r", encoding="utf-8") as f:
        for line in f:
            #print(line.strip())  # .strip() removes \n at the end
            if line[0] == "L":
                start = (start - int(line[1:])) % 100
            else:
                start = (start + int(line[1:])) % 100

            if start == 0:
                cntr += 1

    print(cntr)

if __name__ == "__main__":
    day1_pt1()