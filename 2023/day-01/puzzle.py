from re import sub

def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  val_sum = 0
  for line in lines:
    leftmost = find_leftmost(line)
    rightmost = find_leftmost(line[::-1])
    val_sum += int(leftmost + rightmost)

  sol = f"{val_sum}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  num_replace = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
  }
  lines = ingest_file("input.txt")
  val_sum = 0
  for line in lines:
    modified_line = line
    for k in num_replace.keys():
      modified_line = sub(k, num_replace[k], modified_line)
    leftmost = find_leftmost(modified_line)
    rightmost = find_leftmost(modified_line[::-1])

    val_sum += int(leftmost + rightmost)

  sol = f"{val_sum}"
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def find_leftmost(line):
  for c in line:
    if c.isdigit():
      return c

if __name__ == "__main__":
  main()
