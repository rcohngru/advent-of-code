import re
import numpy as np

def main():

  M = parse_input()

  lines_to_check = []

  for i in range(M.shape[0]):
    hor = M[i]
    diag = M.diagonal(-1 * i)
    diag_rev = np.fliplr(M).diagonal(-1 * i)

    lines_to_check.append(hor)
    lines_to_check.append(hor[::-1])
    lines_to_check.append(diag)
    lines_to_check.append(diag[::-1])
    lines_to_check.append(diag_rev)
    lines_to_check.append(diag_rev[::-1])

  for i in range(M.shape[1]):
    ver = M[:, i]
    lines_to_check.append(ver)
    lines_to_check.append(ver[::-1])

    if i != 0:
      diag = M.diagonal(i)
      diag_rev = np.fliplr(M).diagonal(i)

      lines_to_check.append(diag)
      lines_to_check.append(diag[::-1])
      lines_to_check.append(diag_rev)
      lines_to_check.append(diag_rev[::-1])

  occurrences = 0
  for line in lines_to_check:
    occurrences += count_occurrences("".join(line))

  print(occurrences)

def count_occurrences(line):
  matches = re.findall('XMAS', line)
  cnt = len(matches)
  return cnt


def parse_input():
  M = []
  with open("input.txt", "r") as f:
    lines = f.readlines()

  for line in lines:
    M.append([c for c in line.strip()])

  return np.array(M)

if __name__ == "__main__":
  main()
