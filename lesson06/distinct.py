def solution(A):
    return distinct(A, len(A))


def distinct(A, n):
    b = sorted(A)
    result = 1
    if n == 0: return 0
    for i in range(0, n - 1):
        if b[i] != b[i + 1]:
            result += 1
    return result
