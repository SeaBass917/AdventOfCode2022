import json
import enum

class BBool(enum.Enum):
    false = 0
    true = 1
    unk = 2

def is_lt(signal_0, signal_1):

    # Convert to list type
    if type(signal_0) != list and type(signal_1) == list:
        return is_lt([signal_0], signal_1)
    elif type(signal_0) == list and type(signal_1) != list:
        return is_lt(signal_0, [signal_1])
    
    N0 = len(signal_0)
    N1 = len(signal_1)

    for i in range(max(N0, N1)):
        if N0 <= i: return BBool.true
        if N1 <= i: return BBool.false

        left = signal_0[i]
        right = signal_1[i]

        if type(left) != list and type(right) != list:
            if left < right:
                return BBool.true
            elif right < left:
                return BBool.false
        else:
            status = is_lt(signal_0[i], signal_1[i])
            if status != BBool.unk:
                return status

    return BBool.unk

def part_1():
    with open("data/data_13") as fp_in:
        buffer = fp_in.read()

        signal_pairs = [[json.loads(line) for line in stanza.split("\n")] for stanza in buffer.split("\n\n")]

        in_order_pairs = []
        for i, (signal_0, signal_1) in enumerate(signal_pairs):
            if BBool.true == is_lt(signal_0, signal_1):
                in_order_pairs.append(i+1)

        print( "Part 1:", sum(in_order_pairs) )

def part_2():
    with open("data/data_13") as fp_in:
        buffer = fp_in.read()
        signals = [json.loads(line) for line in buffer.split("\n") if line]
        
        def quick_sort(array):
            """Sort the array by using quicksort."""

            less = []
            equal = []
            greater = []

            if 1 < len(array):
                pivot = array[0]
                for x in array:
                    if x == pivot:
                        equal.append(x)
                    elif BBool.true == is_lt(x, pivot):
                        less.append(x)
                    else:
                        greater.append(x)
                return quick_sort(less)+equal+quick_sort(greater)
            else:
                return array

        # add divider packets
        signals.append([[2]])
        signals.append([[6]])

        signals = quick_sort(signals)

        decoder_key = 1
        for i, signal in enumerate(signals):
            if signal == [[2]] or signal == [[6]]:
                decoder_key *= i+1
        
        print( "Part 2:", decoder_key )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()