import argparse
import re
from typing import List
from typing import NamedTuple
from typing import Tuple

import pytest


class Pw(NamedTuple):
    pos_a: int
    pos_b: int
    letter: str
    pw_str: str

    @property
    def pos_a_str(self) -> str:
        return self.pw_str[self.pos_a - 1]

    @property
    def pos_b_str(self) -> str:
        return self.pw_str[self.pos_b - 1]


def valid_pw(pw_tup: Pw) -> bool:
    if (
            pw_tup.pos_a_str == pw_tup.letter
            and pw_tup.pos_b_str != pw_tup.letter
            or pw_tup.pos_a_str != pw_tup.letter
            and pw_tup.pos_b_str == pw_tup.letter
    ):
        return True
    else:
        return False


def _parse_input_line(str_line: str) -> Pw:
    line_split: List[str] = re.split(r'-|\s|:\s', str_line)
    parsed_line = Pw(
        pos_a=int(line_split[0]),
        pos_b=int(line_split[1]),
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


@pytest.mark.parametrize(
    ('pw', 'exp'),
    (
        (Pw(pos_a=1, pos_b=3, letter='a', pw_str='abcde'), True),
        (Pw(pos_a=1, pos_b=3, letter='a', pw_str='cdefg'), False),
        (Pw(pos_a=1, pos_b=3, letter='c', pw_str='ccccccccc'), False),
        (Pw(pos_a=1, pos_b=3, letter='a', pw_str='ccccccccc'), False),
    ),
)
def test_valid_pw(pw, exp):
    assert valid_pw(pw) == exp


def test_parse_line():
    assert _parse_input_line('1-3 b: cdefg') == (1, 3, 'b', 'cdefg')


def test_get_letter():
    pw = Pw(pos_a=1, pos_b=3, letter='a', pw_str='abcde')
    assert pw.pos_a_str == 'a'
    assert pw.pos_b_str == 'c'


@pytest.mark.parametrize(
    ('pw_tup', 'nr_valid_pw'),
    (
        (
            (
                Pw(pos_a=1, pos_b=3, letter='a', pw_str='abcde'),
                Pw(pos_a=3, pos_b=4, letter='a', pw_str='abcde'),
                Pw(pos_a=2, pos_b=4, letter='a', pw_str='abacde'),
            ),
            1,
        ),
    ),
)
def test_find_nr_of_valid_pw(pw_tup, nr_valid_pw):
    assert find_nr_valid_pw(pw_tup) == nr_valid_pw


if __name__ == '__main__':
    exit(main())
