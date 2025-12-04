
def day3_pt2():
    #file = 'input'
    file = 'test'

    with open(file, "r", encoding="utf-8") as f:
        cntr = 0
        for raw_line in f:
            line = raw_line.strip()

            top_n_nums = []
            top_n_indexes = []
            n = 12

            for digit in range(n):
                last_top_n=0
                last_top_i=0

                for i, c in enumerate(line):

                    if i > len(top_n_nums):
                        if int(c) > last_top_n and (len(top_n_indexes) == 0 or top_n_indexes[-1] > i):
                            last_top_n = int(c)
                            last_top_i = i
                    else:
                        last_top_n = int(c)
                        last_top_i = i

                top_n_nums.append(last_top_n)
                top_n_indexes.append(last_top_i)

            num_s = ""
            for c in top_n_nums:
                num_s += str(c)

            print(num_s)
            cntr += int(num_s)
    assert 3121910778619 == cntr
    print(cntr)

    # 987654321111
    # 811111111119
    # 434234234278
    # 888911112111

if __name__ == '__main__':
    day3_pt2()