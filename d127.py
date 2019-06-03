from operator import itemgetter


def f(): return map(int, input().split())


N, M = f()
A = list(f())
BC = [list(f()) for i in range(M)]

BC.sort(key=itemgetter(1), reverse=True)

for b, c in BC:
    A.extend([c]*b)
    if len(A) >= 2*N:
        break

A.sort(reverse=True)
print(sum(A[:N]))
