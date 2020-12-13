import argparse
import copy
from typing import List
from typing import NamedTuple
from typing import Union

import pytest


class Instruction(NamedTuple):
    c_id: int
    instr: str
    val: int

    @property
    def instr_swapped(self):
        if self.instr == 'nop':
            return Instruction(self.c_id, 'jmp', self.val)
        elif self.instr == 'jmp':
            return Instruction(self.c_id, 'nop', self.val)
        else:
            return self


def run_boot_code(instr_list: List[Instruction]) -> Union[int, bool]:
    instructions_ran = set()
    nr_instructions = len(instr_list)
    acc = 0
    c_id = 0
    while c_id not in instructions_ran:
        instruction = instr_list[c_id]
        c_id = instruction.c_id
        instructions_ran.add(c_id)
        if instruction.instr == 'acc':
            acc += instruction.val
            c_id += 1
        elif instruction.instr == 'jmp':
            c_id += instruction.val
        elif instruction.instr == 'nop':
            c_id += 1
        else:
            raise NotImplementedError
        # last statement executed
        if c_id == nr_instructions:
            return acc
    else:
        return False


def find_wrong_statement(instructions: str):
    instr_list = [
        Instruction(i[0], i[1].split()[0], int(i[1].split()[1]))
        for i in enumerate(instructions.splitlines())
    ]
    nr_instructions = len(instr_list)
    # run the code for each line and swap
    for i in range(nr_instructions):
        if instr_list[i].instr in ['jmp', 'nop']:
            instr_list_modifed = copy.deepcopy(instr_list)
            instr_list_modifed[i] = instr_list_modifed[i].instr_swapped
            acc = run_boot_code(instr_list_modifed)
            if acc is not False:
                return acc
        else:
            continue
    else:
        raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        instruc_str = f.read()
    solution = find_wrong_statement(instruc_str)
    print(f'the solution is: {solution}')
    return 0


TEST_INPUT = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''


@pytest.mark.parametrize(
    ('instr', 'exp'),
    (
        ('jmp', 'nop'),
        ('nop', 'jmp'),
        ('acc', 'acc'),
    ),
)
def test_instruction_swapped(instr, exp):
    assert Instruction(1, instr, 2).instr_swapped.instr == exp


def test_wrong_statement():
    assert find_wrong_statement(TEST_INPUT) == 8


if __name__ == '__main__':
    exit(main())
