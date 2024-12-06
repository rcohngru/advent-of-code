import numpy as np

def main():
  MAS = [
    np.array([
      ['M', '.', 'S'],
      ['.', 'A', '.'],
      ['M', '.', 'S']
    ]),
    np.array([
      ['M', '.', 'M'],
      ['.', 'A', '.'],
      ['S', '.', 'S']
    ]),
    np.array([
      ['S', '.', 'M'],
      ['.', 'A', '.'],
      ['S', '.', 'M']
    ]),
    np.array([
      ['S', '.', 'S'],
      ['.', 'A', '.'],
      ['M', '.', 'M']
    ]),
  ]
  M = parse_input()
  I, J = M.shape

  cnt = 0
  for i in range(0, I - 2):
    for j in range(0, J - 2):
      m = M[i:i+3, j:j+3].copy()
      m[0, 1] = '.'
      m[1, 0] = '.'
      m[1, 2] = '.'
      m[2, 1] = '.'

      for mas in MAS:
        if (m == mas).all():
          cnt +=1

  print(cnt)

def parse_input():
  M = []
  with open("input.txt", "r") as f:
    lines = f.readlines()

  for line in lines:
    M.append([c for c in line.strip()])

  return np.array(M)

if __name__ == "__main__":
  main()
