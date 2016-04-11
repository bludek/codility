def solution(N, A):
    return counter(N, A)


# O(N*M) 66%
def easy_counter(N, A):
    result = [0] * N
    for number in A:
        if 1 <= number <= N:
            result[number - 1] += 1
        elif number == N + 1:
            result[:] = [max(result)] * N

    return result


# O(N*M) 77%
def poor_counter(N, A):
    result = [0] * N
    max = 0
    for number in A:
        if 1 <= number <= N:
            result[number - 1] += 1
            if result[number - 1] > max:
                max = result[number - 1]
        elif number == N + 1:
            result = [max] * N

    return result


# O(N+M) 100%
def counter(N, A):
    result = [0] * N
    max = 0
    temp = 0
    for c in A:
        if 1 <= c <= N:
            if max > result[c - 1]:
                result[c - 1] = max
            result[c - 1] += 1
            if result[c - 1] > temp:
                temp = result[c - 1]
        elif c == N + 1:
            max = temp

    for i in xrange(0, N):
        if result[i] < max:
            result[i] = max

    return result
