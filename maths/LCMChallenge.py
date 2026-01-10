n = int(input())
#arr = list(range(1, n + 1))   not required

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n % 2 != 0:     #when odd
    print(n * (n - 1) * (n - 2))
else:                #when even
    if n%3!=0:             #ex 8
        print(n * (n - 1) * (n - 3))
    else:                  #ex 6
        print((n-1) * (n - 2) * (n - 3))




#Doesnt work
# n=int(input())
# arr=[0]*n          #arr = list(range(1, n + 1))
# for i in range(1,n+1):
#     arr[i-1]=i
#
# def lcm(a,b):
#     return (a*b)//gcd(a,b)
#
# def lcm3(a,b,c):
#     return lcm(lcm(a,b),c)
# def gcd(a,b):
#     maxm=max(a,b)
#     minm=min(a,b)
#     while maxm%minm!=0:
#         temp=maxm
#         maxm=minm
#         minm=temp%minm
#     return minm
#
#
#
# pMaxLcm=[0]*n
# pMaxLcm[0]=arr[0]
# for i in range(1,n):
#     pMaxLcm[i]=max(pMaxLcm[i-1],lcm(pMaxLcm[i-1],arr[i]))
#
# sMaxLcm=[0]*n
# sMaxLcm[-1]=arr[-1]
# for i in range(n-2,-1,-1):
#     sMaxLcm[i]=max(sMaxLcm[i+1],lcm(sMaxLcm[i+1],arr[i]))
#
# ans=0
# for i in range(n):
#     ans=max(ans,lcm3(pMaxLcm[i],arr[i],sMaxLcm[i]))
#
# print(ans)



