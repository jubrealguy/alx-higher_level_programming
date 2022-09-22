#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum = 0

    if len(argv) == 1:
        sum = 0

    elif len(argv) == 2:
        sum += int(argv[1])

    elif len(argv) > 2:
        for i in range(1, len(argv)):
            sum += int(argv[i])

    print(sum)
