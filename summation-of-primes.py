from numpy import *

out = []
nums = list(range(2, 200000))
def primes(nums, out):
    if not nums:
        return out
    out.append(nums[0])
    indicies = ['a'] * len(nums)
    for j in indicies:
        if j % out[-1] == 0:
            nums.remove(j)

while nums:
    primes(nums, out)

print(sum(out))
