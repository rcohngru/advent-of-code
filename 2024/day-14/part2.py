import re

N = 100
X = 101
Y = 103

div_V = X // 2
div_H = Y // 2

def main():
  R0 = parse_input()

  for i in range(10000):
    Rn = []
    for r in R0:
      x0, y0 = r[0]
      vx, vy = r[1]

      xN = x0 + i * vx
      yN = y0 + i * vy

      xN = xN % X
      yN = yN % Y
      Rn.append((xN, yN))

    # this is so dumb but dump the arrangements to an alignment file
    # with the iteration and scan the file until tree is found
    disp_map(Rn, i)


def disp_map(R, i):
  M = [['.' for j in range(Y)] for i in range(X)]

  for r in R:
    M[r[0]][r[1]] = '*'

  with open("out.txt", "a") as f:
      f.write(f"{i}\n")

  for m in M:
    with open("out.txt", "a") as f:
      f.write("".join(m) + "\n")



def parse_input():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  R = []
  for line in lines:
    data = list(map(int, re.findall("(-?\d+)", line)))
    R.append(
      (
        (data[0], data[1]),
        (data[2], data[3])
      )
    )
  return R


if __name__ == "__main__":
  main()
