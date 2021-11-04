
import math

def p_triplets(cap):
    for a in range(1, cap):
        for b in range(a + 1, cap + 1):
            c = math.sqrt(a ** 2 + b ** 2)
            if c % 1 == 0:
                if a + b + c == 1000:
                    return int(a * b * c)
    return 1

print(p_triplets(400))
