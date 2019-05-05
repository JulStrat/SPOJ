from sys import stdin
from itertools import accumulate
readl = stdin.readline

n = int(readl())
s = map(int, readl().split())
ps = list(accumulate(s))
qn = int(readl())
for __ in range(qn):
    l, r = map(int, readl().split())
    if l == 0:
        print(ps[r])
    else:
        print(ps[r]-ps[l-1])
        