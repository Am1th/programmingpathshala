t = int(input())
def findgcd(a, b):
    minm = min(a, b)
    maxm = max(a, b)
    while (maxm % minm != 0):
        temp = maxm
        maxm = minm
        minm = temp % minm
    return minm


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dict1 = {}
    for i in range(n):
        dict1[arr[i]] = 1 + dict1.get(arr[i], 0)

    result = []
    for val in dict1.values():
        result.append(val)

    gcd = result[0]
    for i in range(len(result)):
        gcd = findgcd(gcd, result[i])

    if gcd >= 2:
        print("true")
    else:
        print("false")



#solution from chatgpt
import math
from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = Counter(arr).values()

    g = 0
    for f in freq:
        g = math.gcd(g, f)

    print("true" if g >= 2 else "false")

"""
The key idea is to think about how grouping actually works.

1️⃣ What does the problem really want?
We must split the array into groups such that:
	1. Every group has the SAME size X (and X ≥ 2)
	2. All numbers inside one group are identical
So, if a number appears freq times, we must divide those copies into groups:

freq = X + X + X + ... (some number of times)
This means:
🔴 freq must be divisible by X.
Example:
If a number appears 6 times, and X = 3:

6 = 3 + 3      ✔️ works
If X = 4:

6 = 4 + 2      ❌ doesn't work
So X must divide 6.

2️⃣ Apply that to ALL numbers
Let’s say frequencies are:
number	frequency
1	6
2	9
3	3
We need ONE single X that works for all of them.
X must divide:

6
9
3
What values divide all of them?
Divisors:
	• 6 → {1,2,3,6}
	• 9 → {1,3,9}
	• 3 → {1,3}
👉 The only common divisor = 3
So X = 3 works.
That means we CAN group:

1 1 1   |   1 1 1
2 2 2   |   2 2 2   |   2 2 2
3 3 3

3️⃣ Now look at the failing case
Array:
[1,1,1,2,2,2,3,3]
Frequencies:
number	frequency
1	3
2	3
3	2
What numbers can X be?
	• Possible group sizes for 3 → {1,3}
	• Possible group sizes for 2 → {1,2}
Common divisors across all frequencies = only 1
But X must be ≥ 2.
So no valid X exists → false.

4️⃣ Why are we using GCD?
The GCD (Greatest Common Divisor) of all frequencies is exactly:
	the largest number that divides ALL frequencies.
If:

GCD ≥ 2   → we can use X = GCD (or any divisor of it) → possible
GCD = 1   → no X ≥ 2 exists → impossible
So instead of testing every possible X, we just compute:

GCD of all frequencies

5️⃣ Visual intuition (very important)
Think of frequencies like piles of blocks.
If GCD = 2:

Each pile can be split into groups of 2 blocks.
If GCD = 3:

Each pile can be split into groups of 3 blocks.
If GCD = 1:

There is no group size ≥ 2 that fits all piles.

6️⃣ Re-explain in one sentence
	Count how many times each number appears.
	If there exists one group size X ≥ 2 that divides every frequency, answer is true.
	GCD tells us whether such an X exists.

🎯 Summary
	• Count frequency of each number
	• Compute GCD of frequencies
	• If GCD ≥ 2 → true
	• Otherwise → false

"""









"""
Questions based on second code:
what is this Counter? 
what is stored in freq? 
is it a list or what? what is the tc of the code?


Answers from chatgpt:

1️⃣ What is Counter?
Counter comes from:

from collections import Counter
It is a special dictionary designed for counting things.
When you do:

Counter(arr)
it automatically counts how many times each value appears.
Example:

arr = [1, 2, 2, 3, 3, 3]
c = Counter(arr)
Now c becomes:

{1: 1, 2: 2, 3: 3}
So instead of manually writing:

dict1[x] = 1 + dict1.get(x, 0)
Counter does it for you — internally it is still a hash map / dictionary.

2️⃣ What is stored in freq?
Code:

freq = Counter(arr).values()
Counter(arr) gives a dictionary like:

{ value : frequency }
.values() returns only the frequency numbers.
Example:

c = Counter([1,1,2,2,2,3])
c.values() → [2, 3, 1]
👉 Technically, it is not a list, it is a view object (like an iterable).
But you can loop over it like a list, which is exactly what we do:

for f in freq:
    ...
If you really want to see it as a real list, you could do:

list(freq)
but you don’t need to.

3️⃣ Time Complexity (TC)
Let’s analyze the optimized solution.

freq = Counter(arr).values()
Counting frequencies: O(N)
Then:

for f in freq:
    g = math.gcd(g, f)
Number of distinct values = k
(at worst, every element is different → k = N)
Each GCD operation is very fast (≈ log of value).
So this loop: O(k log M)
(where M is the max frequency — small compared to N)
Total:
✅ Time Complexity = O(N)
(for competitive programming, that’s perfect)

4️⃣ Space Complexity (SC)
We store frequency dictionary:
✅ Space = O(k)
(k = number of unique elements)
Worst case → O(N).

🎯 Quick recap (simple version)
Question	Answer
What is Counter?	A dictionary that counts elements automatically.
What is freq?	Iterable containing only the frequencies (like [2,3,1]).
TC of code?	O(N) (linear).





Questions:
you said tc if o(klogM) and again saying o(N)?
also dict1.values() which i wrote also returns view object iterable and not a list?

1️⃣ “You said O(k log M) and then O(N). Which one is right?”
Short answer:
	Exact expression: O(N + k log M)
	Simplified big-O: usually written as O(N) (because k ≤ N and log M is tiny)
Let’s unpack it.

🔹 Step-by-step complexity
1️⃣ Building the Counter

Counter(arr)
Visits each element once → O(N)

2️⃣ Looping through frequencies

for f in freq:
    g = gcd(g, f)
Let:
	• k = number of distinct numbers
	• M = maximum frequency
Loop length = k
Each gcd() call ≈ O(log M)
So loop = O(k log M)

🔹 Combine them

Total = O(N) + O(k log M)
Now, notice:
	• k ≤ N (you can’t have more distinct elements than total elements)
	• M ≤ N (a value cannot appear more than N times)
So worst-case:

O(N + k log M)  
→ O(N + N log N)  
→ O(N log N)
But in practice:
	• frequencies are often small
	• gcd is extremely fast
	• k is usually much smaller than N
So people commonly summarize this algorithm as:
	“linear time” → O(N)
because the dominating cost is counting elements.
Both statements are correct — one is precise, the other is simplified.

2️⃣ “Does my dict1.values() also return a view object?”
👉 YES — exactly.
In your code:

dict1.values()
returns a dict_values view, which:
	• is iterable
	• is not a list
	• reflects updates to the dictionary (lazy view)
Same behavior as:

Counter(arr).values()
Example proof:

d = {1: 2, 2: 3}
v = d.values()
print(v)          # dict_values([2, 3])
If you want a real list:

list(d.values())   # [2, 3]
But we don’t need a list — iterating the view is perfectly fine.

🎯 Final recap
Concept	Answer
Exact time complexity	O(N + k log M)
Simplified	Often written O(N)
Why simplifiable	k ≤ N and gcd is tiny cost
dict.values()	returns a view object, not a list
Counter.values()	also a view object


"""