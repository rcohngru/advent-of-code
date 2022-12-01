# For a challenge, not using any non-native Python libraries

def main():
    # Part 1
    print("---------- Part 1 ----------")
    lines = ingest_file()
    elf_calories = prepare_elves(lines)
    max_calories = max(elf_calories)
    elf_position = elf_calories.index(max_calories)

    print(f"The Elf carrying the most calories is Elf #{elf_position + 1} carrying {max_calories} calories.")

    # Part 2
    print("---------- Part 2 ----------")
    n = 3
    elves, top_n_cals = top_n_elves(elf_calories, n)
    print(f"The top {n} elves carrying the most calories were:")
    for e, c, in zip(elves, top_n_cals):
        print(f"\t- Elf #{e + 1}: {c} calories")

    print(f"The total calories carried by these elves is: {sum(top_n_cals)} calories")

### Code for Part 1 ###
def ingest_file():
    f = open("puzzle_data.txt", "r")
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

def prepare_elves(lines):
    elf_calories = []
    current_elf = 0
    for l in lines:
        if l == '':
            elf_calories.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(l)

    return elf_calories

### Code for Part 2 ###
def top_n_elves(elf_calories, n):
    sorted_calories = sorted(elf_calories, reverse=True)
    top_n_cals = sorted_calories[:n]
    elves = [elf_calories.index(c) for c in top_n_cals]

    return elves, top_n_cals


if __name__ == "__main__":
    main()