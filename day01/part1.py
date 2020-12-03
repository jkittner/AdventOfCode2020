import argparse
from typing import Optional
from typing import Set

import pytest


def find_sum_to_2020(exp_rep: Set[int]) -> Optional[int]:
    for i in exp_rep:
        for j in exp_rep:
            if i + j == 2020:
                return i * j
            else:
                continue
    else:
        raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        in_file = {int(i.strip()) for i in f.readlines()}
    solution = find_sum_to_2020(in_file)
    print(f'the solution is: {solution}')
    return 0


@pytest.mark.parametrize(
    ('exp_rep', 'res'),
    (
        ({2000, 150, 180, 20}, 40000),
    ),
)
def test_main(exp_rep, res):
    assert find_sum_to_2020(exp_rep) == res


def test_raises_if_not_found():
    with pytest.raises(NotImplementedError):
        find_sum_to_2020({10, 20, 30})


if __name__ == '__main__':
    exit(main())
