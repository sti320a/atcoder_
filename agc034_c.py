n, x = list(map(int, input().split()))

exms = []
nrm = 0

lines = [map(int, input().split()) for _ in range(n)]

for i, line in enumerate(lines):
    b, l, u = line
    exms.append((u * x - b * (u - l), b, l, u, i))
    nrm += b * l
exms_sorted = sorted(exms, reverse=True)


remain_nrm = nrm

sub_d = -1
i = 0
used = set()
for i, (d, b, l, u, ei) in enumerate(exms_sorted):
    if remain_nrm < d:
        sub_d = d
        break
    remain_nrm -= d
    used.add(ei)

if sub_d == -1:
    print(n * x)
    exit()

base_ans = i * x
base_remain_nrm = remain_nrm

ans = 10 ** 10

for d, b, l, u, i in exms:
    if i in used:
        curr_remain_nrm = base_remain_nrm + d - sub_d
    else:
        curr_remain_nrm = base_remain_nrm

    if curr_remain_nrm <= b * l:
        extra = (curr_remain_nrm - 1) // l + 1
    else:
        extra = (curr_remain_nrm + b * (u - l) - 1) // u + 1
    if extra > x:
        continue
    ans = min(ans, base_ans + extra)

print(ans)
