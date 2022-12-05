import re


def parser_stacks(buffer : str):
    COL_WIDTH = 3

    lines = buffer.split("\n")

    order = [col.strip() for col in lines.pop().split(" "*COL_WIDTH)]
    col_cnt = len(order)

    stacks = {key : [] for key in order}

    for line in lines:
        for i, key in zip(range(col_cnt), order):
            i_beg = i + i*COL_WIDTH
            box = line[i_beg: i_beg + COL_WIDTH].strip()

            if box:
                stacks[key].append(box[1])

    for stack in stacks.values():
        stack.reverse()

    return stacks, order

def parser_moves(buffer : str):

    moves = []
    for line in buffer.split("\n"):
        matches = re.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
        moves.append((int(matches[0]), matches[1], matches[2]))

    return moves

def parser(buffer_1 : str, buffer_2 : str):
    stacks, order = parser_stacks(buffer_1)
    moves = parser_moves(buffer_2)
    return stacks, moves, order

def part_1():
    with open("data/data_5") as fp_in:
        buffer = fp_in.read()
        buffer_1, buffer_2 = buffer.split("\n\n")

        stacks, operations, order = parser(buffer_1, buffer_2)

        for (cnt, i_src, i_dst) in operations:
            for _ in range(cnt):
                stacks[i_dst].append(stacks[i_src].pop())

        print( "Part 1:", "".join([stacks[key][-1] for key in order]) )

def part_2():
    with open("data/data_5") as fp_in:
        buffer = fp_in.read()
        buffer_1, buffer_2 = buffer.split("\n\n")

        stacks, operations, order = parser(buffer_1, buffer_2)

        for (cnt, i_src, i_dst) in operations:
            crates = []
            for _ in range(cnt):
                crates.append(stacks[i_src].pop())

            crates.reverse()
            stacks[i_dst] += crates

        print( "Part 2:", "".join([stacks[key][-1] for key in order]) )


def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()