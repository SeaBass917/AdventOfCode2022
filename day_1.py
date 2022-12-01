

def main():
    with open("data/data_1") as fp_in:
        buffer = fp_in.read()
        calories_list = [sum([int(num) for num in text.split("\n")]) for text in buffer.split("\n\n")]

        calories_list.sort(reverse=True)

        print( "Part 1:", calories_list[0] )

        print( "Part 2:", sum(calories_list[:3]) )

if __name__ == "__main__":
    main()