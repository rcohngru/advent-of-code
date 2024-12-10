FREE_SPACE = '.'

def main():
  data = parse_input()

  L = len(data)
  files = {} # file_id: (start, size)
  free_space = [] # [(start, size), ...]

  disk_space = 0
  for i in range(L):
    blocks = data[i]

    if i % 2 == 0: # then we are processing a file
      file_id = i // 2
      files[file_id] = (disk_space, int(blocks))
    else:
      free_space.append((disk_space, int(blocks)))

    disk_space += int(blocks)

  for i in sorted(files.keys(), reverse=True):
    file_start, file_size = files[i]

    for j in range(len(free_space)):
      free_space_start, free_space_size = free_space[j]

      if file_start < free_space_start:
        continue

      if file_size <= free_space_size:
        new_free_space_start = free_space_start + file_size
        new_free_space_size = free_space_size - file_size
        new_file_start = free_space_start

        free_space.pop(j)
        free_space = update_free_space(free_space, (new_free_space_start, new_free_space_size))
        free_space = update_free_space(free_space, (file_start, file_size))

        files[i] = (new_file_start, file_size)

        break

  print(checksum(files))

def update_free_space(l, free_space):
  fs_start, fs_size = free_space

  if fs_size == 0:
    return l

  for i in range(len(l)):
    start, _ = l[i]

    if fs_start < start:
      l.insert(i, (fs_start, fs_size))
      return l

  l.append((fs_start, fs_size))
  return l


def checksum(files):
  tot = 0
  for id, (start, size) in files.items():
    for i in range(size):
      tot += (start + i) * id

  return tot



def parse_input():
  with open("input.txt", "r") as f:
    data = f.read().strip()

  return data

if __name__ == "__main__":
  main()
