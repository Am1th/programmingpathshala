import math

t = int(input())

N = 10 ** 6
primes = [1] * (N + 1)
primes[0] = primes[1] = 0
spf = [-1] * (N + 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i] == 1:
        for j in range(i, (N // i) + 1):
            if primes[i * j] == 1:
                primes[i * j] = 0
                spf[i * j] = i

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = []
    for num in arr:
        if num == 0 or num == 1:
            res.append(0)
            continue
        cnt = 0
        while spf[num] != -1:
            p = spf[num]
            while num % p == 0:
                num = num // p
            cnt += 1
        if num != 1: cnt += 1
        res.append(cnt)
    print(*res)



#same above solution we can skip primes array completely
import math
t=int(input())

N=10**6
spf=[-1]*(N+1)

for i in range(2,int(math.sqrt(N))+1):
    if spf[i]==-1:              # i is prime
        for j in range(i, (N//i)+1):
            if spf[i*j]==-1:
                spf[i*j]=i

for _ in range(t):
    res = []
    n=int(input())
    arr=list(map(int,input().split()))
    for num in arr:
        if num==0 or num==1:
            res.append(0)
            continue
        cnt=0
        while spf[num]!=-1:
            p=spf[num]
            while num%p==0:
                num//=p
            cnt+=1
        if num!=1:
            cnt+=1
        res.append(cnt)
    print(*res)


"""
wkt the same above for loop can be written as below
for i in range(2,int(math.sqrt(N))+1):
    if spf[i]==-1:              # i is prime
        for j in range(i*i, N+1,i):
            if spf[j]==-1:
                spf[j]=i
"""






# same solution, but storing spf for primes as prime number itself
import math
t=int(input())

N=10**6
spf=list(range(N+1))

for i in range(2,int(math.sqrt(N))+1):    #we skipped primes array completely
    if spf[i]==i:              # i is prime
        for j in range(i*i, N+1,i):
            if spf[j]==j:
                spf[j]=i

for _ in range(t):
    res = []
    n=int(input())
    arr=list(map(int,input().split()))
    for num in arr:
        cnt=0
        while num>1:     #we removed checks for num==0 and num==1.
            p=spf[num]
            while num%p==0:
                num//=p
            cnt+=1
        res.append(cnt)
    print(*res)








#just using functions
import math

import sys
input = sys.stdin.readline   #for faster input reading
t = int(input())

N = 10 ** 6
spf = list(range(N + 1))

for i in range(2, int(math.sqrt(N)) + 1):
    if spf[i] == i:  # i is prime
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i


def count_unique_prime_factors(num):
    cnt = 0
    while num > 1:
        p = spf[num]
        while num % p == 0:
            num //= p
        cnt += 1
    return cnt


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # res = []
    # for num in arr:
    #     res.append(count_unique_prime_factors(num))

    # res=[count_unique_prime_factors(num) for num in arr]
    # print(*res)

    res = [str(count_unique_prime_factors(num)) for num in arr]
    print(" ".join(res))




