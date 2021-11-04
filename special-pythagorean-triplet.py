
def p_triples():
    for a in range(1, 332):
        for b in range(a + 1, 499):
            c = 1000 - (a + b)
            if a ** 2 + b ** 2 == c ** 2:
                return int(a * b * c)
    return 1

print(p_triples())
