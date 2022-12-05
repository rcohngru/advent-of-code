from queue import LifoQueue
from typing import List, Tuple

def main():
    """Driver code to solve the puzzle."""

    fname = "puzzle_data.txt"
    lines = ingest_file(fname)
    raw_crates, num_stacks, raw_instructions = parse_lines(lines)

    stacks = prepare_crates(raw_crates, num_stacks)
    instructions = prepare_instructions(raw_instructions)

    final_stacks = process_instructions_9000(stacks, instructions)

    top = ""
    for s in final_stacks:
        top += s.get()

    print("-------- Part 1 --------")
    print(top)


    stacks = prepare_crates(raw_crates, num_stacks)
    final_stacks = process_instructions_9001(stacks, instructions)

    top = ""
    for s in final_stacks:
        top += s.get()

    print("-------- Part 2 --------")
    print(top)

# -------- Part 1 --------
def ingest_file(fname: str) -> List[str]:
    """Returns a list of lines, given a filename."""
    with open(fname, "r") as f:
        lines = f.readlines()

    lines = [l.strip("\n") for l in lines]
    return lines

def parse_lines(lines: List[str]) -> Tuple[List[str], int, List[str]]:
    """
        Parses the input list of lines and returns metadata necessary to construct the necessary elements to solve the problem.

        Parameters:
        lines (List[str]): a list of strings, where each string is a line in the input file

        Returns:
        raw_crates (List[str]): a list of strings, where each string is one layer of crates along the stacks
        num_stacks (int): the number of stacks that are in the problem
        raw_instructions (List[str]): a list of strings, where each string is one instruction as listed in the input file
    """
    parsing_crates = True
    raw_crates = []
    num_stacks = None

    raw_instructions = []
    for l in lines:
        if parsing_crates:
            if "[" in l:
                raw_crates.append(l)
            else:
                num_stacks = int(l.strip()[-1])
                parsing_crates = False
        else:
            if l == "":
                continue

            raw_instructions.append(l)

    return raw_crates, num_stacks, raw_instructions
    
def prepare_crates(raw_crates: List[str], num_stacks: int) -> List[LifoQueue]:
    """
        Returns the filled LifoQueues representing the stacks and crates in the problem.

        Parameters:
        raw_crates (List[str]): a list of strings, where each string is one layer of crates along the stacks
        num_stacks (int): the number of stacks that are in the problem

        Returns:
        stacks (List[LifoQueue]): a list of LifoQueues, where each LifoQueue represents a stack of crates.
    """
    stacks = []
    for i in range(num_stacks):
        stacks.append(LifoQueue())

    for c in reversed(raw_crates):
        for i in range(0, num_stacks * 4, 4):
            stack = i // 4
            crate = c[i:i+4][1]
            if crate.isalpha():
                stacks[stack].put(crate, block=False)
    
    return stacks

def prepare_instructions(raw_instructions: List[str]) -> List[Tuple[int, int, int]]:
    """
        Returns the formatted instructions.

        Parameters:
        raw_instructions (List[str]): a list of strings, where each string is one instruction as listed in the input file

        Returns:
        instructions (List[Tuple[int, int, int]]): a list of tuples, where each tuple is one instruction containing three elements.
                                                    The first element is the amount of crates to move, the second element is the 
                                                    1-indexed stack of origin, and the third element is the 1-indexed destination stack.
    """
    instructions = []
    for instruction in raw_instructions:
        i = instruction.split(" ")
        instructions.append((
            int(i[1]),
            int(i[3]),
            int(i[5])
        ))
    
    return instructions

def process_instructions_9000(stacks: List[LifoQueue], instructions: List[Tuple[int, int, int]]) -> List[LifoQueue]:
    """
        Processes the set of instructions on the stacks.

        This simulates instructions for a CrateMover 9000, which can only pick up one crate at a time. Instructions are processed in
        sequential order. Within each instruction are the number of crates to be moved and the 1-indexed locations of the destination
        and origin stacks.

        An important thing to note is that due to the 1-crate nature of the CrateMover 9000, if multiple crates are being moved in one 
        instruction, the ordering of them will be reversed in the new stack.

        Parameters:
        stacks (List[LifoQueue]): a list of LifoQueues, where each LifoQueue represents a stack of crates.
        instructions (List[Tuple[int, int, int]]): a list of tuples, where each tuple is one instruction containing three elements.
                                                    The first element is the amount of crates to move, the second element is the 
                                                    1-indexed stack of origin, and the third element is the 1-indexed destination stack.
    """
    for move_amount, from_stack, to_stack in instructions:
        for _ in range(move_amount):
            
            c = stacks[from_stack - 1].get(block=False)
            stacks[to_stack - 1].put(c, block=False)
    
    return stacks


# -------- Part 2 --------

def process_instructions_9001(stacks: List[LifoQueue], instructions: Tuple[int, int, int]) -> List[LifoQueue]:
    """
        Processes the set of instructions on the stacks.

        This simulates instructions for a CrateMover 9001, which can pick up multiple crates at a time. Instructions are processed in
        sequential order. Within each instruction are the number of crates to be moved and the 1-indexed locations of the destination
        and origin stacks.

        An important thing to note is that due to the multi-crate nature of the CrateMover 9000, the ordering of the crates being moved
        will be the same across the origin and destination stacks.

        Parameters:
        stacks (List[LifoQueue]): a list of LifoQueues, where each LifoQueue represents a stack of crates.
        instructions (List[Tuple[int, int, int]]): a list of tuples, where each tuple is one instruction containing three elements.
                                                    The first element is the amount of crates to move, the second element is the 
                                                    1-indexed stack of origin, and the third element is the 1-indexed destination stack.
    """
    for move_amount, from_stack, to_stack in instructions:
        crates_in_transit = []
        for _ in range(move_amount):
            
            c = stacks[from_stack - 1].get(block=False)
            crates_in_transit.append(c)
        
        for c in reversed(crates_in_transit):
            stacks[to_stack - 1].put(c, block=False)
    
    return stacks

if __name__ == "__main__":
    main()