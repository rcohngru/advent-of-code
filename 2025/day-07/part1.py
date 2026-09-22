def main():
  with open("input.txt", "r") as f:
    lines = f.readlines()

  N = len(lines[0])
  beam_array = [False] * N
  beam_array[lines[0].index('S')] = True
  split_ct = 0

  for line in lines[1:]:
    temp_beam_array = [False] * N
    for i, c in enumerate(line):
      if beam_array[i] and c == '^':
        split_ct += 1
        temp_beam_array[i-1] = True
        temp_beam_array[i+1] = True
        continue
      elif beam_array[i]:
        temp_beam_array[i] = True

    beam_array = temp_beam_array

  print(split_ct)


if __name__ == "__main__":
  main()
