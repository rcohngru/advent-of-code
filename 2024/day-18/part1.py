import re

def main():
  B = parse_input()
  D = 70
  ITER = 1024
  M = [['.' for i in range(D + 1)] for j in range(D + 1)]

  for i in range(ITER):
    b = B[i]
    M[b[1]][b[0]] = '#'

  for m in M:
    print("".join(m))

  bfs(M, (0, 0), (D, D))

def bfs(M, S, E):
  nodes = [S]
  M[S[0]][S[1]] = '0'

  while nodes:
    curr = nodes.pop(0)
    curr_d = int(M[curr[0]][curr[1]])

    for dir in "UDLR":
      dcol, drow = 0, 0
      match dir:
        case "U":
          drow = -1
        case "D":
          drow = 1
        case "L":
          dcol = -1
        case "R":
          dcol = 1
      next_node = (curr[0] + drow, curr[1] + dcol)
      if 0 <= next_node[0] < len(M) and 0 <= next_node[1] < len(M[0]):
        if M[next_node[0]][next_node[1]] == '.':
          M[next_node[0]][next_node[1]] = str(curr_d + 1)
          nodes.append(next_node)

  # for m in M:
  #   print(m)

  print(M[E[0]][E[1]])



def parse_input():
  with open("input.txt", "r") as f:
    data = f.read()

  B = re.findall("(\d+,\d+)", data)
  B = [list(map(int, b.split(","))) for b in B]
  return B

if __name__ == "__main__":
  main()
