import argparse
import re
from typing import Any
from typing import Dict
from typing import List

import pytest


EXP_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}


def valid_field(field: str, value: str) -> bool:
    if field == 'byr':
        year_int = int(value)
        if year_int >= 1920 and year_int <= 2002:
            return True
        else:
            return False
    elif field == 'iyr':
        year_int = int(value)
        if year_int >= 2010 and year_int <= 2020:
            return True
        else:
            return False
    elif field == 'eyr':
        year_int = int(value)
        if year_int >= 2020 and year_int <= 2030:
            return True
        else:
            return False
    elif field == 'hgt':
        if re.match(r'\d{3}cm$', value):
            height_str = re.search(r'\d{3}', value)
            assert height_str is not None
            height = int(height_str.group(0))
            if height >= 150 and height <= 193:
                return True
            else:
                return False
        elif re.match(r'\d{2}in$', value):
            height_str = re.search(r'\d{2}', value)
            assert height_str is not None
            height = int(height_str.group(0))
            if height >= 59 and height <= 76:
                return True
            else:
                return False
        else:
            return False
    elif field == 'hcl':
        if re.match(r'^#[0-9a-f]{6}$', value):
            return True
        else:
            return False
    elif field == 'ecl':
        allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in allowed:
            return True
        else:
            return False
    elif field == 'pid':
        if re.match(r'^[0-9]{9}$', value):
            return True
        else:
            return False
    elif field == 'cid':
        return True
    else:
        raise NotImplementedError


def _empty_dict() -> Dict[Any, Any]:
    return {}


def _check_passport_fields(passport: Dict[str, str]) -> bool:
    for key, value in passport.items():
        if not valid_field(key, value):
            return False
    else:
        return True


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
            len(keys_set_diff) == 1
            and 'cid' in keys_set_diff
            and _check_passport_fields(passport_dict)
            or len(keys_set_diff) == 0
            and _check_passport_fields(passport_dict)
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


TEST_INPUT_INVALID = [
    'eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',  # noqa E501
    'iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946',  # noqa E501
    'hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',  # noqa E501
    'hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007',  # noqa E501
]

TEST_INPUT_VALID = [
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f',  # noqa E501
    'eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',  # noqa E501
    'hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022',  # noqa E501
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',  # noqa E501
]


@pytest.mark.parametrize(
    ('test_list', 'exp'),
    (
        (TEST_INPUT_INVALID, 0),
        (TEST_INPUT_VALID, 4),
    ),
)
def tests_passport_check(test_list, exp):
    assert passport_check(test_list) == exp


@pytest.mark.parametrize(
    ('field', 'value', 'exp'),
    (
        ('byr', '2000', True),
        ('byr', '1900', False),
        ('byr', '1', False),
        ('byr', '1123456', False),

        ('iyr', '2015', True),
        ('iyr', '1850', False),
        ('iyr', '2', False),
        ('iyr', '1123456', False),

        ('eyr', '2025', True),
        ('eyr', '1850', False),
        ('eyr', '2', False),
        ('eyr', '1123456', False),

        ('hgt', '180cm', True),
        ('hgt', '200cm', False),
        ('hgt', '20000cm', False),
        ('hgt', '2cm', False),
        ('hgt', '65in', True),
        ('hgt', '200in', False),
        ('hgt', '20000in', False),
        ('hgt', '2in', False),

        ('hcl', '#123abc', True),
        ('hcl', '#123123123123', False),
        ('hcl', '#invali', False),
        ('hcl', '#123', False),
        ('hcl', '#iq', False),

        ('ecl', 'amb', True),
        ('ecl', 'not_in', False),

        ('pid', '000012345', True),
        ('pid', '123456789', True),
        ('pid', '123', False),
        ('pid', '1234567891011', False),

        ('cid', '', True),
    ),
)
def test_validate_field(field, value, exp):
    assert valid_field(field, value) is exp


if __name__ == '__main__':
    exit(main())
