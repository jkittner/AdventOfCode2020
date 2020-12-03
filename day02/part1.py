import argparse
import re
from collections import Counter
from typing import NamedTuple
from typing import Tuple

import pytest


class Pw(NamedTuple):
    min_nr: int
    max_nr: int
    letter: str
    pw_str: str


def valid_pw(pw_tup: Pw) -> bool:
    nr_chars = Counter(pw_tup.pw_str)
    if (
        nr_chars[pw_tup.letter] >= pw_tup.min_nr
        and nr_chars[pw_tup.letter] <= pw_tup.max_nr
    ):
        return True
    else:
        return False


def _parse_input_line(str_line: str) -> Pw:
    line_split = re.split(r'-|\s|:\s', str_line)
    parsed_line = Pw(
        min_nr=int(line_split[0]),
        max_nr=int(line_split[1]),
        letter=line_split[2],
        pw_str=line_split[3],
    )
    return parsed_line


def find_nr_valid_pw(pw_to_check: Tuple[Pw, ...]) -> int:
    valid_counter = 0
    for i in pw_to_check:
        if valid_pw(i):
            valid_counter += 1
        else:
            continue
    return valid_counter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        in_file = tuple(_parse_input_line(i.strip()) for i in f.readlines())
    solution = find_nr_valid_pw(in_file)
    print(f'the solution is: {solution}')
    return 0


def test_parse_line():
    assert _parse_input_line('1-3 b: cdefg') == (1, 3, 'b', 'cdefg')


@pytest.mark.parametrize(
    ('pw', 'exp'),
    (
        (Pw(min_nr=1, max_nr=3, letter='a', pw_str='abcde'), True),
        (Pw(min_nr=1, max_nr=3, letter='a', pw_str='aaaaa'), False),
    ),
)
def test_valid_pw(pw, exp):
    assert valid_pw(pw) == exp


@pytest.mark.parametrize(
    ('pw_tup', 'nr_valid_pw'),
    (
        (
            (
                Pw(min_nr=1, max_nr=3, letter='a', pw_str='abcde'),
                Pw(min_nr=3, max_nr=4, letter='a', pw_str='abcde'),
                Pw(min_nr=2, max_nr=4, letter='a', pw_str='abacde'),
            ),
            2,
        ),
        (
            (
                Pw(min_nr=1, max_nr=3, letter='a', pw_str='aaaaa'),
                Pw(min_nr=1, max_nr=4, letter='a', pw_str='aaaaa'),
                Pw(min_nr=1, max_nr=5, letter='a', pw_str='aaabb'),
                Pw(min_nr=1, max_nr=3, letter='b', pw_str='aaabb'),
            ),
            2,
        ),
    ),
)
def test_find_nr_of_valid_pw(pw_tup, nr_valid_pw):
    assert find_nr_valid_pw(pw_tup) == nr_valid_pw


if __name__ == '__main__':
    exit(main())
