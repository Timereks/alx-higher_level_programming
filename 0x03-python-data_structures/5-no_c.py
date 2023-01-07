#!/usr/bin/python3
def no_c(my_string):
    result = []
    for t in my_string:
        if t != 'c' and t != 'C':
            result.append(t)
    return ''.join(result)
