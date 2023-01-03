#!/usr/bin/python3
for tim in range(0, 10):
    for mine in range(1, 10):
        if tim >= mine:
            continue
        elif tim == 8 and mine == 9:
            print("{}{}".format(tim, mine))
        else:
            print("{}{}".format(tim, mine), end=", ")
