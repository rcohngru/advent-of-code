
def main():
  with open("input.txt") as f:
    lines = f.readlines()

  G = []
  spots = []
  ROWS = len(lines)
  COLS = 0
  for i, line in enumerate(lines):
    l = []
    COLS = len(line.strip())
    for j, spot in enumerate(line.strip()):
      if spot == "@":
        spots.append((i, j))
      l.append(spot)
    G.append(l)

  valid_spots = []
  for (row, col) in spots:
    occupied_neighbors = 0
    spots_to_check = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
    for r, c in spots_to_check:
      if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        continue
      if G[r][c] == "@":
        occupied_neighbors += 1
    if occupied_neighbors < 4:
      valid_spots.append((row, col))
  print(len(valid_spots))

if __name__ == "__main__":
  main()
