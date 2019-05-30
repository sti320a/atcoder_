from operator import itemgetter

N = int(input())
ins = [list(input().split()) for _ in range(N)]

res = []
for i, row in enumerate(ins):
    row = [i+1] + [row[0]] + [int(row[1])]
    res.append(row)

res.sort(key=itemgetter(2), reverse=True)
res.sort(key=itemgetter(1))

for i in res:
    print(i[0])
