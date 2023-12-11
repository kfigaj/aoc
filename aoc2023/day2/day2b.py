def dict_power(min_possile):
    power_result = 1
    for k, v in min_possile.items():
        power_result *= v
    return power_result


def main():
    with open('input2.txt', 'r') as f:
        sum = 0
        lines = f.readlines()
        for line in lines:
            game, game_results = line.split(':')
            game_rounds = game_results.strip().split(';')
            min_possible = {}
            for this_round in game_rounds:
                round_results = this_round.strip().split(',')
                for result in round_results:
                    round_nr, round_color = result.strip().split(' ')
                    if min_possible.get(round_color, 0) < int(round_nr):
                        min_possible[round_color] = int(round_nr)

            sum += dict_power(min_possible)
        print(sum)


if __name__ == "__main__":
    main()
