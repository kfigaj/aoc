def check_if_part_number(engine, digit_row, first_digit_sign, last_digit_sign):
    for i in range(digit_row - 1, digit_row + 2):
        for j in range(first_digit_sign - 1, last_digit_sign + 2):
            value = engine[i][j]
            if not value.isdigit() and value != '.':
                return True
    return False


def parse_number(engine, digit_row, j, max_j):
    number = engine[digit_row][j]
    last_digit_sign = j
    # find the number and ending
    for y in range(j + 1, max_j):
        if engine[digit_row][y].isdigit():
            number += engine[digit_row][y]
            last_digit_sign = y
        else:
            break

    # find the symbol around
    is_part = check_if_part_number(engine, digit_row, j, last_digit_sign)

    if is_part:
        return int(number), last_digit_sign + 1
    else:
        return None, last_digit_sign + 1


def main():
    engine = []
    with open('input2.txt', 'r') as f:
        sum = 0
        lines = f.readlines()
        for line in lines:
            engine.append(line[:-1])

        MAX_I = len(engine)
        MAX_J = len(engine[0])

        print(engine)

        for i in range(0, MAX_I):
            engine[i] = '.' + engine[i] + '.'

        engine.insert(0, '.' * (MAX_J + 2))
        engine.append('.' * (MAX_J + 2))

        MAX_I = len(engine)
        MAX_J = len(engine[0])

        i = 0
        while i < MAX_I:
            j = 0
            while j < MAX_J:
                if engine[i][j].isdigit():
                    number, y = parse_number(engine, i, j, MAX_J)
                    print(number)
                    if number:
                        sum += number

                    j = y
                else:
                    j += 1

                if j == MAX_J:
                    i += 1

        print(sum)


if __name__ == "__main__":
    main()
