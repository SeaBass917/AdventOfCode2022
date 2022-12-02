import enum

class RPS(enum.Enum):
    rock = 0
    paper = 1
    scissors = 2
    unk = 3

class Game(enum.Enum):
    lose = 0
    draw = 1
    win = 2
    unk = 3

def part_1():

    def convert(char):
        if char == "A": return RPS.rock
        elif char == "B": return RPS.paper
        elif char == "C": return RPS.scissors
        elif char == "X": return RPS.rock
        elif char == "Y": return RPS.paper
        elif char == "Z": return RPS.scissors
        return RPS.unk

    def score_game(you, them):
        score = 0
        
        if you == RPS.rock: 
            score += 1
        elif you == RPS.paper: 
            score += 2
        elif you == RPS.scissors: 
            score += 3
        
        delta = int(them.value) - int(you.value)

        if delta == 0:
            score += 3
        elif 0 < delta and abs(delta) == 2:
            score += 6
        elif delta < 0 and abs(delta) == 1:
            score += 6

        return score

    with open("data/data_2") as fp_in:
        buffer = fp_in.read()
        rps_games = [[convert(char) for char in text.split(" ")] for text in buffer.split("\n")]
        total_score = sum([score_game(rps_game[1], rps_game[0]) for rps_game in rps_games])

        print( "Part 2:", total_score )

def part_2():

    def convert_abc(char):
        if char == "A": return RPS.rock
        elif char == "B": return RPS.paper
        elif char == "C": return RPS.scissors
        return RPS.unk

    def convert_xyz(char):
        if char == "X": return Game.lose
        elif char == "Y": return Game.draw
        elif char == "Z": return Game.win
        return Game.unk

    def score_game(them, plan):
        score = 0

        if plan == Game.draw:
            score += 3
            you = them
        elif plan == Game.win:
            score += 6
            if them == RPS.rock:
                you = RPS.paper
            elif them == RPS.paper:
                you = RPS.scissors
            elif them == RPS.scissors:
                you = RPS.rock
        elif plan == Game.lose:
            if them == RPS.rock:
                you = RPS.scissors
            elif them == RPS.paper:
                you = RPS.rock
            elif them == RPS.scissors:
                you = RPS.paper   

        if you == RPS.rock: 
            score += 1
        elif you == RPS.paper: 
            score += 2
        elif you == RPS.scissors: 
            score += 3

        return score

    with open("data/data_2") as fp_in:
        buffer = fp_in.read()
        rps_games = [[char for char in text.split(" ")] for text in buffer.split("\n")]
        strat = [(convert_abc(rps_game[0]), convert_xyz(rps_game[1])) for rps_game in rps_games]

        total_score = sum([score_game(*game) for game in strat])

        print( "Part 2:", total_score )


def main():
    part_1()

    part_2()

if __name__ == "__main__":
    main()