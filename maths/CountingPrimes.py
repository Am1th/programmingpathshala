# TC O(log(logN))+O(Q)
import math

N = 10 ** 6
primes = [1] * (N + 1)
for i in range(1, N + 1):  #loop not req as already initialized with 1
    primes[i] = 1
primes[0] = 0
primes[1] = 0

for i in range(2, int(math.sqrt(N)) + 1):
    for j in range(i, (N // i) + 1):     #must write but i skipped,  if primes[i]==1
        primes[i * j] = 0

#alternate loop suggested by chatgpt for above
# for i in range(2, int(math.sqrt(N)) + 1):
#     if primes[i]:
#         for j in range(i*i, N + 1, i):
#             primes[j] = 0


for i in range(1, N + 1):
    primes[i] = primes[i - 1] + primes[i]

t = int(input())
for _ in range(t):
    n = int(input())
    print(primes[n])

# brute force, O(N√N) solution, TLE, 1/3 passed
# import math
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     primeCount=0
#     if n==1:
#         print(primeCount)
#         continue


#     for i in range(2,n+1):
#         cnt=0
#         for j in range(2,int(math.sqrt(i))+1):
#             if i%j==0:
#                 cnt+=1
#                 break
#         if cnt==0:primeCount+=1
#     print(primeCount)


