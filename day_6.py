def part_1():
    with open("data/data_6") as fp_in:
        buffer = fp_in.read()

        char_set = []
        for i, c in enumerate(buffer):
            if c in char_set:
                char_set = [c]
            else:
                char_set.append(c)
            
            if 4 == len(char_set):

                print( "Part 1:", i+1 )
                break

def part_2():
    with open("data/data_6") as fp_in:
        buffer = fp_in.read()

        char_hist = {}
        i_l = 0
        for i_r, c in enumerate(buffer):
            if c not in char_hist: 
                char_hist[c] = 1
            else:
                char_hist[c]+=1

            while 1 < char_hist[c]:
                char_hist[buffer[i_l]] -= 1
                i_l += 1
            
            if 14 == sum(char_hist.values()):

                print( "Part 2:", i_r+1 )
                break

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()