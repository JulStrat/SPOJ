from sys import stdin
from operator import xor
readl = stdin.readline

for __ in xrange(int(readl())):
    n = int(readl())
    seq = map(int, readl().split())
    r = reduce(xor, seq, 0)
    print(r)
    