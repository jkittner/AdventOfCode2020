import argparse


INVALID_NR_PT1 = 375054920


def find_number_range(numbers: str, invalid_nr: int) -> int:
    nr_int = [int(i) for i in numbers.splitlines()]
    numbers_len = len(nr_int)
    for i in range(numbers_len):
        for j in range(numbers_len):
            pot_sum = sum(nr_int[i:j + 1])
            if pot_sum == invalid_nr:
                sum_min_max = min(nr_int[i:j + 1]) + max(nr_int[i:j + 1])
                return sum_min_max
    else:
        raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        numbers = f.read()
    solution = find_number_range(numbers, INVALID_NR_PT1)
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


def test_find_number_range():
    assert find_number_range(TEST_INPUT, 127) == 62


if __name__ == '__main__':
    exit(main())
