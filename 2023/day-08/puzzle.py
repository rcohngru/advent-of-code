import math

def main():
  print("------------- Part 1 -------------")
  part_1()
  print("------------- Part 2 -------------")
  part_2()


def part_1():
  lines = ingest_file("input.txt")
  dirs = lines[0]

  network = {}

  for line in lines[2:]:
    (node, inst) = line.split(" = ")
    l, r = inst.strip("()").split(", ")
    network[node.strip()] = (l.strip(), r.strip())

  L = len(dirs)
  curr_dir = 0
  steps = 0
  next_node = 'AAA'
  while next_node != 'ZZZ':
    dir = dirs[curr_dir]
    if dir == "L":
      next_node = network[next_node][0]
    else:
      next_node = network[next_node][1]

    curr_dir += 1
    if curr_dir == L:
      curr_dir = 0

    steps += 1

  sol = f"{steps}"
  print(f"The solution for Part 1 is: {sol}")

def part_2():
  lines = ingest_file("input.txt")
  dirs = [l for l in lines[0]]

  curr_nodes = []
  network = {}
  for line in lines[2:]:
    (node, inst) = line.split(" = ")
    l, r = inst.strip("()").split(", ")
    network[node.strip()] = (l.strip(), r.strip())
    if node.endswith('A'):
      curr_nodes.append(node)


  # the solve for part 2 is tricky
  # its unfeasible to try and find the answer by iterating over
  # everything, but for each start node theres a repeatable number of loops
  # that it will take until it reaches the final node
  # so all we need to do is find least common multiple of them
  node_steps = []
  for next_node in curr_nodes:
    inst = dirs.copy()
    steps = 0
    while not next_node.endswith('Z'):
      steps += 1
      dir = inst.pop(0)
      inst.append(dir)
      if dir == "L":
        next_node = network[next_node][0]
      else:
        next_node = network[next_node][1]

    node_steps.append(steps)

  lcm = math.lcm(*node_steps)

  sol = f"{lcm}"
  print(f"The solution for Part 2 is: {sol}")

def ingest_file(file):
    f = open(file, "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

if __name__ == "__main__":
  main()
