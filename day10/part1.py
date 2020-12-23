import argparse

import pytest


def compute_solution(inp_str: str) -> int:
    adapters = [int(i) for i in inp_str.splitlines()]
    # add the charging outlet
    adapters.append(0)
    # add our device
    adapters.append(max(adapters) + 3)
    adapters.sort()

    nr_adapters = len(adapters)
    diff_one = 0
    diff_three = 0
    i = 0
    while i < nr_adapters - 1:
        if adapters[i + 1] - adapters[i] == 1:
            diff_one += 1
        elif adapters[i + 1] - adapters[i] == 3:
            diff_three += 1
        else:
            raise NotImplementedError
        i += 1
    return diff_one * diff_three


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        adapter_str = f.read()
    solution = compute_solution(adapter_str)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT_a = '''\
16
10
15
5
1
11
7
19
6
12
4
'''


TEST_INPUT_b = '''\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
'''


@pytest.mark.parametrize(
    ('i', 'exp'),
    (
        (TEST_INPUT_a, 35),
        (TEST_INPUT_b, 220),
    ),
)
def test_compute_solutions(i, exp):
    assert compute_solution(i) == exp


if __name__ == '__main__':
    exit(main())
