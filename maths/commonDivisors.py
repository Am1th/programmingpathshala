# • Let g=gcd(A,B).
# • Any common divisor of A and B ,must divide g, and every divisor of g is a common divisor of A and B.
#  so find divisors of g
# O(t⋅(log(max(a,b))+√g))
import math
t = int(input())
def findGCD(a, b):
    maxm = max(a, b)
    minm = min(a, b)
    while (maxm % minm != 0):
        temp = maxm
        maxm = minm
        minm = temp % minm
    return minm


for _ in range(t):
    a, b = map(int, input().split())
    g = findGCD(a, b)
    cnt = 0
    for i in range(1, int(math.sqrt(g)) + 1):
        if g % i == 0: cnt += 2
        if i * i == g: cnt -= 1
    print(cnt)



#Below solution uses spf method and is passing all test cases but is incorrect
# N can go upto 10**9 as per constraints and an array of 10**9 is not possible.
# so i ignored constraints and took 10**6 array and tried.
#    O(NloglogN+t⋅(log(max(a,b))+log g))

import math

t = int(input())


def findGCD(a, b):
    maxm = max(a, b)
    minm = min(a, b)
    while (maxm % minm != 0):
        temp = maxm
        maxm = minm
        minm = temp % minm
    return minm


N = 10 ** 6
spf = list(range(N + 1))
for i in range(2, int(math.sqrt(N)) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

for _ in range(t):
    a, b = map(int, input().split())
    g = findGCD(a, b)
    ans = 1
    while g > 1:
        p = spf[g]
        cnt = 0
        while g % p == 0:
            g = g // p
            cnt += 1
        ans *= (cnt + 1)
    print(ans)



#c++ solution from comments,  converted to python.
# t* (log(max(a,b))+root(N)+logN)
#  O(t⋅(log(max(a,b))+√g+logN))
import math

def count_common_divisors(a, b):
    # Step 1: GCD
    n = math.gcd(a, b)

    # Step 2: Prime factorization of gcd
    factors = {}
    temp = n

    i = 2
    while i * i <= temp:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1

    # If remaining n is a prime
    if n != 1:
        factors[n] = factors.get(n, 0) + 1

    # Step 3: Count divisors using formula
    answer = 1
    for exp in factors.values():
        answer *= (exp + 1)

    return answer


# Input handling
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(count_common_divisors(a, b))



#same above,simplified, skipped map
import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    g = math.gcd(a, b)

    ans = 1
    i = 2
    while i * i <= g:
        cnt = 0
        while g % i == 0:
            g //= i
            cnt += 1
        if cnt > 0:
            ans *= (cnt + 1)
        i += 1

    if g > 1:   # remaining prime
        ans *= 2

    print(ans)

