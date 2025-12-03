from libxml2 import boolToText


def day3_pt1():
    #file = 'input'
    file = 'test'

    with open(file, "r", encoding="utf-8") as f:
        cntr = 0
        for raw_line in f:
            line = raw_line.strip()
            #print(line)

            top_left = 0
            bottom_right = 0

            top_left_i = 0
            bottom_right_i = len(line)

            for i in range(len(line)):
                if int(line[i]) > top_left and i != len(line) - 1:
                    top_left = int(line[i])
                    top_left_i = i

            for i in range(top_left_i, -1, len(line)):
                print(i)
                if int(line[i]) > bottom_right and i > top_left_i:
                    bottom_right = int(line[-i])

            num = int(str(top_left) + str(bottom_right))
            print(num)

            cntr += num
    assert 357 == cntr

if __name__ == '__main__':
    day3_pt1()