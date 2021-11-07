
out = []
nums = list(range(2, 2000000))
def primes(nums, out):
    out.append(nums[0])
    last_i = len(nums)
    i = 0
    while i < last_i:
        if nums[i] % out[-1] == 0:
            nums.remove(nums[i])
            last_i -= 1
        else:
            i += 1

while nums:
    primes(nums, out)

print(sum(out))
