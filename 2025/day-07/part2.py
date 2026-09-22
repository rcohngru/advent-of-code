

def main():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  M = len(lines)
  N = len(lines[0])
  S = lines[0].index('S')

  spots = [(0, S)]
  paths = 0
  key_path = {}

  # perform a DFS on the spots with beams on them. If a spot reaches to
  # the end of the grid, we increment the number of paths and add that
  # spot to the known key_paths with a value of 1
  # if the beam eventually hits a splitter, we check the left and right values
  # at the spot of the splitter. If the number of paths from that point is not
  # already known, we process it, otherwise we just add the number of paths
  # to the running total
  # if both sides of a splitter are known, we can just add the two values together
  # and put it into the known paths at that node to save on memory
  while len(spots) > 0:
    (row, col) = spots.pop()

    reached_bottom = True
    for i in range(row + 1, M):
      if lines[i][col] == '^':
        if (i, col-1) not in key_path.keys():
          spots.append((i, col-1))
        else:
          paths += key_path[(i, col-1)]

        if (i, col+1) not in key_path.keys():
          spots.append((i, col+1))
        else:
          paths += key_path[(i, col+1)]

        if (i, col-1) in key_path.keys() and (i, col+1) in key_path.keys():
          poss_paths = key_path[(i, col-1)] + key_path[(i, col+1)]
          key_path[(row, col)] = poss_paths
        reached_bottom = False
        break

    if reached_bottom:
      paths += 1
      key_path[(row, col)] = 1

  print(paths)

if __name__ == "__main__":
  main()
