
# Modification of 10001st_prime.py

def prime_check(x, out):
    for i in out:
        if x % i == 0:
            return False
    return True

i = 3
out = [2]
sum = 2
while out[-1] < 2000000:
    if prime_check(i, out):
        out.append(i)
        sum += i
    i += 1
print(sum - out[-1])
