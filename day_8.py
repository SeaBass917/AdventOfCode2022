

def part_1():
    with open("data/data_8") as fp_in:
        buffer = fp_in.read()
        
        table = [[int(c) for c in line] for line in buffer.split("\n")]

        N = len(table)
        M = len(table[0])

        invisible_cnt = 0
        for i in range(1, N-1):
            for j in range(1, M-1):

                val = table[i][j]

                # UP
                is_visible = True
                for ii in range(0, i):
                    if val <= table[ii][j]:
                        is_visible = False
                        break
                if is_visible: continue

                # LEFT
                is_visible = True
                for jj in range(0, j):
                    if val <= table[i][jj]:
                        is_visible = False
                        break
                if is_visible: continue
                
                # DOWN
                is_visible = True
                for ii in range(i+1, N):
                    if val <= table[ii][j]:
                        is_visible = False
                        break
                if is_visible: continue

                # RIGHT
                is_visible = True
                for jj in range(j+1, M):
                    if val <= table[i][jj]:
                        is_visible = False
                        break
                if is_visible: continue

                invisible_cnt += 1                

        print( "Part 1:", M*N - invisible_cnt )

def part_2():
    with open("data/data_8") as fp_in:
        buffer = fp_in.read()
        
        table = [[int(c) for c in line] for line in buffer.split("\n")]

        N = len(table)
        M = len(table[0])

        scenic_score_max = 1
        for i in range(0, N):
            for j in range(0, M):

                scenic_score = 1
                val = table[i][j]

                # UP
                views = 0
                for ii in range(i-1, -1, -1):
                    views += 1
                    if val <= table[ii][j]: break
                scenic_score *= views

                # LEFT
                views = 0
                for jj in range(j-1, -1, -1):
                    views += 1
                    if val <= table[i][jj]: break
                scenic_score *= views
                
                # DOWN
                views = 0
                for ii in range(i+1, N):
                    views += 1
                    if val <= table[ii][j]: break
                scenic_score *= views

                # RIGHT
                views = 0
                for jj in range(j+1, M):
                    views += 1
                    if val <= table[i][jj]: break
                scenic_score *= views

                scenic_score_max = max(scenic_score_max, scenic_score)           

        print( "Part 2:", scenic_score_max )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()