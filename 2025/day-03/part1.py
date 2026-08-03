
def main():
  with open("input.txt") as f:
    lines = f.readlines()

  total = 0
  for line in lines:
    m = line[0]
    m_i = 0
    for i in range(1, len(line) - 2, 1):
      if line[i] > m:
        m = line[i]
        m_i = i
    n = line[m_i + 1]
    for i in range(m_i + 1, len(line), 1):
      if line[i] > n:
        n = line[i]

    total += int(f"{m}{n}")

  print(total)




if __name__ == "__main__":
  main()