"""
Key idea:
	• Using bigger numbers usually increases the LCM — but only if they are not “too divisible” by each other.
	• We only need to reason about the largest few numbers (around n), because any smaller ones won’t help maximize the LCM.
Observations
	1. If n ≤ 2, the answer is simply n (because we can only choose numbers like 1,1,1 or 2,2,1).
	2. If n is odd, the numbers

n, n-1, n-2

are pairwise co-prime enough that their LCM is just their product — and this is optimal.
	3. If n is even, choosing n, n-1, n-3 works best.
(We skip n-2 because it’s also even, which would reduce the LCM.)
So the rule becomes:

if n <= 2: answer = n
else if n is odd: answer = n * (n-1) * (n-2)
else: answer = lcm(n, n-1, n-3)
We compute LCM with the formula:

lcm(a,b) = a*b / gcd(a,b) 





Goal: choose three numbers ≤ n whose LCM is as large as possible.

1️⃣ Why the “odd” case was easy
If n is odd, the three biggest numbers

n, n-1, n-2
are usually pair-wise co-prime (they don’t share big common factors).
So their LCM = their product — clearly the maximum.
Example: n = 9

LCM(9,8,7) = 504   (and it’s just 9×8×7)

2️⃣ What goes wrong when n is EVEN
Suppose n = 8.
If we naively copy the odd strategy:

LCM(8,7,6)
Notice something:
	• 8 is divisible by 2
	• 6 is also divisible by 2
	• and 8 and 6 share gcd = 2
Because they share factors, the LCM shrinks:

LCM(8,6) = 24   (not 8×6 = 48)
LCM(24,7) = 168
But look at this instead:

LCM(8,7,5)
Here, 5 does not share factors with 8:

LCM(8,7) = 56
LCM(56,5) = 280   (bigger!)
So:

LCM(8,7,5) = 280  >  168 = LCM(8,7,6)
👉 The problem with n-2 is that it’s also even, so it overlaps with n.

3️⃣ So why specifically choose (n, n-1, n-3)?
When n is even:

n     → even
n-1   → odd
n-2   → even   ❌ bad, overlaps with n
n-3   → odd    ✅ usually co-prime with n
So the best trio is:

n, n-1, n-3
	• n (even)
	• n-1 (odd)
	• n-3 (odd)
	• and they rarely share big gcds with each other
This makes the LCM roughly as large as the product again.
Example: n = 10
Try bad choice:

LCM(10,9,8) = 360
Try the chosen one:

LCM(10,9,7) = 630   ✔ bigger
Because 8 overlaps with 10 (both even), while 7 stays “independent”.



🎯 Summary intuition
	• Big numbers are good — unless they share factors.
	• When n is even, n-2 is also even → overlaps → hurts the LCM.
	• Replacing n-2 with n-3 avoids most overlaps, giving:

max LCM = lcm(n, n-1, n-3)



“Overlap means they share factors?”
Yes — exactly.
When I said overlap, I meant:
	Two numbers share a common divisor greater than 1 (i.e., their gcd > 1).
Examples:

8 and 6  -> share factor 2   -> overlap
10 and 8 -> share factor 2   -> overlap
12 and 9 -> share factor 3   -> overlap
When numbers overlap, the LCM does not grow as much as the product, because the shared factor is counted only once.
Formula:

lcm(a,b) = a * b / gcd(a,b)
So if gcd(a,b) is big → LCM becomes smaller.


Why avoiding n-2 matters for even n
If n is even:

n is even
n-2 is also even
So:

gcd(n, n-2) ≥ 2   (always)
Meaning they always overlap.
But n-3 is odd, so usually:

gcd(n, n-3) = 1   (or very small)
This helps maximize the LCM.
Example (n = 10):

LCM(10, 8) = 40       (gcd = 2 → overlap)
LCM(10, 7) = 70       (gcd = 1 → no overlap)
70 is larger than 40, so 7 is better than 8.



If n is even:
If n is not divisible by 3, answer is n⋅(n−1)⋅(n−3)
If n is divisible by 3, answer is (n−1)⋅(n−2)⋅(n−3)

is this case true? if so why?


es — that rule is correct, and it’s exactly the “more precise” version of the idea we discussed.
Let’s prove it carefully and intuitively.

We’re only considering two candidate triples (when n is even)
When n is even, the only triples that can possibly win are:

S1 = { n, n-1, n-3 }
S2 = { n-1, n-2, n-3 }
We choose between them depending on whether n is divisible by 3.

Case 1️⃣ — n is even AND not divisible by 3
Then:
	• n is even
	• n-1 is odd
	• n-3 is odd
	• and gcd(n, n-3) = 1 (because n is not divisible by 3)
So these three numbers are essentially pairwise co-prime, which makes:

LCM(n, n-1, n-3) = n · (n-1) · (n-3)
Meanwhile, n-2 (in S2) is even — it would overlap with some numbers and usually gives a smaller LCM.
➡️ So when n is not divisible by 3,
S1 wins:

answer = n · (n-1) · (n-3)

Case 2️⃣ — n is even AND divisible by 3
So now let:

n = 6k   (because it’s even AND multiple of 3)
Look again at:

S1 = { n, n-1, n-3 }
But here:
	• n is divisible by 3
	• n-3 is also divisible by 3
So:

gcd(n, n-3) = 3
That hurts the LCM.
Let’s compute it:

LCM(n, n-3) = n(n-3)/3
So:

LCM(S1) = n(n-1)(n-3)/3

Now look at:

S2 = { n-1, n-2, n-3 }
These three numbers are:
	• consecutive except missing n
	• and pairwise coprime:
Reason:
	• n-1 and n-2 are consecutive → gcd = 1
	• n-2 and n-3 are consecutive → gcd = 1
	• n-1 and n-3 differ by 2, both odd → gcd = 1
So:

LCM(S2) = (n-1)(n-2)(n-3)

Now compare S1 vs S2
We only need to compare:

n(n-1)(n-3)/3   vs   (n-1)(n-2)(n-3)
Cancel (n-1)(n-3) on both sides:

n/3   vs   n-2
Is n-2 bigger than n/3?
Yes, for all n ≥ 6:

n-2 > n/3
Therefore:

(n-1)(n-2)(n-3)   >   n(n-1)(n-3)/3
➡️ So when n is divisible by 3,
S2 wins:

answer = (n-1)(n-2)(n-3)

🎯 Final rule (clean summary)
If n is odd:

answer = n(n-1)(n-2)
If n is even:

if n % 3 != 0:
    answer = n(n-1)(n-3)
else:
    answer = (n-1)(n-2)(n-3)

"""