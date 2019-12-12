tests = [('R8,U5,L5,D3', 'U7,R6,D4,L4'),
         ('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'),
         ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')]


def get_path(str_):
    i, j = 0, 0
    path = [(i, j, 'o')]
    for step in str_.split(','):
        direction = step[0]
        length = int(step[1:])
        if direction == 'U':
            hor, vert, char = 0, 1, '|'
        elif direction == 'D':
            hor, vert, char = 0, -1, '|'
        elif direction == 'L':
            hor, vert, char = -1, 0, '-'
        else:  # direction == 'R':
            hor, vert, char = 1, 0, '-'
        for _ in range(length - 1):
            i += hor
            j += vert
            path.append((i, j, char))
        i += hor
        j += vert
        path.append((i, j, '+'))
    return path


def join_paths(strs):
    lists = [get_path(str_) for str_ in strs]
    sets = [set((i, j) for i, j, _ in list_) for list_ in lists]
    _joined = set([x for y in lists for x in y])
    dict_ = {(i, j): char for i, j, char in _joined}
    shared = sets[0].intersection(*sets[1:])
    shared.remove((0, 0))
    for i, j in dict_:
        if (i, j) in shared:
            dict_[i, j] = 'X'
    return [(i, j, dict_[i, j]) for i, j in dict_]


def plot_paths(strs):
    joined = join_paths(strs)
    dict_ = {(i, j): char for i, j, char in joined}
    xs = [i for i, j, char in joined]
    min_x, max_x = min(xs), max(xs)
    ys = [j for i, j, char in joined]
    min_y, max_y = min(ys), max(ys)
    grid = list()
    for j in range(min_y - 1, max_y + 2):
        row = list()
        for i in range(min_x - 1, max_x + 2):
            if (i, j) in dict_:
                char = dict_[i, j]
            else:
                char = '.'
            row.append(char)
        grid.append(row)
    print('\n'.join([''.join(row) for row in reversed(grid)]) + '\n')


def get_closest(strs):
    distance, point = None, None
    for i, j, char in join_paths(strs):
        dist = abs(i) + abs(j)
        if char == 'X':
            if distance is None:
                distance = dist
                point = i, j
            elif dist < distance:
                distance = dist
                point = i, j
    return point


# Part 1 Tests
for paths in tests:
    # plot_paths(paths)
    i, j = get_closest(paths)
    print((i, j), abs(i) + abs(j))

# Part 1
inp = list()
with open('day3.in', 'r') as f:
    for line in f:
        inp.append(line.strip())
i, j = get_closest(inp)
print((i, j), abs(i) + abs(j))

# Part 2 Test
for paths in tests:
    shared = list()
    distance = None
    for i, j, char in join_paths(paths):
        if char == 'X':
            shared.append((i, j))
    for i, j in shared:
        tot = 0
        for path in paths:
            path = get_path(path)
            for count, (x, y, _) in enumerate(path):
                if i == x and j == y:
                    break
            tot += count
        if distance is None:
            distance = tot
        elif tot < distance:
            distance = tot
    print(distance)

# Part 2
inp = list()
with open('day3.in', 'r') as f:
    for line in f:
        inp.append(line.strip())
shared = list()
distance = None
for i, j, char in join_paths(inp):
    if char == 'X':
        shared.append((i, j))
for i, j in shared:
    tot = 0
    for path in inp:
        path = get_path(path)
        for count, (x, y, _) in enumerate(path):
            if i == x and j == y:
                break
        tot += count
    if distance is None:
        distance = tot
    elif tot < distance:
        distance = tot
print(distance)
