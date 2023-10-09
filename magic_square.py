def generate(n):
    arr = [[0 for i in range(n)] for j in range(n)]
    i = n // 2
    j = n - 1
    num = 1
    while num <= (n * n):
        if i < 0 and j > n - 1:  # 3rd condt
            i = 0
            j = n - 2
        else:
            if i < 0:
                i = n - 1
            if j > n - 1:
                j = 0
        if arr[i][j] != 0:
            i += 1
            j -= 2
            if i >= n:  # Correct for out-of-bounds i
                i = 0
            if j < 0:  # Correct for out-of-bounds j
                j = n - 1
            continue
        else:
            arr[i][j] = num
            num = num + 1
        i = i - 1
        j = j + 1
        if i < 0:  # Correct for out-of-bounds i
            i = n - 1
        if j >= n:  # Correct for out-of-bounds j
            j = 0

    for row in arr:
        print(row)
n = 3
generate(n)