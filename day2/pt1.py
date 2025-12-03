def day2_pt1():
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
                    if numm[:len(numm)//2] == numm[len(numm)//2:] and len(str(num)) % 2 == 0:
                        cntr += num
                        print("Invalid ID", num)
            if not line:
                continue
    print("sum:", cntr)

    #assert 1227775554 == cntr

if __name__ == '__main__':
    day2_pt1()