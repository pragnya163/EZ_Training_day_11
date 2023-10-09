def count(n):
    if n == 1:
        return 1
    return 2 * count(n - 1) + 1
ans = count(3)
print(ans)
