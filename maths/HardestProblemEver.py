t = int(input())

def findgcd(a, b):
    maxm = max(a, b)
    minm = min(a, b)
    while maxm % minm != 0:
        temp = maxm
        maxm = minm
        minm = temp % minm
    return minm


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    if n < 2 and arr[0] != 1:
        print(0)
        continue
    elif n < 2 and arr[0] == 1:
        print(1)
        continue

    gcd = findgcd(arr[0], arr[1])
    if gcd == 1:
        print(1)
        continue
    for i in range(2, n):
        gcd = findgcd(gcd, arr[i])
        if gcd == 1:
            print(1)
            break
    if gcd > 1:
        print(0)




#simple:
t = int(input())

def findgcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    g = arr[0]
    for i in range(1, n):
        g = findgcd(g, arr[i])

    if g == 1:            #alternately print(1 if g == 1 else 0)
        print(1)
    else:
        print(0)

        

"""
Let’s restate what the function really does.
For any non-empty subsequence:
	• Divisors(subsequence) returns 0 if there exists some integer j ≥ 2 that divides every element of that subsequence.
→ i.e., the subsequence has a common divisor ≥ 2
→ equivalently, its gcd > 1.
	• Otherwise it returns 1
→ i.e., the gcd of the subsequence is 1.
We then take the bitwise OR of these results over all subsequences.

Key observation
The OR becomes 1 if there exists at least one subsequence whose gcd is 1.
The OR becomes 0 only if every subsequence has gcd > 1 — which can happen only when all numbers share a common divisor ≥ 2.
That means:
	🔑 The final answer is 0 iff gcd(A[0], A[1], …, A[N−1]) > 1.
	Otherwise the answer is 1.

So you never need to iterate over subsequences.


Algorithm
For each test case:
	1. Read the array.
	2. Compute the gcd of all elements.
	3. If gcd == 1 → print 1
else → print 0

Example
Array: [2, 3]
	• gcd(2, 3) = 1 → so the answer is 1
(Matches the sample: only because the subsequence [2,3] has gcd 1.)

Complexity
Computing gcd over N numbers: O(N log max(A[i])) — efficient for the constraints.



my question:
so for subsequence of just 1 elements , as any element has factor as 1 and itself,
there exists  integer j ≥ 2 (here the number itself ) that divides every element(here the element itself) of that subsequence.

so we should return 0 for every subsequence of length 1?

the above is correct✅ , but for [1] we should return 1

What the function actually checks
Inside the loop:

for (j = 2; j <= number; j++) {
    if (number % j == 0) {
        count[j]++;
        if (count[j] == subsequence.length)
            return 0;
    }
}
For a single-element subsequence:
	• subsequence.length = 1
	• count[j] becomes 1 the first time j divides that number.
	• As soon as that happens, the condition

count[j] == subsequence.length   // 1 == 1
becomes true → the function returns 0.
This happens for j = the number itself (if ≥ 2), and often for other divisors > 1 too.
So:
	✔ If the element is ≥ 2 → Divisors([x]) returns 0.
What if the element is 1?
	• The inner loop runs for (j = 2; j <= number)
	• But since number = 1, the loop doesn’t run at all.
	• No count[j] reaches subsequence.length.
	• So the function reaches the end and returns 1.
	✔ Divisors([1]) returns 1.








Why our earlier rule still holds
A subsequence returns 1 exactly when its gcd is 1.
Single-element subsequences have:
	• gcd(x) = x →
returns 1 only if x = 1.
And the OR over all subsequences is 1 iff some subsequence has gcd 1, which is equivalent to saying the overall array gcd is 1.






Simple solution:
t = int(input())

def findgcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    g = arr[0]
    for i in range(1, n):
        g = findgcd(g, arr[i])

    if g == 1:            #alternately print(1 if g == 1 else 0)
        print(1)
    else:
        print(0)


✔️ Why this works
	• If gcd(arr) == 1 → some subsequence has gcd 1 → OR becomes 1
	• If gcd(arr) > 1 → every subsequence has gcd > 1 → OR becomes 0
That matches exactly what the original Divisors function does.



✔ Why this works
Even when n = 1, the gcd of the array is just the element itself.
The loop only reduces the gcd when there are more elements — otherwise it simply never runs.
So:
arr	gcd	output
[1]	1	1
[7]	7	0
[2, 3]	1	1
[4, 8]	4	0
All correct.

"""