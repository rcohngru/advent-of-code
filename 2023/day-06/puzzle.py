def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  times = map(int, lines[0].split()[1:])
  distances = map(int, lines[1].split()[1:])
  moe = 1
  for t, d in zip(times, distances):
    poss = 0
    for i in range(t):
      dist = i * (t - i)
      if dist > d:
        poss += 1

    moe *= poss


  sol = f"{moe}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  lines = ingest_file("input.txt")
  time = int("".join(lines[0].split()[1:]))
  distance = int("".join(lines[1].split()[1:]))
  poss = 0
  for i in range(time):
    dist = i * (time - i)
    if dist > distance:
      poss += 1
  sol = f"{poss}"
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

if __name__ == "__main__":
  main()
