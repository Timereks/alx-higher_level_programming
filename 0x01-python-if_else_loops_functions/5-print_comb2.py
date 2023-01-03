#!/usr/bin/python3
for tim in range(0, 100):
    if tim == 99:
        print("{}".format(tim))
    else:
        print("{:02}".format(tim), end=", ")
