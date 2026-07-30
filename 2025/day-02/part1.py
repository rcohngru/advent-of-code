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
      digits = len(str_num)
      if digits % 2 != 0:
        continue

      if str_num[:digits // 2] == str_num[digits // 2:]:
        total += i

  print(total)

if __name__ == "__main__":
  main()
