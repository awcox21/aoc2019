from itertools import combinations


def intcode(inp):
    i = 0
    while True:
        value = inp[i]
        if value == 99:
            break
        elif value in (1, 2):
            x, y, z = inp[i + 1: i + 4]
            if value == 1:
                inp[z] = inp[x] + inp[y]
            elif value == 2:
                inp[z] = inp[x] * inp[y]
            i += 4
    return inp


test_strs = ['1,9,10,3,2,3,11,0,99,30,40,50', '1,0,0,0,99', '2,3,0,3,99', '2,4,4,5,99,0', '1,1,1,4,99,5,6,0,99']
for _str in test_strs:
    out = intcode([int(_) for _ in _str.split(',')])
    print(out)

with open('day2.in', 'r') as f:
    inp = [int(_) for _ in f.read().strip().split(',')]
inp[1] = 12
inp[2] = 2
out = intcode(inp)
print(f'Part 1 solution: {out[0]}')

count = 0
for noun, verb in combinations(range(100), 2):
    with open('day2.in', 'r') as f:
        inp = [int(_) for _ in f.read().strip().split(',')]
    inp[1] = noun
    inp[2] = verb
    out = intcode(inp)[0]
    if out == 19690720:
        print(f'Tried {count} options')
        break
    else:
        count += 1
print(f'Part 2 solution: {100 * noun + verb}')
