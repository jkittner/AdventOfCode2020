import argparse
from typing import List
from typing import NamedTuple

import pytest


class SeatPlan(NamedTuple):
    row: int
    col: int

    @property
    def seat_id(self) -> int:
        return (self.row * 8) + self.col


def get_seat_info(enc_str: str) -> SeatPlan:
    row_str = enc_str[:7]
    col_str = enc_str[7:]
    row = int(row_str.replace('F', '0').replace('B', '1'), 2)
    col = int(col_str.replace('R', '1').replace('L', '0'), 2)
    return SeatPlan(row, col)


def find_my_seat(seat_ids: List[int]) -> int:
    seat_id_set = set(seat_ids)
    exp_seat_ids = set(range(min(seat_id_set), max(seat_id_set) + 1))
    # we expect only one match
    my_seat = [i for i in exp_seat_ids.difference(seat_id_set)]
    if len(my_seat) > 1:
        raise NotImplementedError
    else:
        return my_seat[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        seat_specifiers = f.readlines()
    all_seat_ids = [get_seat_info(i).seat_id for i in seat_specifiers]
    solution = find_my_seat(all_seat_ids)
    print(f'the solution is: {solution}')
    return 0


@pytest.mark.parametrize(
    ('enc_str', 'expected'),
    (
        ('BFFFBBFRRR', 567),
        ('FFFBBBFRRR', 119),
        ('BBFFBBFRLL', 820),
    ),
)
def test_to_binary(enc_str, expected):
    assert get_seat_info(enc_str).seat_id == expected


def test_find_my_seat():
    INPUT = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13]
    assert find_my_seat(INPUT) == 9


if __name__ == '__main__':
    exit(main())
