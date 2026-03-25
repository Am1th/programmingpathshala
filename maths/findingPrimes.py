import math
N = 10 ** 6
primes = [1] * (N + 1)
primes[0] = primes[1] = 0
for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i] == 1:
        for j in range(i, (N // i) + 1):
            primes[i * j] = 0

for i in range(2, N + 1):
    primes[i] = primes[i - 1] + primes[i]

t = int(input())
for _ in range(t):
    n = int(input())
    print(primes[n] - primes[(n // 2)])



#not req, can read if u have time
"""
First, recall the original sieve idea (the normal way of finding primes).
You start from 2 and go upward. When you mark a number as prime, you eliminate all of its multiples. In the end, the numbers that survive are exactly the prime numbers ≤ N. So the first list is simply:
→ all primes in the range 2 to N.
Now look carefully at the modified algorithm, which works in reverse.
You start from N and go downward.
When you mark a number x as prime, you eliminate all of its factors (except itself).
So a number gets removed (marked “not prime”) if it is a factor of some larger number.
This observation is the key.
Think about a number k between 2 and N.
k will be marked not prime in the modified algorithm if and only if there exists some number m > k such that
k divides m.
But that just means:
there exists a multiple of k greater than k and ≤ N.
The smallest such multiple is 2k.
So:
	• If 2k ≤ N, then k will eventually be removed.
	• If 2k > N, then k can never be a factor of any larger number in the range.
This gives a very clean rule:
• If k ≤ N/2, then k will be eliminated in the modified method.
• If k > N/2, then k will survive and be marked as prime in the modified method.
So the second list (from the modified algorithm) is:
→ all numbers in the range (N/2, N], regardless of whether they are actually prime or composite.
Now we want numbers that appear in both lists.
From the first list: only true primes.
From the second list: all numbers greater than N/2.
So the intersection is:
→ prime numbers strictly greater than N/2 and ≤ N.
That’s the final insight.
In simple words, the answer for each test case is:
Count how many prime numbers lie in the range (N/2, N].
Let’s quickly verify with the examples.
For N = 2
N/2 = 1
Primes in (1, 2] → {2}
Answer = 1
For N = 4
N/2 = 2
Primes in (2, 4] → {3}
Answer = 1
For N = 7
N/2 = 3.5
Primes in (3.5, 7] → {5, 7}
Answer = 2
Matches perfectly.
So algorithmically, the problem reduces to:
	1. Precompute all primes up to 10⁶ (using a normal sieve).
	2. For each N, count primes in the interval (N/2, N].

Once you see this property, the problem becomes very elegant instead of confusing.
"""