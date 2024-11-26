def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():

  sol = f""
  print(f"The solution for Part 1 is: {sol}")

def part_2():

  sol = f""
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

if __name__ == "__main__":
  main()
