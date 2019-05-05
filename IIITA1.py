from sys import stdin
xrange = range
def main():
    readl = stdin.readline
    for __ in xrange(int(readl())):
        a, b = map(int, readl().split())
        r = a ^ b
        print(bin(r).count("1"))

if __name__ == "__main__":
    main()