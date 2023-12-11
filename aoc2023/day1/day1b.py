digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
string_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

string_digits_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def main():
    with (open('input1.txt', 'r') as f):
        sum = 0
        lines = f.readlines()
        for line in lines:
            first = None
            last = None

            for i in range(0, len(line)):
                if first is None:
                    if line[i].isdigit():
                        first = line[i]
                    else:
                        for sd in string_digits:
                            try:
                                sd_len = len(sd)
                                if sd == line[i : i + sd_len]:
                                    first = string_digits_map.get(sd)
                                    break
                            except:
                                pass

                if last is None:
                    if line[len(line) - i - 1].isdigit():
                        last = line[len(line) - i - 1]
                    else:
                        for sd in string_digits:
                            try:
                                sd_len = len(sd)
                                if sd == line[len(line) - i - 1 - sd_len : len(line) - i - 1]:
                                    last = string_digits_map.get(sd)
                                    break
                            except:
                                pass
                if first and last:
                    break

            sum += int(first + last)

        print(sum)


if __name__ == "__main__":
    main()
