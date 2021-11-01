
def product_pal(x, y):
    product = str(int(x) * int(y))
    for c in range(0, int(len(product) / 2)):
        if product[c] != product[(len(product) - 1) - c]:
            return False
    return True

def largest_pal():
    palindromes = []
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            if product_pal(i, j):
                palindromes.append(i * j)
    return max(palindromes)

print(largest_pal())
