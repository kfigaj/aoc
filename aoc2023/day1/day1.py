def main():
    with open('input1.txt', 'r') as f:
        sum = 0
        lines = f.readlines()
        for line in lines:
            first = None
            last = None

            for i in range(0, len(line)):
                if first is None and line[i].isdigit():
                    first = line[i]
                if last is None and line[len(line) - i - 1].isdigit():
                    last = line[len(line) - i - 1]
                if first and last:
                    break

            sum += int(first + last)

        print(sum)


if __name__ == "__main__":
    main()
