
def main():

    lines = ingest_file()
    rucksacks = prepare_compartments(lines)
    shared = [compare_compartments(*r) for r in rucksacks]
    scores = [score_shared(s) for s in shared]
    total_score = sum(scores)

    print("-------- Part 1 --------")
    print(total_score)

    groups = prepare_groups(lines)
    badges = [find_badge(*g) for g in groups]
    scores = [score_shared(b) for b in badges]
    total_score = sum(scores)

    print("-------- Part 2 --------")
    print(total_score)

# -------- Part 1 --------

def ingest_file():
    with open("puzzle_data.txt", "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]

    return lines

def prepare_compartments(lines):
    rucksacks = []
    for l in lines:
        num_items = len(l)
        half = int(num_items / 2)

        c1, c2 = l[:half], l[half:]

        rucksacks.append((c1, c2))

    return rucksacks

def compare_compartments(c1, c2):

    c1_set = set(c1)
    c2_set = set(c2)

    shared = c1_set.intersection(c2_set)

    return shared.pop()

def score_shared(item):
    if item.isupper():
        reference = "A"
        modifier = 26
    else:
        reference = "a"
        modifier = 0

    score = ord(item) - ord(reference) + 1 + modifier

    return score

# -------- Part 2 --------
def prepare_groups(lines):
    group_items = []
    for i in range(0, len(lines), 3):
        group_items.append((lines[i], lines[i+1], lines[i+2]))

    return group_items

def find_badge(g1, g2, g3):
    g1_set = set(g1)
    g2_set = set(g2)
    g3_set = set(g3)

    badge = g1_set.intersection(g2_set).intersection(g3_set)

    return badge.pop()

if __name__ == "__main__":
    main()