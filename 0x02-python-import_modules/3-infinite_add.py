#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    counter = len(sys.argv) - 1
    for i in range(counter):
        sum += int(sys.argv[i + 1])
    print("{}".format(sum))
