"""
# You want primes/composites for prices 2.. N+1 ,  i.e. indices 2..N+1 in cnt.
import math
N=int(input())
#colors are 2,3,4,5,6,7....   so at 0 index we have 0, at index 1 we have 1, at index 2 we have 2 and so on...at index N+1 we have N+1
cnt=[0]*(N+2)   # indices: 0..N+1
cnt[0]=cnt[1]=0
# Sieve on numbers up to N+1 to find primes in [2..N+1]
for i in range(2,int(math.sqrt(N+1))+1):  #if there are 4 elements the elements will be 2,3,4,5 so if N is 4,last element will be N+1
    if cnt[i]==0: #prime number
        cnt[i]=1  # color prime number with 1
        for j in range(i*i,N+2,i):
            cnt[j]=2  # color composites with 2

for i in range(int(math.sqrt(N+1))+1,N+2):
    if cnt[i]==0:  #primes after sqrt(N)
        cnt[i]=1   #color these primes with 1

k=1 if N<=2 else 2
print(k)
for i in range(2,N+2):    #loop stop at N+1 inclusive, so index N+1 is also touched.
    print(cnt[i],end=" ")
"""

#same above, without comments
import math
N=int(input())
cnt=[0]*(N+2)
cnt[0]=cnt[1]=0
for i in range(2,int(math.sqrt(N+1))+1):
    if cnt[i]==0:
        cnt[i]=1
        for j in range(i*i,N+2,i):
            cnt[j]=2

for i in range(int(math.sqrt(N+1))+1,N+2):
    if cnt[i]==0:
        cnt[i]=1

k=1 if N<=2 else 2
print(k)
for i in range(2,N+2):
    print(cnt[i],end=" ")


#solution i wrote using normal approach
import math
N=int(input())
primes=[1]*(N+2)
primes[0]=primes[1]=0
for i in range(2,int(math.sqrt(N+1))+1):
    if primes[i]:
        for j in range(i,( (N+1)//i ) + 1):
            primes[i*j]=0

k= 1 if N<=2 else 2
print(k)

for i in range(2,N+2):
    print(1 if primes[i]==1 else 2,end=" ")




#perplexity suggested solution
# import math
# N = int(input())
# limit = N + 1
# is_prime = [True] * (limit + 1)
# is_prime[0] = is_prime[1] = False
#
# for i in range(2, int(math.isqrt(limit)) + 1):
#     if is_prime[i]:
#         for j in range(i * i, limit + 1, i):
#             is_prime[j] = False
#
# k = 1 if N <= 2 else 2
# print(k)
#
# for x in range(2, N + 2):
#     print(1 if is_prime[x] else 2, end=" ")
# print()
