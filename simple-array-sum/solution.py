#!/bin/python3
#
# Complete the simpleArraySum function below.
#


inp = """6
1 2 3 4 10 11"""

def parse_input(inp):
    stripped = inp.strip()
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
        print('No values')
        raise TypeError('The input is not correctly formatted.', ar)
    print(length, arr)
    # result = simpleArraySum(ar)
    # print(result)
    return ''

simpleArraySum(inp)