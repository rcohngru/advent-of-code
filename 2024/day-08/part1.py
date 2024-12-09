def main():
  global R, C
  R, C, N = parse_input()

  antinodes = set()
  for freq in N:
    nodes = N[freq]
    L = len(nodes)
    for i in range(L):
      for j in range(i):
        n1 = nodes[i]
        n2 = nodes[j]

        is_an, an = antinode(n1, n2)
        if is_an:
          antinodes.add(an)

        is_an, an = antinode(n2, n1)
        if is_an:
          antinodes.add(an)

  print(len(antinodes))

def antinode(n1, n2):
  x1, y1 = n1
  x2, y2 = n2

  an = (
    x2 + (x2 - x1),
    y2 + (y2 - y1)
  )

  if 0 <= an[0] < R and 0 <= an[1] < C:
    return True, an
  else:
    return False, None



def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  nodes = {}
  R = len(lines)
  C = len(lines[0]) - 1
  for i, line in enumerate(lines):
    for j, c in enumerate(line.strip()):
      if c != '.':
        if c in nodes:
          nodes[c].append((i, j))
        else:
          nodes[c] = [(i, j)]
  return R, C, nodes

if __name__ == "__main__":
  main()
