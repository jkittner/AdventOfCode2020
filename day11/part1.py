import argparse
import copy
from collections import Counter
from typing import List

import pytest


def update_seatmap(seat_map: List[List[str]]) -> List[List[str]]:
    nr_rows = len(seat_map)
    row_len = len(seat_map[0])
    new_seat_map = copy.deepcopy(seat_map)
    for y, row in enumerate(seat_map):
        for x, seat in enumerate(row):
            surrounding_seats = []
            x_l = x - 1 if x > 0 else x
            x_r = x + 2 if x < row_len else x
            if y > 0:
                surrounding_seats.extend(seat_map[y - 1][x_l:x_r])
            if y < nr_rows - 1:
                surrounding_seats.extend(seat_map[y + 1][x_l:x_r])

            surrounding_seats.extend(seat_map[y][x_l:x_r])

            seat_counter = Counter(surrounding_seats)
            if seat == 'L':
                if seat_counter['#'] == 0:
                    new_seat_map[y][x] = '#'
            elif seat == '#':
                if seat_counter['#'] > 4:
                    new_seat_map[y][x] = 'L'
            elif seat == '.':
                pass
            else:
                raise NotImplementedError
    return new_seat_map


def parse_data(inp_str: str) -> List[List[str]]:
    seat_rows = inp_str.splitlines()
    seat_map = [[j for j in i] for i in seat_rows]
    return seat_map


def calc_solution(s: str) -> int:
    seat_map = parse_data(s)
    prev_seat_map: List[List[str]] = []
    while seat_map != prev_seat_map:
        prev_seat_map = seat_map
        seat_map = update_seatmap(seat_map)
        print(seat_map == prev_seat_map)
    # count seats
    occupied = 0
    for row in seat_map:
        occupied += Counter(row)['#']
    return occupied


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        seat_map_str = f.read()
    solution = calc_solution(seat_map_str)
    print(f'the solution is: {solution}')
    return 0


START = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
'''


FIRST_ROUND = '''\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
'''
SECOND_ROUND = '''\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
'''
THIRD_ROUND = '''\
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
'''


@pytest.mark.parametrize(
    ('i', 'exp'),
    (
        (START, parse_data(FIRST_ROUND)),
        (FIRST_ROUND, parse_data(SECOND_ROUND)),
        (SECOND_ROUND, parse_data(THIRD_ROUND)),
    ),
)
def test_compute_solutions(i, exp):
    seat_map = parse_data(i)
    assert update_seatmap(seat_map) == exp


def test_calc_solution():
    assert calc_solution(START) == 37


if __name__ == '__main__':
    exit(main())
