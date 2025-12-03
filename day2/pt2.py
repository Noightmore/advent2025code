def all_second_equal(d: dict) -> bool:
    values = list(d.values())
    if not values:
        return False

    first_second = values[0][1]
    return all(v[1] == first_second for v in values[1:])

def day2_pt22():
    file = 'input'
    #file = 'test'

    with open(file, "r", encoding="utf-8") as f:
        cntr = 0
        for raw_line in f:
            line = raw_line.strip()
            #print(line)

            ranges = line.split(",")
            for r in ranges:

                if r == '':
                    continue

                print("checking range:", (int(r.split("-")[0]), int(r.split("-")[1])+1))
                for num in range(int(r.split("-")[0]), int(r.split("-")[1])+1):
                    numm = str(num)

                    # check divisibility from 2 to len(numm) and then check if those groups are the same
                    is_cool = False

                    for group in range(1, len(numm) // 2 + 1):
                        if len(numm) % group == 0:  # the part must tile the string
                            part = numm[:group]
                            ok = True

                            for same_part in range(group, len(numm), group):
                                if numm[same_part:same_part + group] != part:
                                    ok = False
                                    break

                            if ok:
                                is_cool = True
                                break

                    if is_cool:
                        cntr += num
                        print(num)

            if not line:
                continue

    print("sum:", cntr)

    #assert 4174379265 == cntr

if __name__ == '__main__':
    day2_pt22()