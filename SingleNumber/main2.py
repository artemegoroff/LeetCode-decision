def findNonRepeating(a, n):
    res = 0

    # XOR of all numbers
    for i in range(n):
        res ^= a[i]
    return res


# Driver code
a = [3, 8, 3, 2, 2, 1, 1]
n = len(a)

print(findNonRepeating(a, n))