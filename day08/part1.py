import argparse
from typing import NamedTuple


class Instruction(NamedTuple):
    c_id: int
    instr: str
    val: int


def run_boot_code(instructions: str) -> int:
    instructions_list = [
        Instruction(i[0], i[1].split()[0], int(i[1].split()[1]))
        for i in enumerate(instructions.splitlines())
    ]
    instructions_ran = set()
    acc = 0
    c_id = 0
    while c_id not in instructions_ran:
        instruction = instructions_list[c_id]
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
    return acc


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    args = parser.parse_args()
    with open(args.input) as f:
        instruc_str = f.read()
    solution = run_boot_code(instruc_str)
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


def test_bags():
    assert run_boot_code(TEST_INPUT) == 5


if __name__ == '__main__':
    exit(main())
