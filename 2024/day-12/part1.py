import re

UP = "up"
LEFT="left"
RIGHT="right"
DOWN="down"
DELTAS = {
    UP: (-1, 0),
    DOWN: (1, 0),
    LEFT: (0, -1),
    RIGHT: (0, 1)
}
DIRS = [UP, DOWN, LEFT, RIGHT]

def main():
    global M, R
    M = parse_input()
    rows = len(M)
    cols = len(M[0])
    # R maps a spot to a region
    R = [[None for j in range(cols)] for i in range(rows)]
    region_id = 0
    for row in range(rows):
        for col in range(cols):
            if R[row][col] == None:
                dfs((row, col), region_id)
                region_id += 1

    disp_matrix(R)

    regions = {}
    for row in range(rows):
        for col in range(cols):
            region = R[row][col]
            if region not in regions:
                regions[region] = {
                    "area": 0,
                    "perimeter": 0
                }

            outside_edges = 0
            for dir in DIRS:
                valid, spot = adj((row, col), dir)
                if not valid:
                    outside_edges += 1
                elif valid and R[spot[0]][spot[1]] != region:
                    outside_edges += 1

            regions[region]["area"] += 1
            regions[region]["perimeter"] += outside_edges

    print(regions)

    tot = 0
    for region, metrics in regions.items():
        tot += metrics["area"] * metrics ["perimeter"]
    print(tot)

def disp_matrix(M):
    for m in M:
        print(m)
    print()

def adj(loc, dir):
    maxrow = len(M)
    maxcol = len(M[0])
    row, col = loc
    d_row, d_col = DELTAS[dir]
    new_row, new_col = (row + d_row, col + d_col)
    valid_spot = False
    if 0 <= new_row < maxrow and 0 <= new_col < maxcol:
        valid_spot = True
    return valid_spot, (new_row, new_col)

def dfs(loc, region_id):
    crop = M[loc[0]][loc[1]]
    R[loc[0]][loc[1]] = region_id
    for dir in DIRS:
        valid, spot = adj(loc, dir)
        if not valid or R[spot[0]][spot[1]] != None:
            continue
        adj_crop = M[spot[0]][spot[1]]
        if adj_crop == crop:
            dfs(spot, region_id)



def parse_input():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    M = []
    for line in lines:
        M.append(re.findall('\w', line))

    return M


if __name__ == "__main__":
    main()
