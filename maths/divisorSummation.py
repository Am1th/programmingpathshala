import math
t = int(input())
def properDivisors(n):
    if n == 1: return 0
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            sum += n // i
            if i == n // i:
                sum -= i
    return sum

for _ in range(t):
    n = int(input())
    print(properDivisors(n))




#solution suggested by chatgpt, not required
import sys
import math

# Step 1: Sieve primes up to 31622
MAX = 31622
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

primes = []
for i in range(2, MAX + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False


def sum_of_proper_divisors(n):
    if n == 1:
        return 0

    original_n = n
    total_sum = 1

    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            power_sum = 1
            term = 1
            while n % p == 0:
                n //= p
                term *= p
                power_sum += term
            total_sum *= power_sum

    # If n is still > 1, it is a prime factor
    if n > 1:
        total_sum *= (1 + n)

    return total_sum - original_n


# Input handling
t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(sum_of_proper_divisors(n))

