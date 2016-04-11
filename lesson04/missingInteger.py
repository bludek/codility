def solution(A):
    return missing(A, len(A))


def sorted_missing(A, n):
    b = sorted(A)
    if b[0] > 1:
        return 1
    for i in xrange(0, n):
        if b[i] < 0:
            continue
        else:
            if i - 1 >= 0 >= b[i - 1] and b[i] > 1:
                return 1
            elif i + 1 >= n:
                return b[i] + 1
            elif b[i] == b[i + 1]:
                continue
            elif b[i] + 1 != b[i + 1]:
                return b[i] + 1
    return 1


def missing(A, n):
    cover = [False] * (n + 1)
    for number in A:
        if 0 < number <= n + 1:
            cover[number - 1] = True

    for i in xrange(0, n + 1):
        if not cover[i]:
            return i + 1
    return 1
