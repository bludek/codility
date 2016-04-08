def solution(X, A):
    return golden_cross(X, A, len(A))


def cross(X, A, n):
    array = range(1, X + 1)
    for i in range(0, n):
        if A[i] in array:
            array.remove(A[i])
        if not array:
            return i
    return -1


def golden_cross(X, A, n):
    cover = [-1] * X
    uncovered = X

    for i in range(0, n):
        if cover[A[i] - 1] != -1:
            continue
        else:
            cover[A[i] - 1] = i
            uncovered -= 1
            if uncovered == 0:
                return i
    return -1
