FREE_SPACE = '.'

def main():
  data = parse_input()

  L = len(data)
  file_system = []

  for i in range(L):
    blocks = data[i]

    if i % 2 == 0:
      file_system.extend([str(i // 2)] * int(blocks))
    else:
      file_system.extend([FREE_SPACE] * int(blocks))

  left = 0
  right = len(file_system) - 1
  while left < right:
    r = file_system[right]
    l = file_system[left]

    if l == FREE_SPACE and r != FREE_SPACE:
      file_system[left] = r
      file_system[right] = l
      right -= 1
      left += 1
    elif l == FREE_SPACE and r == FREE_SPACE:
      right -= 1
    elif l != FREE_SPACE and r == FREE_SPACE:
      right -= 1
      left += 1
    else: # l != FREE_SPACE and r != FREE_SPACE
      left += 1

  print(checksum(file_system))



def checksum(l):
  tot = 0
  for i, n in enumerate(l):
    if n == FREE_SPACE:
      break
    tot += i * int(n)

  return tot



def parse_input():
  with open("input.txt", "r") as f:
    data = f.read().strip()

  return data

if __name__ == "__main__":
  main()
