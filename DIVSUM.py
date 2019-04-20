from sys import stdin, stdout

def div_sum(n):
    sz = n + 1
    ds = [1]*sz
    ds[0] = 0
    ds[1] = 0

    for d in xrange(2, n//2+1):
        for j in xrange(2*d, sz, d):
            ds[j] += d
    return ds

def main():
    readl = stdin.read
    writeb = stdout.write
    seq = map(int, readl().split())
    UB = max(seq[1:])
    ds = div_sum(UB)
    for x in seq[1:]:
        writeb(str(ds[x]))
        writeb('\n')
    stdout.flush()

if __name__ == "__main__":
    main()