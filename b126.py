S = input()

aa = S[0:2]
bb = S[2:4]


def isYY(yy):
    if 0 <= int(yy) and int(yy) <= 99:
        return True
    else:
        return False


def isMM(mm):
    if 1 <= int(mm) and int(mm) <= 12:
        return True
    else:
        return False


ans = []
if isYY(aa) and isMM(bb):
    # YYMM
    ans.append('YYMM')
if isMM(aa) and isYY(bb):
    # MMYY
    ans.append('MMYY')

if len(ans) >= 2:
    print('AMBIGUOUS')
elif len(ans) == 1:
    print(ans[0])
else:
    print('NA')
