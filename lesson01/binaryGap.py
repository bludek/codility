def solution(N):
    return gap(N)


def gap(N):
    s = str(bin(N)).strip("0")
    gap = 0
    temp = 0
    for i in range(len(s)):
        if s[i] == "0":
            temp += 1
        else:
            if gap < temp:
                gap = temp
            temp = 0
    return gap
