def tail_adjust(h, t):
        
    delta_ud = t[0] - h[0]
    delta_lr = t[1] - h[1]

    ud_factor = 0
    if abs(delta_ud) == 2 or (abs(delta_lr) == 2 and 0 < abs(delta_ud)):
        ud_factor = 1 if delta_ud < 0 else -1
        
    lr_factor = 0
    if abs(delta_lr) == 2 or (abs(delta_ud) == 2 and 0 < abs(delta_lr)):
        lr_factor = 1 if delta_lr < 0 else -1

    return t[0] + ud_factor, t[1] + lr_factor

def move_head(h, dir):
    if dir == 'L':
        return h[0], h[1] - 1
    elif dir == 'R':
        return h[0], h[1] + 1
    elif dir == 'U':
        return h[0] + 1, h[1]
    elif dir == 'D':
        return h[0] - 1, h[1]

def part_1():
    with open("data/data_9") as fp_in:
        buffer = fp_in.read()
        input = [[line.split(" ")[0], int(line.split(" ")[1])] for line in buffer.split('\n')]
        
        t = (0,0)
        h = (0,0)
        t_visits = set([t])
        for dir, cnt in input:
            for _ in range(cnt):
                h = move_head(h, dir)
                t = tail_adjust(h, t)
                t_visits.add(t)
        
        print( "Part 1:", len(t_visits) )

def part_2():
    with open("data/data_9") as fp_in:
        NUM_KNOTS = 9
        buffer = fp_in.read()
        input = [[line.split(" ")[0], int(line.split(" ")[1])] for line in buffer.split('\n')]
        
        knot_list = [(0,0) for _ in range(NUM_KNOTS)]
        t_visits = set([knot_list[NUM_KNOTS-1]])
        for dir, cnt in input:
            for _ in range(cnt):

                knot_list[0] = move_head(knot_list[0], dir)

                for i in range(1, NUM_KNOTS):
                    knot_list[i] = tail_adjust(knot_list[i-1], knot_list[i])

                t_visits.add(knot_list[NUM_KNOTS-1])

        print( "Part 2:", len(t_visits) )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()