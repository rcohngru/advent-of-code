# this is my first pass. going to try and clean this up/optimize a bit

E = 'E'
N = 'N'
W = 'W'
S = 'S'
WALL = '#'

ROT_CLOCK = {
  N: E,
  E: S,
  S: W,
  W: N
}

ROT_COUNTER = {
  N: W,
  E: N,
  S: E,
  W: S
}

OPP = {
  N: S,
  E: W,
  S: N,
  W: E
}

STEP = {
  N: (-1, 0),
  E: (0, 1),
  S: (1, 0),
  W: (0, -1)
}

def rot90(dir, clockwise):
  if clockwise:
    return ROT_CLOCK[dir]
  else:
    return ROT_COUNTER[dir]

def step(row, col, dir):
  drow, dcol = STEP[dir]
  return row + drow, col + dcol, dir


def build_graph(M, start_row, start_col, start_dir):
  graph = {}

  processed_nodes = set()
  nodes = [(start_row, start_col, start_dir)]
  while len(nodes) > 0:
    curr = nodes.pop()
    if curr not in graph:
      graph[curr] = {}

    next = step(*curr)
    if M[next[0]][next[1]] != WALL:
      graph[curr][next] = 1
      if next not in processed_nodes:
        nodes.append(next)

    clock = rot90(curr[2], clockwise=True)
    next_clock = (curr[0], curr[1], clock)
    graph[curr][next_clock] = 1000
    if next_clock not in processed_nodes:
      nodes.append(next_clock)

    counter = rot90(curr[2], clockwise=False)
    next_counter = (curr[0], curr[1], counter)
    graph[curr][next_counter] = 1000
    if next_counter not in processed_nodes:
      nodes.append(next_counter)

    processed_nodes.add(curr)

  return graph


def main():
  M, (start_row, start_col), (end_row, end_col) = parse_input()

  start = (start_row, start_col, E)
  G = build_graph(M, *start)

  node_distances = {
    (start_row, start_col, E): {
      "prior": set(),
      "distance": 0
    }
  }

  nodes = [start]
  while len(nodes) > 0:
    curr = nodes.pop()
    if curr[0] == end_row and curr[1] == end_col:
      continue
    curr_node_distance = node_distances[curr]["distance"]

    next_nodes = G[curr].items()
    for next_node, weight in next_nodes:
      if next_node not in node_distances:
        node_distances[next_node] = {
          "prior": {curr},
          "distance": curr_node_distance + weight
        }

        nodes.append(next_node)
        continue

      next_node_distance = node_distances[next_node]["distance"]
      if curr_node_distance + weight < next_node_distance:
        node_distances[next_node]["prior"].add(curr)
        node_distances[next_node]["distance"] = curr_node_distance + weight
        nodes.append(next_node)

  max_dist = 100000 # "cheating" by using a value higher than the distance from p1
  end_nodes = []
  for (row, col, d), item in node_distances.items():
    if row == end_row and col == end_col:
      dist = item["distance"]
      if dist < max_dist:
        end_nodes = [(row, col, d)]
        max_dist = dist
      elif dist == max_dist:
        end_nodes.append((row, col, d))

  tile_dirs = set()
  nodes = end_nodes
  while len(nodes) > 0:
    node = nodes.pop()
    tile_dirs.add(node)
    priors = node_distances[node]["prior"]
    for prior in priors:
      if prior not in tile_dirs:
        nodes.append(prior)

  tiles = set()
  for (row, col, _) in tile_dirs:
    tiles.add((row, col))

  print(len(tiles))





def disp_matrix(M):
  for m in M:
    print("".join(m))

  print()


def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  M = []
  for i, line in enumerate(lines):
    m = []
    for j, space in enumerate(line.strip()):
      if space == 'S':
        start = (i, j)
      if space == 'E':
        end = (i, j)

      m.append(space)

    M.append(m)

  return M, start, end

if __name__ == "__main__":
  main()
