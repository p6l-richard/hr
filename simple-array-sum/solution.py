#!/bin/python3
#
# Complete the simpleArraySum function below.
#
# INSTRUCTIONS
# 1st: run unit test `python -m unittest test_solution`
# 2nd: run `python -m solution.py`

inp = """6
1 2 3 4 10 11"""

def parse_input(inp):
    stripped = str(inp).strip()
    lines = list(filter(None, stripped.splitlines()))
    if not len(lines) == 2:
        return 'Input does not contain 2 lines'
    try: 
        int(lines[0])
        pass
    except ValueError:
        return 'First value is no integer'
    if int(lines[0]) != len(lines[1].split()):
        return 'length and array-length do not match'

    length = int(lines[0])
    arr = list(map(lambda el: float(el), lines[1].split()))
    return [length, arr]

def simpleArraySum(ar):
    length, arr = parse_input(ar)   
    if not length:
        raise TypeError('The input is not correctly formatted.', ar)
    return sum(arr)

print('Input:\n', inp, '\n\nSum:',simpleArraySum(inp))