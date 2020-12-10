import argparse


def find_number(numbers: str, skip_nr: int) -> int:
    nr_int = [int(i) for i in numbers.splitlines()]
    numbers_len = len(nr_int)
    row_count = 0
    while row_count <= numbers_len - skip_nr:
        intervall = nr_int[row_count:row_count + skip_nr]
        nr_sum = nr_int[row_count + skip_nr]
        valid = False
        for i in intervall:
            for j in intervall:
                if i + j == nr_sum:
                    valid = True
                    break  # break for j
            if valid:
                break  # break for i
        else:
            return nr_sum
        row_count += 1
    else:
        raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        numbers = f.read()
    solution = find_number(numbers, 25)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
'''


def test_find_numbers():
    assert find_number(TEST_INPUT, 5) == 127


if __name__ == '__main__':
    exit(main())
