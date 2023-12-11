"12 red cubes, 13 green cubes, and 14 blue cubes"

cubes = {'red': 12, 'green': 13, 'blue': 14}


def main():
    with open('input2.txt', 'r') as f:
        sum = 0
        lines = f.readlines()
        game_nr = 1
        for line in lines:
            game, game_results = line.split(':')
            game_rounds = game_results.strip().split(';')
            possible = True
            for this_round in game_rounds:
                if possible:
                    round_results = this_round.strip().split(',')
                    for result in round_results:
                        round_nr, round_color = result.strip().split(' ')
                        if cubes.get(round_color) < int(round_nr):
                            possible = False
                            break
                else:
                    break

            if possible:
                sum += game_nr
            game_nr += 1

        print(sum)


if __name__ == "__main__":
    main()
