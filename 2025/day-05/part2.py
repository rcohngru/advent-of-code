import re
def main():
  with open("input.txt", "r") as f:
    file = f.read()

  fresh_ranges = re.findall("^\d+-\d+$", file, flags=re.MULTILINE) # find ranges in file
  unsorted_ranges = []
  for r in fresh_ranges:
    [s, e] = r.split("-")
    t = (int(s), int(e))
    unsorted_ranges.append(t)

  # sort ranges based on Sn >= Sn-1 and En >= En-1
  sorted_ranges = insertion_sort(unsorted_ranges)
  uniq_ids = 0
  prev_high = 0
  for i in range(0, len(sorted_ranges)):
    s_i, e_i = sorted_ranges[i]
    if i == 0:
      uniq_ids += e_i - s_i + 1
      prev_high = e_i
      continue

    # the current range is within the bounds of a previous, so no new values needed
    if s_i <= prev_high and e_i <= prev_high:
      uniq_ids += 0
    # the current range overlaps with the bounds of a previous, so we add new values using the prior high value
    elif s_i <= prev_high and e_i > prev_high:
      uniq_ids += e_i - prev_high
      prev_high = e_i
    # the current range is disparate from the previous, so we can add all new values
    else:
      uniq_ids += e_i - s_i + 1
      prev_high = e_i

  print(uniq_ids)

def insertion_sort(arr):
  for i in range(1, len(arr)):
    (s, e) = arr[i]
    j = i - 1

    while j >= 0:
      # if the prior element is smaller than current, then we don't need to move
      if arr[j][0] < s:
        break
      # if the prior element is the same size as current
      # and the end of the range is smaller than current, then we don't need to move
      if arr[j][0] == s and arr[j][1] < e:
        break

      arr[j + 1] = arr[j]
      j -= 1

    arr[j + 1] = (s, e)

  return arr

if __name__ == "__main__":
  main()
