tests = [111111, 223450, 123789]


def verify(num):
    str_ = str(num)
    if len(str_) != 6:
        return False
    char = str_[0]
    for next_ in str_[1:]:
        if char == next_:
            break
        char = next_
    else:
        return False
    char = int(str_[0])
    for next_ in str_[1:]:
        next_ = int(next_)
        if next_ < char:
            return False
        char = next_
    else:
        return True


for value in tests:
    print(verify(value))

low, high = (108457, 562041)
count = 0
for value in range(low, high + 1):
    if verify(value):
        count += 1
print(count)

tests = [112233, 123444, 111122]


def verify2(num):
    str_ = str(num)
    if len(str_) != 6:
        return False
    flag = False
    char, count = str_[0], 1
    for next_ in str_[1:]:
        if char == next_:
            count += 1
        else:
            if count == 2:
                flag = True
            count = 1
        char = next_
    if count == 2:
        flag = True
    if not flag:
        return False
    char = int(str_[0])
    for next_ in str_[1:]:
        next_ = int(next_)
        if next_ < char:
            return False
        char = next_
    else:
        return True


for value in tests:
    print(verify2(value))

count = 0
for value in range(low, high + 1):
    if verify2(value):
        count += 1
print(count)
