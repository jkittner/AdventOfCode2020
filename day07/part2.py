import argparse
import collections
import re
from typing import NamedTuple
from typing import Optional


class Bag(NamedTuple):
    number_str: int
    color: str

    @property
    def number(self) -> Optional[int]:
        try:
            return int(self.number_str)
        except ValueError:
            print('cannot convert to int')
            return None


def nr_bags_contain(bags: str) -> int:
    # default dict to be able to directly append
    # no need to check if it exists and is a list
    bag_dict = collections.defaultdict(list)
    for line in bags.splitlines():
        matches = re.match(r'^([a-z]+ [a-z]+) bags contain (.*)$', line)
        assert matches is not None
        parent_bag_color = matches.groups()[0]
        contents = re.findall(r'(\d+) ([a-z]+ [a-z]+)', matches.groups()[1])
        for i in contents:
            bag_dict[parent_bag_color].append(Bag(*i))
            # bag_dict -> Dict[str, List[Bag, ...]]

    bags_to_check = bag_dict['shiny gold']
    bag_counter = 0
    # add bags we checked and can contain shiny
    counter = 0
    while len(bags_to_check) > 0:
        # remove checked item from bags_to_check
        curr_bag = bags_to_check.pop()
        # count the number of bags it can contain
        assert curr_bag.number is not None
        bag_counter += curr_bag.number
        # check all bags this bag contains
        for i in bag_dict[curr_bag.color]:
            # contain 2 dark orange bags --> dark orange bags contain 2 ...
            nr_new_bag_can_contain = curr_bag.number * i.number
            bags_to_check.append(Bag(nr_new_bag_can_contain, i.color))
        counter += 1
    print(f'needed {counter} iterations')
    return bag_counter


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        rules = f.read()
    solution = nr_bags_contain(rules)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
'''


def test_bags():
    assert nr_bags_contain(TEST_INPUT) == 126


if __name__ == '__main__':
    exit(main())
