#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("{:d} {:s}".format(0, "arguments."))

    elif len(argv) == 2:
        print("{:d} {:s}".format(1, "argument:"))
        print("{:d}: {:s}".format(1, argv[1]))

    elif len(argv) > 2:
        print("{:d} {:s}".format(len(argv) - 1, "arguments:"))

        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
