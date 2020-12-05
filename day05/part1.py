import argparse
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        seat_specifiers = f.readlines()
    all_seat_ids = [get_seat_info(i).seat_id for i in seat_specifiers]
    solution = max(all_seat_ids)
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


if __name__ == '__main__':
    exit(main())
