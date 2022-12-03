# A -> 65
# Z -> 90
# ...
# a -> 97
def priority(c):
    _ord = ord(c)
    if ord('a') <= _ord:
        _ord -= ord('a') - 1
    else:
        _ord -= ord('A')
        _ord += 27
    return _ord

def part_1():

    with open("data/data_3") as fp_in:
        buffer = fp_in.read()
        rucksacks = [[[c for c in text[:int(len(text)/2)]], [c for c in text[int(len(text)/2):]]] for text in buffer.split("\n")]

        com_char_ovl = [set(comp1).intersection(set(comp2)).pop() for comp1, comp2 in rucksacks]

        _sum = 0
        for c in com_char_ovl:
            _sum += priority(c)

        print( "Part 1:", _sum )

def part_2():

    with open("data/data_3") as fp_in:
        buffer = fp_in.read()
        rucksacks = [[char for char in text] for text in buffer.split("\n")]

        rucksack_groups = []

        rucksack_group = []
        for i, rucksack in enumerate(rucksacks):

            if i % 3 == 0:
                rucksack_group = set(rucksack)
            else:
                rucksack_group = rucksack_group.intersection(set(rucksack))

            if i % 3 == 2:
                rucksack_groups.append(rucksack_group.pop())

        _sum = sum([priority(c) for c in rucksack_groups])

        print( "Part 2:", _sum )


def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()