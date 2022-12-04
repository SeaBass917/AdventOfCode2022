def part_1():
    with open("data/data_4") as fp_in:
        buffer = fp_in.read()
        pairs = [[[int(x) for x in rng.split("-")] for rng in line.split(",")] for line in buffer.split("\n")]
        
        _sum = 0
        for pair1, pair2 in pairs:
            if ((pair1[0] <= pair2[0]) and (pair2[1] <= pair1[1])) or ((pair2[0] <= pair1[0]) and (pair1[1] <= pair2[1])):
                _sum += 1

        print( "Part 1:", _sum )

def part_2():
    with open("data/data_4") as fp_in:
        buffer = fp_in.read()
        pairs = [[[int(x) for x in rng.split("-")] for rng in line.split(",")] for line in buffer.split("\n")]
        
        _sum = 0
        for pair1, pair2 in pairs:
            if ((pair2[0] <= pair1[1]) and (pair1[0] <= pair2[1])) or \
                ((pair1[0] <= pair2[0]) and (pair2[1] <= pair1[1])) or \
                ((pair2[0] <= pair1[0]) and (pair1[1] <= pair2[1])) or \
                ((pair1[0] <= pair2[1]) and (pair2[0] <= pair1[1])):
                _sum += 1

        print( "Part 2:", _sum )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()