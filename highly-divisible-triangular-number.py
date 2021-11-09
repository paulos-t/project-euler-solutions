
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
    if math.sqrt(num) % 1 == 0:
        factors.append(len(factors) * 2 + 1)
    else:
        factors.append(len(factors) * 2)
    return factors

l = t_nums()
print(l)
for i in l:
    print(factors(i)[-1])
