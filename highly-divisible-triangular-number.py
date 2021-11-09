
import math

def t_nums():
    t_nums = [1]
    for i in range(2, 11):
        t_nums.append(i + t_nums[-1])
    return t_nums

def factors(num):
    factors = []
    test = 1
    while (num / test) > test:
        if num % test == 0:
            factors.append([test, int(num / test)])
        test += 1
    factors.append(len(factors) * 2)
    if math.sqrt(num) % 1 == 0:
        factors[-1] += 1
    return factors

l = t_nums()
print(l)
out = 0
most_factors = 0
for i in l:
    next = factors(i)[-1]
    if next > most_factors:
        most_factors = next
    out = i
print(f'{out} has {most_factors} factors')
