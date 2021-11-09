
import math

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

out = 0
most_factors = 0
i = 1
t_num = 1
while most_factors < 500:
    next = factors(t_num)[-1]
    if next > most_factors:
        most_factors = next
        out = t_num
    i += 1
    t_num += i

print(f'Triangle number {out} has {most_factors} factors.')
