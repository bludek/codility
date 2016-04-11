def solution(A):
    return triangle(A, len(A))


def triangle(A, n):
    if n < 3:
        return 0
    A.sort()
    for i in range(0, n - 2):
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0