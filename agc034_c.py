import sys

n, x = list(map(int, input().split()))

exams = []
norma = 0

for i, line in enumerate(sys.stdin):
    b, l, u = map(int, line.split())
    exams.append((u * x - b * (u - l), b, l, u, i))
    norma += b * l
exams_sorted = sorted(exams, reverse=True)


remain_norma = norma

sub_d = -1
i = 0
used = set()
for i, (d, b, l, u, ei) in enumerate(exams_sorted):
    if remain_norma < d:
        sub_d = d
        break
    remain_norma -= d
    used.add(ei)

if sub_d == -1:
    print(n * x)
    exit()

base_ans = i * x
base_remain_norma = remain_norma

ans = 10 ** 10

for d, b, l, u, i in exams:
    if i in used:
        curr_remain_norma = base_remain_norma + d - sub_d
    else:
        curr_remain_norma = base_remain_norma

    if curr_remain_norma <= b * l:
        extra = (curr_remain_norma - 1)
    else:
        extra = (curr_remain_norma + b * (u-l) - 1)
    if extra > x:
        continue
    ans = min(ans, base_ans + extra)

print(ans)
