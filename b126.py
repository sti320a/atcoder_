S = input()

aa = S[0:2]
bb = S[2:4]


def isYY(aa):
    if 1 <= int(aa) and int(aa) <= 12:
        return True
    else:
        return False


def isXX(bb):
    if 1 <= int(bb) and int(bb) <= 31:
        return True
    else:
        return False


if isYY(aa) and isXX(bb):
    print(aa + bb)

# TODO
