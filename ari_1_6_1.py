n = 5
a = [2, 3, 4, 5, 10]


def mktr(x, y, j):
    brs = [x, y, j]
    brs.sort()

    if brs[2] >= brs[1] + brs[0]:
        return 0

    return x+y+j


print(mktr(6, 4, 2))
