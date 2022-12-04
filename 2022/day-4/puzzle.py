
def main():

    lines = ingest_file()
    pairs = create_pairs(lines)
    full_overlaps = [pair_fully_overlaps(*p) for p in pairs]
    total_full_overlaps = sum(full_overlaps)

    print("-------- Part 1 --------")
    print(total_full_overlaps)

    partial_overlaps = [pair_partial_overlaps(*p) for p in pairs]
    total_partial_overlaps = sum(partial_overlaps)

    print("-------- Part 2 --------")
    print(total_partial_overlaps)



def ingest_file():
    with open("puzzle_data.txt", "r") as f:
        lines = f.readlines()

    lines = [l.strip() for l in lines]

    return lines

def create_pairs(lines):

    pairs = []
    for l in lines:
        p1, p2 = l.split(",")

        p1 = p1.split("-")
        p2 = p2.split("-")
        p1_sections = set(
            [i for i in range(
                int(p1[0]), int(p1[1]) + 1
                )]
        )

        p2_sections = set(
            [i for i in range(
                int(p2[0]), int(p2[1]) + 1
                )]
        )

        pairs.append((p1_sections, p2_sections))

    return pairs

def pair_fully_overlaps(p1: set, p2: set):
    # returns 1 if one of the pairs is a subset of the other, else returns 0

    if p1.issubset(p2) or p2.issubset(p1):
        return 1
    else:
        return 0

def pair_partial_overlaps(p1: set, p2: set):
    # returns 1 if the pairs partially (or fully) overlap, else returns 0

    ix = p1.intersection(p2)

    if len(ix) > 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    main()