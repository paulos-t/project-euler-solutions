
def prime_check(x, out):
    for i in out:
        if x % i == 0:
            return False
    return True

i = 2
out = []
while len(out) < 10001:
    if prime_check(i, out):
        out.append(i)
    i += 1
print(out[-1])
