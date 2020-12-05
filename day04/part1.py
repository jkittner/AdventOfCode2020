import argparse
import re
from typing import Any
from typing import Dict
from typing import List


EXP_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}


def _empty_dict() -> Dict[Any, Any]:
    return {}


def passport_check(passports: List[str]) -> int:
    valid_counter = 0
    for passport in passports:
        passport_dict = _empty_dict()
        fields_pairs = re.split(r'\s', passport)
        for pair in fields_pairs:
            key, value = pair.split(':')
            passport_dict[key] = value
        key_set = set(passport_dict.keys())
        keys_set_diff = EXP_FIELDS.difference(key_set)
        if (
            len(keys_set_diff) == 1 and 'cid' in keys_set_diff
            or len(keys_set_diff) == 0
        ):
            valid_counter += 1
        else:
            continue
    return valid_counter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        passports = f.read().strip().split('\n\n')
    solution = passport_check(passports)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm',  # noqa E501
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929',  # noqa E501
    'hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm',  # noqa E501
    'hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in',
]


def tests_passport_check():
    assert passport_check(TEST_INPUT) == 2


if __name__ == '__main__':
    exit(main())
