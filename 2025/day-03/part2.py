
def main():
  with open("input.txt") as f:
    lines = f.readlines()

  total = 0
  for line in lines:
    joltage = process_line(line)
    total += joltage

  print()
  print(total)

def process_line(line):
  # starting numbers
  p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  p_max = assemble_joltage(line, p)
  # consider every number after initial set
  # i is position of new number to be considered
  for i in range(12, len(line) - 1):
    # insert i into set of numbers from right to left
    # to determine if resulting number is larger than current max
    # print(i, line[i])
    local = p.copy()
    local_max = assemble_joltage(line, local)
    for j in range(11, -1, -1):
      # print(j)
      local_2 = p.copy()
      local_2.remove(p[j])
      local_2.append(i)
      local_2_j = assemble_joltage(line, local_2)
      # print(local, local_2)
      # print(local_max, local_2_j, local_2_j > local_max)
      if local_2_j > local_max:
        local = local_2
        local_max = local_2_j

    p = local
    p_max = local_max

  return p_max


def assemble_joltage(line, p):
  j = ""
  for p in p:
    j += line[p]
  return int(j)



if __name__ == "__main__":
  main()
