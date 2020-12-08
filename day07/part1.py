import argparse
import collections
import re


def bags_contain_shiny(bags: str) -> int:
    # default dict to be able to directly append
    # no need to check if it exists and is a list
    bag_dict = collections.defaultdict(list)
    for line in bags.splitlines():
        matches = re.match(r'^([a-z]+ [a-z]+) bags contain (.*)$', line)
        assert matches is not None
        parent_bag_color = matches.groups()[0]
        contents = re.findall(r'(\d+) ([a-z]+ [a-z]+)', matches.groups()[1])
        for number, color in contents:
            bag_dict[color].append(parent_bag_color)
    # first start with the bags we know that can directly contain shiny bags
    # and extend from here
    bags_to_check = bag_dict['shiny gold']
    # add bags we checked and can contain shiny
    can_contain_shiny = []
    counter = 0
    while len(bags_to_check) > 0:
        # remove checked item from bags_to_check
        curr_col = bags_to_check.pop()
        # check if not already tested
        if curr_col not in can_contain_shiny:
            can_contain_shiny.append(curr_col)
            # add new list of other bags to check
            bags_to_check.extend(bag_dict[curr_col])
        counter += 1
    print(f'needed {counter} iterations')
    nr_bags = len(can_contain_shiny)
    return nr_bags


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        rules = f.read()
    solution = bags_contain_shiny(rules)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = '''\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''


def test_bags():
    assert bags_contain_shiny(TEST_INPUT) == 4


if __name__ == '__main__':
    exit(main())
