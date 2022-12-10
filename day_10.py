def decode(crt_ascii_art_str : str):

    width_crt = 40
    height_crt = 6
    

def part_1():
    with open("data/data_10") as fp_in:
        buffer = fp_in.read()
        codes = [line.split(" ") for line in buffer.split("\n")]

        special_cycles = [20, 60, 100, 140, 180, 220]
        x_sum = 0
        x = 1
        pc = 0
        add_delay = 0
        for clk_cycle in range(1, max(special_cycles)+1):
            
            if clk_cycle in special_cycles:
                x_sum += x * clk_cycle

            if codes[pc][0] == "noop":
                pc+=1
            elif codes[pc][0] == "addx":
                add_delay += 1

                if add_delay == 2:
                    add_delay = 0
                    x += int(codes[pc][1])
                    pc+=1


            if len(codes) <= pc: 
                break

        print( "Part 1:", x_sum )

def part_2():
    with open("data/data_10") as fp_in:
        buffer = fp_in.read()
        codes = [line.split(" ") for line in buffer.split("\n")]

        width_crt = 40
        height_crt = 6

        screen = ['.' for _ in range(width_crt * height_crt)]

        x = 1
        pc = 0
        add_delay = 0
        clk_cycle = -1
        while pc < len(codes):
            clk_cycle += 1

            pixel = clk_cycle % (width_crt * height_crt)

            if abs((pixel % width_crt) - x) <= 1:
                screen[pixel] = '#'

            if codes[pc][0] == "noop":
                pc+=1
            elif codes[pc][0] == "addx":
                add_delay += 1

                if add_delay == 2:
                    add_delay = 0
                    x += int(codes[pc][1])
                    pc+=1

        str_out = ""
        for row in range(height_crt):
            for col in range(width_crt):
                str_out += screen[row*width_crt + col]
            str_out += "\n"

        print("Part 2:", decode(str_out))

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()