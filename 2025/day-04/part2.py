
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

  total_removed = 0
  while True:
    removed_spots = []
    next_round = []
    for (row, col) in spots:
      occupied_neighbors = 0
      neighbors = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
      neighbors = [(r, c) for (r, c) in neighbors if r >= 0 and r < ROWS and c >= 0 and c < COLS] # filter to valid spots
      for r, c in neighbors:
        if G[r][c] == "@":
          occupied_neighbors += 1

      if occupied_neighbors < 4:
        removed_spots.append((row, col))
      else:
        next_round.append((row, col))

    for (row, col) in removed_spots:
      G[row][col] = "x"

    spots = next_round

    total_removed += len(removed_spots)
    if len(removed_spots) == 0:
      break

  print(total_removed)

if __name__ == "__main__":
  main()
