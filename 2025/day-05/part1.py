import re
def main():
  with open("input.txt", "r") as f:
    file = f.read()

  fresh_ranges = re.findall("^\d+-\d+$", file, flags=re.MULTILINE) # find ranges in file
  ingredient_ids = re.findall("^\d+$", file, flags=re.MULTILINE) # find individual ingredient ids in file

  id_ranges = []
  for r in fresh_ranges:
    [s, e] = r.split("-")
    id_ranges.append((int(s), int(e)))

  fresh_cnt = 0
  for ing in ingredient_ids:
    ing = int(ing)
    fresh = False
    for r in id_ranges:

      if ing >= r[0] and ing <= r[1]:
        fresh = True
        break

    if fresh:
      fresh_cnt += 1

  print(fresh_cnt)

if __name__ == "__main__":
  main()
