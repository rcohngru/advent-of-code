from typing import List, Tuple, Set

def main():
    fname = "puzzle_data.txt"
    motions = ingest_file(fname)
    num_tail_positions = process_motions(motions)
    print("-------- Part 1 --------")
    print(num_tail_positions)

def ingest_file(fname: str) -> List[Tuple[str, int]]:
    with open(fname, "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]
    motions = [l.split(" ") for l in lines]
    motions = [(m[0], int(m[1])) for m in motions]

    return motions

def update_tail(head_x, head_y, tail_x, tail_y) -> Tuple[int, int]:
    delta_x = head_x - tail_x
    delta_y = head_y - tail_y

    if abs(delta_x) <= 1 and abs(delta_y) <= 1:
        return tail_x, tail_y

    elif abs(delta_x) > 1 and abs(delta_y) == 1:
        if delta_y < 0:
            tail_y -= 1
        else:
            tail_y += 1

    elif abs(delta_x) == 1 and abs(delta_y) > 1:
        if delta_x < 0:
            tail_x -= 1
        else:
            tail_x += 1

    elif abs(delta_x) > 1 and abs(delta_y) <= 1:
        if delta_x < 0:
            tail_x -= 1
        else:
            tail_x += 1
    
    elif abs(delta_x) <= 1 and abs(delta_y) > 1:
        if delta_y < 0:
            tail_y -= 1
        else:
            tail_y += 1

    return update_tail(head_x, head_y, tail_x, tail_y)

def process_motions(motions: List[Tuple[str, int]]) -> int:
    head_x: int = 0
    head_y: int = 0
    tail_x: int = 0
    tail_y: int = 0

    tail_positions: Set[Tuple[int, int]] = set()
    tail_positions.add((tail_x, tail_y))
    for (direction, num_movements) in motions:
        for i in range(num_movements):
            
            if direction == "R":
                head_x += 1
            elif direction == "U":
                head_y += 1
            elif direction == "L":
                head_x -= 1
            elif direction == "D":
                head_y -= 1
            
            tail_x, tail_y = update_tail(head_x, head_y, tail_x, tail_y)
            tail_positions.add((tail_x, tail_y))

    return len(tail_positions)

class Rope:
    def __init__(self, knots, start_pos=(0, 0)):
        self.

if __name__ == "__main__":
    main()