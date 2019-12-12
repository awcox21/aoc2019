from math import floor


def find_fuel(mass):
    return max((floor(mass / 3) - 2, 0))


test_masses = [12, 14, 1969, 100756]
answers = [2, 2, 654, 33583]


def test_answers():
    assert all(find_fuel(m) == a for m, a in zip(test_masses, answers))


inp = 'day1.in'
total = 0
with open(inp, 'r') as f:
    for line in f:
        m = float(line)
        total += find_fuel(m)
print(total)


def find_fuel_recurse(mass):
    total_fuel = find_fuel(mass)
    fuel = total_fuel
    while True:
        fuel = find_fuel(fuel)
        if not fuel:
            break
        else:
            total_fuel += fuel
    return total_fuel


test_masses = [14, 1969, 100756]
answers = [2, 966, 50346]


def test_answers():
    assert all(find_fuel_recurse(m) == a for m, a in zip(test_masses, answers))


total = 0
with open(inp, 'r') as f:
    for line in f:
        m = float(line)
        total += find_fuel_recurse(m)
print(total)
