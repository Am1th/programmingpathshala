# O(√N+logN)≈O(√N) , brute force,   3/4 passed, TLE for 1 test case. But in C++ got submitted.
import math
t = int(input())
for _ in range(t):
    n = int(input())

    num = n
    for i in range(2, int(math.sqrt(num)) + 1):
        cnt = 0
        while (n % i == 0):
            cnt += 1
            n = n // i
        if cnt > 0:
            print(i, cnt)
    if n != 1:
        print(n, 1)

#same above code, but tried printing output at once, to see if last test case  works, but still getting TLE
import math
t = int(input())
res = []
for _ in range(t):
    n = int(input())

    num = n
    for i in range(2, int(math.sqrt(num)) + 1):
        cnt = 0
        while (n % i == 0):
            cnt += 1
            n = n // i
        if cnt > 0:
            res.append(f"{i} {cnt}")
    if n != 1:
        res.append(f"{n} {1}")

print("\n".join(res))


#this works,brute force, but shrinking the number. Solution suggested by perplexity
#might confuse to what viveksir suggested.
import math
t = int(input())
out = []

for _ in range(t):
    n = int(input())
    num = n           # work on a copy

    i = 2
    while i * i <= num: #shrinks the loop bound as num shrinks
        cnt = 0
        while num % i == 0:
            cnt += 1
            num //= i   #shrinking num
        if cnt > 0:
            out.append(f"{i} {cnt}")
        i += 1

    if num > 1:       # remaining prime factor
        out.append(f"{num} 1")

print("\n".join(out))


"""
1. Loop bound and shrinking
First code

python
num = n
i = 2
while i * i <= num:
    cnt = 0
    while num % i == 0:
        cnt += 1
        num //= i
    if cnt > 0:
        out.append(f"{i} {cnt}")
    i += 1
if num > 1:
    out.append(f"{num} 1")
• The loop condition is i * i <= num.
• num is shrinking inside the loop as factors are removed.
• As num becomes smaller, the condition i * i <= num becomes false earlier, so the loop stops sooner.
• This is the classic improved trial-division pattern: you only need to try divisors while i^2≤current number; once the remaining num is 1 or prime, you exit quickly.
This makes the work closer to optimal O(original n)O(original n) and often less, because the limit shrinks along the way.

Second code

python
num = n
for i in range(2, int(math.sqrt(num)) + 1):
    cnt = 0
    while (n % i == 0):
        cnt += 1
        n = n // i
    if cnt > 0:
        res.append(f"{i} {cnt}")
if n != 1:
    res.append(f"{n} {1}")

• The loop bound is computed once: int(math.sqrt(num)) + 1 using the original num = n.
• Inside the loop you divide n, not num.
• As factors are removed, n shrinks, but the for i in range(...) still goes all the way up to sqrt(original n).
• For composite numbers with small factors, this does extra useless checks for large i after n has already become small.
• For a large prime n, you do a modulus check for every i from 2 to sqrt(n) and never break early, which is the worst case.

So the second code always pays the full cost up to original noriginal n, while the first code can stop much earlier once num is reduced.

"""








# best solution
# O(NloglogN+Q.logN)≈O(N)
import math
from collections import defaultdict

t = int(input())
N = 10 ** 6
primes = [1] * (N + 1)
# for i in range(1,N+1):  loop not req
#     primes[i]=1
primes[0] = primes[1] = 0
spf = [-1] * (N + 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i]==1:
        for j in range(i, (N // i) + 1):
            if primes[i * j] == 1:
                primes[i * j] = 0
                spf[i * j] = i

for _ in range(t):
    n = int(input())
    dict1 = defaultdict(int)
    while (spf[n] != -1):
        dict1[spf[n]] += 1
        n = n // spf[n]
    if n != 1: dict1[n] += 1
    for key, value in dict1.items():
        print(key, value)



#same above but skipped dictionary
import math
from collections import defaultdict
t=int(input())

N=10**6
primes=[1]*(N+1)

primes[0]=primes[1]=0
spf=[-1]*(N+1)

for i in range(2,int(math.sqrt(N))+1):
    if primes[i] == 1:
        for j in range(i*i,N+1,i):    #same as my logic , but written differently
            if primes[j]==1:
                primes[j]=0
                spf[j]=i


for _ in range(t):
    n=int(input())
    res=[]
    while n>1 and spf[n]!=-1:  #n>1 can be skipped take n=404... and atlast n becomes 101,  101>1 and enters loop, spf[101]=-1 and it goes wrong.  So i then thought and added spf[n]!=-1 condition
        p=spf[n]
        cnt=0
        while(n%p==0):
            cnt+=1
            n=n//p
        res.append(f"{p} {cnt}")
    if n>1:res.append(f"{n} 1")
    print("\n".join(res))


#below is approach suggest by chatgpt. storing spf for primes as prime number itself (insted of -1 in my approach). removed primes array completely
import math
from collections import defaultdict
t=int(input())

N=10**6
spf=list(range(N+1))

for i in range(2,int(math.sqrt(N))+1):#wkt this same loop , can be written in the style we know,shown in comments
    if spf[i]==i: # # i is prime
        for j in range(i*i,N+1,i):
            if spf[j]==j:
                spf[j]=i

for _ in range(t):
    n=int(input())
    res=[]
    while n>1:
        p=spf[n]
        cnt=0
        while(n%p==0):
            cnt+=1
            n=n//p
        res.append(f"{p} {cnt}")
    print("\n".join(res))


"""
wkt this is our approach
for i in range(2,int(math.sqrt(N))+1):
    if spf[i]==i:
        for j in range(i,(N//i)+1):
            if spf[i*j]==i*j:
                spf[i*j]=i
"""