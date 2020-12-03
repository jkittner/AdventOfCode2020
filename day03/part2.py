import argparse
from typing import List

import pytest


def count_trees(raster_map: List[List[str]], x_walk: int, y_walk: int) -> int:
    y = 0
    x = 0
    x_len = len(raster_map[0])
    y_len = len(raster_map)
    tree_count = 0
    while y < y_len - 1:
        # walk
        x += x_walk
        y += y_walk
        # reset to start from the beginning
        if x >= x_len:
            x = x % x_len
        # check if we hit tree
        if raster_map[y][x] == '#':
            tree_count += 1
    return tree_count


def different_walks_multiply(raster_map: List[List[str]]) -> int:
    walks = (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    )
    solution = 1
    for x, y in walks:
        part_solution = count_trees(raster_map=raster_map, x_walk=x, y_walk=y)
        solution *= part_solution
    return solution


def _parse_file(contents: List[str]) -> List[List[str]]:
    grid = [[j for j in i.strip()] for i in contents]
    return grid


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        contents = f.readlines()
    raster_map = _parse_file(contents)
    solution = different_walks_multiply(raster_map)
    print(f'the solution is: {solution}')
    return 0


FOREST_STR = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#',
]


@pytest.mark.parametrize(
    ('x_walk', 'y_walk', 'exp'),
    (
        (1, 1, 2),
        (3, 1, 7),
        (5, 1, 3),
        (7, 1, 4),
        (1, 2, 2),
    ),
)
def test_main(x_walk, y_walk, exp):
    raster_map = _parse_file(FOREST_STR)
    assert count_trees(
        raster_map=raster_map,
        x_walk=x_walk,
        y_walk=y_walk,
    ) == exp


def test_different_walks_multiply():
    assert different_walks_multiply(FOREST_STR) == 336


if __name__ == '__main__':
    exit(main())
