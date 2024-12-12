def main():
    S = parse_input()

    for i in range(25):
        S = process_stones(S)

    tot = 0
    for _, occ in S.items():
        tot += occ
    print(tot)

def process_stones(S):
    S2 = {}
    for num, occ in S.items():
        num_size = len(num)
        if num == '0':
            S2['1'] = S2.get('1', 0) + occ
        elif num_size % 2 == 0:
            mid = num_size // 2
            l, r = str(int(num[:mid])), str(int(num[mid:]))

            S2[l] = S2.get(l, 0) + occ
            S2[r] = S2.get(r, 0) + occ
        else:
            mult = str(int(num) * 2024)
            S2[mult] = S2.get(mult, 0) + occ

    return S2


def parse_input():
    with open("input.txt", "r") as f:
        data = f.read()

    nums = data.split()
    S = {}
    for num in nums:
        S[num] = S.get(num, 0) + 1

    return S

if __name__ == "__main__":
    main()
