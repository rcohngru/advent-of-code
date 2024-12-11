
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

DELTAS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

def main():
    global M
    M, T = parse_input()

    global next_spots
    next_spots = {}

    global MAX_ROWS, MAX_COLS
    MAX_ROWS = len(M)
    MAX_COLS = len(M[0])

    for row in range(MAX_ROWS):
        for col in range(MAX_COLS):
            curr_height = M[row][col]
            next_spots[(row, col)] = set()

            for dir in DIRECTIONS:
                adj_height = get_adjacent_height((row, col), dir)
                if adj_height and (adj_height - curr_height == 1):
                    next_spot = adj_spot((row, col), dir)
                    next_spots[(row, col)].add(next_spot)

    tot = 0
    for row, col in T:
        unique_paths = travel_path((row, col))

        tot += unique_paths
    print(tot)

def travel_path(loc):
    row, col = loc
    height = M[row][col]

    unique_paths = 0
    if height == 9:
        unique_paths += 1
    else:
        spots_to_visit = next_spots[(row, col)]
        for spot in spots_to_visit:
            unique_paths += travel_path(spot)

    return unique_paths



def adj_spot(loc, dir):
    row, col = loc
    drow, dcol = DELTAS[dir]

    new_row = row + drow
    new_col = col + dcol

    return (new_row, new_col)


def get_adjacent_height(loc, dir):
    adj_row, adj_col = adj_spot(loc, dir)

    if 0 <= adj_row < MAX_ROWS and 0 <= adj_col < MAX_COLS:
        return M[adj_row][adj_col]
    else:
        return None # bad?

def parse_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    M = [] # 2D array of map
    T = [] # list of trailhead locations (row, col)

    for row, line in enumerate(lines):
        m = []
        for col, height in enumerate(line.strip()):
            height = int(height)
            if height == 0:
                T.append((row, col))
            m.append(height)
        M.append(m)
    return M, T


if __name__ == "__main__":
    main()
