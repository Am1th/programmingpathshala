t = int(input())


def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd(a, b):
    maxm = max(a, b)
    minm = min(a, b)
    while maxm % minm != 0:
        temp = maxm
        maxm = minm
        minm = temp % minm
    return minm


for _ in range(t):
    n, a, b, k = map(int, input().split())
    res = n // a + n // b - 2 * (n // lcm(a, b))
    if res >= k:
        print("Win")
    else:
        print("Lose")