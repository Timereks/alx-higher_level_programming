#!/usr/bin/python3
for tim in range(ord('a'), ord('z') + 1):
    if chr(tim) != 'e' and chr(tim) != 'q':
        print('{}'.format(chr(tim)), end="")
