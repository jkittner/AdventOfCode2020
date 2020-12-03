import argparse
from typing import List


def count_trees(raster_map: List[List[str]]) -> int:
    y = 0
    x = 0
    x_len = len(raster_map[0])
    y_len = len(raster_map)
    tree_count = 0
    while y < y_len - 1:
        # walk
        x += 3
        y += 1
        # reset to start of row
        if x >= x_len:
            x = x % x_len
        # check if we hit a tree
        if raster_map[y][x] == '#':
            tree_count += 1
    return tree_count


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
    solution = count_trees(raster_map)
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


def test_count_trees():
    raster_map = _parse_file(FOREST_STR)
    assert count_trees(raster_map) == 7


if __name__ == '__main__':
    exit(main())
