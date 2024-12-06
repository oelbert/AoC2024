import re

example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
example2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def run_day3(pattern: str):
    numbers = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", pattern)
    return sum(int(number[0]) * int(number[1]) for number in numbers)

def run_day3_2(pattern: str):
    new_pattern = re.sub(r"don't\(\).+?do\(\)", "", pattern)
    return run_day3(new_pattern)

def main():
    with open("../data/day3.txt") as inputs:
        pattern = "".join(inputs.read().split('\n'))

    print(run_day3(example))
    print(run_day3(pattern))
    print(run_day3_2(example2))
    print(run_day3_2(pattern))
    new_pattern = re.sub(r"don't\(\).+?do\(\)", "", pattern)
    print(run_day3(new_pattern))


if __name__ == '__main__':
    main()
