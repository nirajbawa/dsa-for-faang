n = 4
for i in range(n*2-1):
    for j in range(n*2-1):
        top = i
        left = j
        right = (2 * n - 1)-1-j
        bottom = (2 * n - 1)-1-i
        val = n - min(min(top, bottom), min(left, right))
        print(val, end=" ")
    print()