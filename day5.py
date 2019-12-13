def intcode(inp):
    i = 0
    while True:
        value = inp[i]
        value_ = int(value.zfill(2)[-2:])
        if value_ == 99:
            print('HALT')
            break
        elif value_ in (1, 2):
            x, y, z = [int(_) for _ in inp[i + 1: i + 4]]
            px, py, _ = [int(_) for _ in reversed(value.zfill(5)[:3])]
            if not px:
                x = int(inp[x])
            if not py:
                y = int(inp[y])
            if value_ == 1:
                inp[z] = str(x + y)
            elif value_ == 2:
                inp[z] = str(x * y)
            i += 4
        elif value_ in (3, 4):
            loc = int(inp[i + 1])
            # param = value.zfill(3)[-3]
            if value_ == 3:
                inp[loc] = input('What is the input?')
            elif value_ == 4:
                print(inp[loc])
            i += 2
        else:
            raise AttributeError
    return inp


def intcode2(inp):
    i = 0
    while True:
        value = inp[i]
        value_ = int(value.zfill(2)[-2:])
        if value_ == 99:
            print('HALT')
            break
        elif value_ in (1, 2):
            x, y, z = [int(_) for _ in inp[i + 1: i + 4]]
            px, py, _ = [int(_) for _ in reversed(value.zfill(5)[:3])]
            if not px:
                x = int(inp[x])
            if not py:
                y = int(inp[y])
            if value_ == 1:
                inp[z] = str(x + y)
            elif value_ == 2:
                inp[z] = str(x * y)
            else:
                raise AttributeError
            i += 4
        elif value_ in (3, 4, 5, 6):
            loc = int(inp[i + 1])
            # param = value.zfill(3)[-3]
            if value_ == 3:
                inp[loc] = input('What is the input?')
            elif value_ == 4:
                print(inp[loc])
            elif value_ == 5:
                pass
            elif value_ == 6:
                pass
            else:
                raise AttributeError
            i += 2
        elif value_ in (7, 8):
            if value_ == 7:
                pass
            elif value_ == 8:
                pass
            else:
                raise AttributeError
            i += 3
        else:
            raise AttributeError
    return inp


with open('day5.in', 'r') as f:
    list_ = f.read().strip().split(',')
intcode(list_)

with open('day5.in', 'r') as f:
    list_ = f.read().strip().split(',')
intcode2(list_)
