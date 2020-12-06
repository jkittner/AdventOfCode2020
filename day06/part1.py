import argparse
from typing import List


def answered_yes(answers: List[str]) -> int:
    answered_yes = sum(
        [len({i for i in group.replace('\n', '')}) for group in answers],
    )
    return answered_yes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        group_questions_str = f.read().split('\n\n')
    solution = answered_yes(group_questions_str)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = [
    'abc',
    'a\nb\nc',
    'ab\nac',
    'a\na\na\na',
    'b',
]


def test_answered_yes():
    assert answered_yes(TEST_INPUT) == 11


if __name__ == '__main__':
    exit(main())
