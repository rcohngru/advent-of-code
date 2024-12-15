import re

N = 100
X = 101
Y = 103

div_V = X // 2
div_H = Y // 2

def main():
  R0 = parse_input()
  RN = []


  for r in R0:
    x0, y0 = r[0]
    vx, vy = r[1]

    xN = x0 + N * vx
    yN = y0 + N * vy

    xN = xN % X
    yN = yN % Y
    RN.append((xN, yN))

  q1, q2, q3, q4 = 0, 0, 0, 0
  for (xN, yN) in RN:
    if 0 <= xN < div_V and 0 <= yN < div_H:
      q1 += 1
    elif 0 <= xN < div_V and div_H < yN < Y:
      q3 += 1
    elif div_V < xN < X and 0 <= yN < div_H:
      q2 += 1
    elif div_V < xN < X and div_H < yN < Y:
      q4 += 1

  print(q1, q2, q3, q4)
  print(q1 * q2 * q3 * q4)



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
