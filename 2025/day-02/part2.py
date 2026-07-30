def main():
  with open("input.txt") as f:
    data = f.read().strip()
    ranges = data.split(",")

  total = 0
  for r in ranges:
    [id1, id2] = r.split("-")
    id1, id2 = int(id1), int(id2)
    for i in range(id1, id2 + 1, 1):
      str_num = str(i)
      if validate(str_num):
        total += i
  print(total)

def validate(str_num):
  pattern_length = 1
  str_length = len(str_num)
  is_match = False
  while pattern_length < str_length:
    if str_length % pattern_length != 0:
      pattern_length += 1
      continue

    pattern = str_num[0:pattern_length]
    is_match = True
    for i in range(pattern_length, str_length, pattern_length):
      substr = str_num[i: i + pattern_length]
      if pattern != substr:
        is_match = False
        break

    if is_match:
      break
    else:
      pattern_length += 1

  return is_match

if __name__ == "__main__":
  main()
