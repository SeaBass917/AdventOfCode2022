from math import prod
import re

class Monkey:

    def __init__(self, stanza):
        lines = [line.strip() for line in stanza.split("\n")]
        
        self.monkey_id = int(re.findall(r"Monkey (\d+):", lines[0])[0])
        self.items = [int(item_id) for item_id in lines[1].split(": ")[1].split(", ")]
        self.operation = re.findall(r"new = (old|\d+) (\*|\+) (old|\d+)", lines[2])[0]
        self.divisible_test = int(re.findall(r"divisible by (\d+)", lines[3])[0])
        self.throw_if_true_id = int(re.findall(r"throw to monkey (\d+)", lines[4])[0])
        self.throw_if_false_id = int(re.findall(r"throw to monkey (\d+)", lines[5])[0])

        self.inspect_cnt = 0

    def process_item(self, item: int):
        self.inspect_cnt += 1

        lhs = item if self.operation[0] == "old" else int(self.operation[0])
        rhs = item if self.operation[2] == "old" else int(self.operation[2])
        
        if self.operation[1] == "+":
            return (lhs + rhs)
        elif self.operation[1] == "*":
            return (lhs * rhs)

        raise RuntimeError("Ahhh!")

    def catch_item(self, item: int):
        self.items.append(item)

    @staticmethod
    def compute_monkey_business(monkeys : dict):
        inspect_cnts = [monkey.inspect_cnt for monkey in monkeys.values()]
        inspect_cnts.sort(reverse=True)
        return inspect_cnts[0] * inspect_cnts[1]

def is_divisible(a, b):
    return a % b == 0

def part_1():
    with open("data/data_11a") as fp_in:
        buffer = fp_in.read()
        stanzas = buffer.split("\n\n")

        NUM_ROUNDS = 20

        monkeys = {}
        monkey_ids = []
        for stanza in stanzas:
            monkey = Monkey(stanza=stanza)
            monkey_ids.append(monkey.monkey_id)
            monkeys[monkey.monkey_id] = monkey
        
        for _ in range(NUM_ROUNDS):
            for monkey_id in monkey_ids:
                monkey = monkeys[monkey_id]
                for item in monkey.items:
                    worry = int(monkey.process_item(item) / 3)
                    if is_divisible(worry, monkey.divisible_test):
                        monkeys[monkey.throw_if_true_id].catch_item(worry)
                    else:
                        monkeys[monkey.throw_if_false_id].catch_item(worry)

                # we threw tha tings
                monkey.items = []

        print( "Part 1:", Monkey.compute_monkey_business(monkeys) )

def part_2():
    with open("data/data_11") as fp_in:
        buffer = fp_in.read()
        stanzas = buffer.split("\n\n")

        NUM_ROUNDS = 10_000

        monkeys = {}
        monkey_ids = []
        for stanza in stanzas:
            monkey = Monkey(stanza=stanza)
            monkey_ids.append(monkey.monkey_id)
            monkeys[monkey.monkey_id] = monkey
            
        mod_factor = prod([monkey.divisible_test for monkey in monkeys.values()])
        
        for _ in range(NUM_ROUNDS):
            for monkey_id in monkey_ids:
                monkey = monkeys[monkey_id]
                for item in monkey.items:
                    worry = monkey.process_item(item) % mod_factor
                    if is_divisible(worry, monkey.divisible_test):
                        monkeys[monkey.throw_if_true_id].catch_item(worry)
                    else:
                        monkeys[monkey.throw_if_false_id].catch_item(worry)

                # we threw tha tings
                monkey.items = []

        print( "Part 2:", Monkey.compute_monkey_business(monkeys) )

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()