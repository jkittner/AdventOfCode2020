import argparse
from collections import Counter
from typing import List


def everyone_answered_yes(answers: List[str]) -> int:
    nr_groups = len(answers)
    persons_per_group = [len(i.split('\n')) for i in answers]
    answers_per_group = [Counter(group.replace('\n', '')) for group in answers]
    i = 0
    all_yes_counter = 0
    while i < nr_groups:
        for j in answers_per_group[i].values():
            if j == persons_per_group[i]:
                all_yes_counter += 1
        i += 1
    return all_yes_counter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        group_questions_str = f.read().strip().split('\n\n')
        print(group_questions_str)
    solution = everyone_answered_yes(group_questions_str)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = [
    'abc',
    'a\nb\nc',
    'ab\nac',
    'a\na\na\na',
    'b',
    'wt\nk\nt',
    'l\ndle\nl',
    'uv\nfabuvn\nzvdu',
]

# falsch 3188


def test_everyone_answered_yes():
    assert everyone_answered_yes(TEST_INPUT) == 9


if __name__ == '__main__':
    exit(main())
