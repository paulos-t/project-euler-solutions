
def collatz(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1

out = 0
count = 0
for start in range(1, 1000000):
    num = start
    seq = [start]
    while num != 1:
        num = collatz(num)
        seq.append(num)
    if len(seq) > count:
        count = len(seq)
        out = start

print(out)
