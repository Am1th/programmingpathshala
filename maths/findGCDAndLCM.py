a, b = map(int, input().split())

maxm = max(a, b)
minm = min(a, b)
while (maxm % minm != 0):
    temp = maxm
    maxm = minm
    minm = temp % minm
print(minm, (a * b) // minm)


