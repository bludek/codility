def solution(A):
    return passing(A)


def passing(A):
    west = 0
    passing = 0
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 0:
            passing += west
            if passing > 1000000:
                return -1
        else:
            west += 1
    return passing
