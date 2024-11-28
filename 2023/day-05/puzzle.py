def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  seeds = [int(s) for s in lines[0].split(":")[1].strip().split()]
  maps = parse_file(lines)

  paths = []
  for seed in seeds:
    path = [seed]
    for map in maps:
      curr_src = path[-1]
      curr_dst = None
      for (s, d, r) in map:
        if s <= curr_src <= s + r - 1:
          curr_dst = d + (curr_src - s)
          break

      if curr_dst is None:
        curr_dst = curr_src
      path.append(curr_dst)
    paths.append(path)

  sol = f"{min(p[-1] for p in paths)}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  sol = f""
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def parse_file(lines):
  L = len(lines)
  row = 2
  maps = []
  while row < L:
    if "map" in lines[row]:
      row += 1
      row_len = len(lines[row])
      m = set()
      while row_len > 0:
        sdr = [int(x) for x in lines[row].split()]
        m.add((sdr[1], sdr[0], sdr[2]))
        row += 1
        if (row >= L):
          break
        row_len = len(lines[row])

      maps.append(m)
    else:
      row += 1

  return maps

if __name__ == "__main__":
  main()
