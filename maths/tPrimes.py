# Tried below , has  bugs
import math
N=10**5
primes=[1]*(N+1)
primes[0]=primes[1]=0
for i in range(2,int(math.sqrt(N))+1):
    if primes[i]:
        for j in range(i,(N//i)+1):
            primes[i*j]=0

for i in range(2,N+1):
    if primes[i]==1:
        primes[i*i]=-1

n=int(input())
arr=list(map(int,input().split()))
for ele in arr:
    if primes[ele]==-1:
        print("YES")
    else:
        print("NO")


"""
❌ Problems in above Code

1. Wrong limit: N = 10^5
You set:

N = 10**5
But the input numbers can be as large as:
xi≤ 10^12
So checking primes[ele] will fail because:

primes[10^12]
is impossible (out of range).

2. You are trying to mark squares like this:

primes[i*i] = -1
But i*i can go beyond N.
Example:

i = 400
i*i = 160000 > 100000
So many prime squares are not even stored.

3. Main mistake: You cannot index primes[ele]

if primes[ele] == -1:
Because ele can be up to 10^12
That would require an array of size  10^12, impossible.

4. Sieve inner loop is inefficient
You wrote:

for j in range(i, (N//i)+1):
    primes[i*j] = 0
This works but is slower than the standard:

for j in range(i*i, N+1, i)



✅ Correct Logic
A number is T-prime if:
	1. It is a perfect square
	2. Its square root is prime
So for each number x:
	• Compute r = isqrt(x)
	• Check r*r == x

Check r is prime
"""


#this is optimized solution
import math
N=10**6   # because sqrt(10^12) = 10^6
# Step 1: Sieve up to 10^6
primes=[1]*(N+1)
primes[0]=primes[1]=0
for i in range(2,int(math.sqrt(N))+1):
    if primes[i]:
        for j in range(i,(N//i)+1):     #for j in range(i * i, N + 1, i):
            primes[i*j]=0                    #prime[j] = 0         this is a little faster

n=int(input())
arr=list(map(int,input().split()))
for ele in arr:
    r = int(math.sqrt(ele))     # use r = int(math.isqrt(x)), Because math.sqrt() uses floating point, and for very large numbers up to 10^12, floating precision can sometimes give wrong roots.
    if r * r == ele and primes[r]==1:
        print("YES")
    else:
        print("NO")







"""
Logic, can skip

✅ What is a T-prime?
A number t is called T-prime if it has exactly 3 distinct positive divisors.

Example
Take:
t = 4
Divisors: 1, 2, 4 → total = 3 → ✅ T-prime
t = 6
Divisors: 1, 2, 3, 6 → total = 4 → ❌ Not T-prime

🔥 Key Observation
A number has exactly 3 divisors only when it is of the form:
t=  p^2
where p is a prime number.

Why?
Let:
t=  p^2 
Divisors are:
1, p, p^2
Exactly 3 divisors → ✅ T-prime

What if the number is not a square?
Example:
12=2^2 . 3  
Divisors count becomes more than 3 → ❌

What if the number is square but not prime square?
Example:
36= 6^2
But 6 is not prime.
Divisors of 36 are:
1,2,3,4,6,9,12,18,36 
Too many → ❌

✅ Final Condition for T-prime
A number x is T-prime if:
	1. x is a perfect square
	2. Sqrt(x)​ is prime

Constraints
	• n≤10^5
	• xi≤10^12
So:
Sqrt(xi)≤10^6 
We can precompute primes up to 10^6 using Sieve of Eratosthenes.

✅ Efficient Approach
Step 1: Sieve primes up to 10^6
Step 2: For each number x:
	• compute r = integer sqrt(x)
	• check if r*r == x (perfect square)
	• check if r is prime
	• if yes → print YES else NO





Time Complexity
	• Sieve: O(10^6loglog10^6)
	• Checking each number: O(1)
Total:
O(10^6 + n)
Efficient for n=10^5

"""
