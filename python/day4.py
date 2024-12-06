def read_data(file):
    infile = open(file, "r")
    return [line.strip() for line in infile.readlines()]

def find_xmas(wordsearch):
    sum1 = 0
    sum2 = 0
    for ii in range(len(wordsearch)):
        for jj in range(len(wordsearch[ii])):
            if wordsearch[ii][jj] == 'X':
                if ii < len(wordsearch) - 3:  # downwards
                    if "".join(wordsearch[ii+k][jj] for k in range(4)) == "XMAS":
                        sum1 += 1
                if ii > 2:  # upwards
                    if "".join(wordsearch[ii-k][jj] for k in range(4)) == "XMAS":
                        sum1 += 1
                if jj < len(wordsearch[ii]) - 3:  # rightwards
                    if "".join(wordsearch[ii][jj+k] for k in range(4)) == "XMAS":
                        sum1 += 1
                if jj > 2:  # leftwards
                    if "".join(wordsearch[ii][jj-k] for k in range(4)) == "XMAS":
                        sum1 += 1
                if (ii < len(wordsearch) - 3) and (jj < len(wordsearch[ii]) - 3):  # down-right diag
                    if "".join(wordsearch[ii+k][jj+k] for k in range(4)) == "XMAS":
                        sum1 += 1
                if (ii < len(wordsearch) - 3) and (jj > 2):  # down-left diag
                    if "".join(wordsearch[ii+k][jj-k] for k in range(4)) == "XMAS":
                        sum1 += 1
                if (ii > 2) and (jj < len(wordsearch[ii]) - 3):  # up-right diag
                    if "".join(wordsearch[ii-k][jj+k] for k in range(4)) == "XMAS":
                        sum1 += 1
                if (ii > 2) and (jj > 2):  # up-left diag
                    if "".join(wordsearch[ii-k][jj-k] for k in range(4)) == "XMAS":
                        sum1 += 1
            elif wordsearch[ii][jj] == 'A':
                if (ii > 0) and (jj > 0) and (ii < len(wordsearch) - 1) and (jj < len(wordsearch[ii]) - 1):
                    if wordsearch[ii-1][jj-1] == 'M':
                        if wordsearch[ii-1][jj+1] == 'S':
                            if wordsearch[ii+1][jj-1] == 'M':
                                if wordsearch[ii+1][jj+1] == 'S':
                                    sum2 += 1
                        elif wordsearch[ii-1][jj+1] == 'M':
                            if wordsearch[ii+1][jj-1] == 'S':
                                if wordsearch[ii+1][jj+1] == 'S':
                                    sum2 += 1
                    elif wordsearch[ii-1][jj-1] == 'S':
                        if wordsearch[ii-1][jj+1] == 'M':
                            if wordsearch[ii+1][jj-1] == 'S':
                                if wordsearch[ii+1][jj+1] == 'M':
                                    sum2 += 1
                        elif wordsearch[ii-1][jj+1] == 'S':
                            if wordsearch[ii+1][jj-1] == 'M':
                                if wordsearch[ii+1][jj+1] == 'M':
                                    sum2 += 1
    return sum1, sum2

def find_x_mas(wordsearch):
    sum = 0
    for ii in range(len(wordsearch)):
        for jj in range(len(wordsearch[ii])):
            if (ii > 0) and (jj > 0) and (ii < len(wordsearch) - 1) and (jj < len(wordsearch[ii]) - 1):
                if wordsearch[ii][jj] == 'A':
                    if wordsearch[ii-1][jj-1] == 'M':
                        if wordsearch[ii-1][jj+1] == 'S':
                            if wordsearch[ii+1][jj-1] == 'M':
                                if wordsearch[ii+1][jj+1] == 'S':
                                    sum += 1
    return sum


def main():
    search1 = read_data("../data/day4_test.txt")
    print(find_xmas(search1))
    search2 = read_data("../data/day4.txt")
    print(find_xmas(search2))

if __name__ == '__main__':
    main()
