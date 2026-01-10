n=int(input())
prices=list(map(int,input().split()))
n=len(prices)
left=[0]*n
right=[0]*n

left[0]=0
right[n-1]=0

leftmin=prices[0]
rightmax=prices[n-1]

for i in range(1,n):
    j=n-1-i
    leftmin=min(leftmin,prices[i])
    left[i]=max(left[i-1],prices[i]-leftmin)
    rightmax=max(rightmax,prices[j])
    right[j]=max(right[j+1],rightmax-prices[j])

maxprofit=0
for i in range(n):
    maxprofit=max(maxprofit,left[i]+right[i])
print(maxprofit)


"""
tarun logic

n=int(input())
arr=list(map(int,input().split()))

sMax=[0]*n
sMax[-1]=arr[-1]
for i in range(n-2,-1,-1):
    sMax[i]=max(sMax[i+1],arr[i])
ans=[0]*n
for i in range(n-2,-1,-1):
    ans[i]=max(ans[i+1],sMax[i]-arr[i])
pMin=arr[0]
re=0
for i in range(1,n-2):
    pMin=min(pMin,arr[i])
    re=max(re,(arr[i]-pMin)+ans[i+1],ans[i])
re=max(re,ans[0])
print(re)


     #code i wrote seeing trn solution.
n=int(input())
arr=list(map(int,input().split()))

ans=[0]*n
smax=arr[-1]
for i in range(n-2,-1,-1):
    smax=max(smax,arr[i])
    ans[i]=max(ans[i+1],smax-arr[i])

res=0
pmin=arr[0]
for i in range(n-1):
    pmin=min(pmin,arr[i])
    res=max(res,arr[i]-pmin+ans[i+1],ans[i])
print(res)
"""


# as i expected below is working
"""
n=int(input())
arr=list(map(int,input().split()))

ans=[0]*n
smax=arr[-1]
for i in range(n-2,-1,-1):
    smax=max(smax,arr[i])
    ans[i]=max(ans[i+1],smax-arr[i])

res=0
pmin=arr[0]
for i in range(n-1):
    pmin=min(pmin,arr[i])
    res=max(res,arr[i]-pmin+ans[i])     //this works!! my understanding     [1,10,20]  bitco transaction:(1rs bitco pen bought, sold for 10rs), parker transaction:(bought parker pen for 10rs and sold for 20rs)
print(res)

"""

"""
n=int(input())
prices=list(map(int,input().split()))
n=len(prices)
left=[0]*n
right=[0]*n

left[0]=0 # this is not prefixmax computation etc, so left[0]=prices[0] will be incorrect
right[n-1]=0#because we can't make any profit with just 1 element

leftmin=prices[0]
rightmax=prices[n-1]

for i in range(1,n):
    j=n-1-i
    leftmin=min(leftmin,prices[i])#find the minimum price till now

    left[i]=max(left[i-1],prices[i]-leftmin)#prices[i]-prices[i-1] will be incorrect. // max of selling today or skipping (previous max profit)

    rightmax=max(rightmax,prices[j])#find the maximum price to the right

    right[j]=max(right[j+1],rightmax-prices[j])#max of buying today or skipping


maxprofit=0
for i in range(n):
    maxprofit=max(maxprofit,left[i]+right[i])
print(maxprofit)
"""


"""
The idea here is to set a break point before which we have completed the first transaction and will complete the second transaction in the remaining days. There are N -1 such break points. Instead of explicitly setting break points and computing the profit for the left part and right part, we precompute the profit for every break point. Starting from the left, for every element we check the least price in the array to its left and check if the selling at current price can make us a larger profit than skipping it. Similarly, starting from the right, for every element, we check the array to the right of it and find an element larger to the current; and check if buying at current price makes us a larger profit than skipping it. This will be clear with the example mentioned below:

int maxProfit(vector<int>& prices) {
        if(!prices.size())
            return 0;
        int n = prices.size();
        int left[n], right[n];
        int leftmin = prices[0], rightmax = prices[n-1], maxprofit = 0;
        left[0] = 0; right[n - 1] = 0;                                     // because we can't make any profit with just 1 element
        int i,j;
        for(i = 1, j = n-2; i < n, j >= 0; i++, j--){
            leftmin  = min(leftmin, prices[i]);                            // find the minimum price till now
            left[i]  = max(left[i - 1], prices[i] - leftmin);              // max of selling today or skipping (previous max profit)
            rightmax = max(rightmax, prices[j]);                           // find the maximum price to the right
            right[j] = max(right[j + 1], rightmax - prices[j]);            // max of buying today or skipping
        }
        for(int i = 0; i < n; i++){
            maxprofit = max(maxprofit, left[i] + right[i]);
        }
        return maxprofit;
    }


//PRICES = [3,3,5,0,0,3,1,4]
// LEFT =    [0,0,2,2,2,3,3,4]
// RIGHT = [4,4,4,4,4,3,3,0]
// SUM =   [4,4,6,6,6,6,6,4]
// MAX PROFIT = 6
"""



"""
tarun logic

n=int(input())
arr=list(map(int,input().split()))

sMax=[0]*n
sMax[-1]=arr[-1]
for i in range(n-2,-1,-1):
    sMax[i]=max(sMax[i+1],arr[i])
ans=[0]*n
for i in range(n-2,-1,-1):
    ans[i]=max(ans[i+1],sMax[i]-arr[i])
pMin=arr[0]
re=0
for i in range(1,n-2):
    pMin=min(pMin,arr[i])
    re=max(re,(arr[i]-pMin)+ans[i+1],ans[i])
re=max(re,ans[0])
print(re)
"""


"""
Q.Why using ans[i+1] in this line ?: re=max(re,(arr[i]-pMin)+ans[i+1],ans[i])
They are ensuring the two transactions don’t overlap:

First transaction ends at day i

Second transaction starts at day i+1

They use ans[i+1] to avoid overlap between the two transactions.


Q.if ans[i+1] is used to avoid overlap, my solution is working which has overlap...so will trn solution work if u use ans[i] in this line? re=max(re,(arr[i]-pMin)+ans[i],ans[i])  ANS: NO!
Reason:

prices = [1, 5, 3, 8]
Trace one iteration:

pMin = 1

arr[2] = 3

arr[2] - pMin = 2 → buy at 1, sell at 3 (first transaction)

ans[2] = 5 → best profit from day 2 onward: buy at 3, sell at 8 (second transaction)

🚨 Problem:

Day 2 (price 3) is being used twice:

->Once to sell

->Once to buy

You're effectively saying:

"I’ll sell stock A at price 3 and also buy stock B at price 3 — on the same day."

But the problem constraint is:

Only one transaction at a time → no double-trading on the same day

So this breaks the rule.

✅ Why ans[i+1] Fixes It:
When you use ans[i+1], you're saying:

First transaction ends at day i

Second transaction starts at day i+1

So there is no overlap, no shared action on the same day

This keeps both transactions safely separated.


Q. So why my solution is working with overlap? 
✅ The Key Idea:
Your code allows a split at day i, where both transactions can "touch" day i, but they don't reuse the same action (buy or sell).

This is the critical difference between your overlap and the bad overlap in the other solution.

🧠 What does left[i] + right[i] mean?
You're computing:

left[i]: best profit from day 0 to day i

right[i]: best profit from day i to day n-1

You allow the same day i to be the sell of first and buy of second transaction.

So the "overlap" is at day i, but only in terms of time, not in terms of reuse of buy/sell.

This is why your code works.


📌 Why Your Overlap is Safe (Important)
Imagine:

Day 0   1   2   3   4
Price: 1   5   3   8   6
Now:

left[2] = max profit from day 0 to 2
→ Buy at 1, sell at 5 ⇒ 4 (or maybe at 3 ⇒ 2)

right[2] = max profit from day 2 to end
→ Buy at 3, sell at 8 ⇒ 5

You're doing:

left[2] + right[2] = 4 + 5 = 9
Both profits might involve day 2, but they do not both:

Sell on day 2 and

Buy on day 2

They just happen to split the timeline at day 2.
The two profits are calculated independently, and at most, one transaction uses day 2 as a buy or sell, not both.

So the "overlap" is:

At the boundary

But actions don't overlap — and that's why it works!




Q.why my code is working with right[i],  and tarun code will not work if we use ans[i] instead of ans[i+1]?
Clarification of the Rules:
Overlap: Two transactions can meet at the same day, but the first transaction must sell before or on the same day the second transaction buys. You cannot perform buy and sell actions on the same day for a single transaction. Two different transactions can share the same day for their sell and buy, but the same transaction cannot buy and sell on the same day.

Correct Explanation:
Transaction 1: You buy on day i and sell on day j (where j > i).

Transaction 2: You can buy on day j and sell on a later day k (where k > j).

The transactions can meet at day j, but the important point is:

You can't sell on day j and buy on day j for the same transaction.

Example:
Transaction 1:
Buy on day 2, Sell on day 4.

Transaction 2:
Buy on day 4, Sell on day 6.

Here, the first transaction sells on day 4, and the second transaction buys on day 4. This is fine, as the two transactions are allowed to meet at day 4, but the sell of transaction 1 happens before the buy of transaction 2.

What’s Not Allowed:
Buying and selling on the same day within the same transaction is not allowed.

For example:

If you buy on day 4, you cannot sell on day 4 within the same transaction.

So, What Does "Overlap" Mean?
You can have overlapping transactions: The first transaction can sell on day i, and the second transaction can buy on day i. But:

You cannot perform both buying and selling in the same transaction on the same day.




Doubt Question:
re=max(re,(arr[i]-pMin)+ans[i+1],ans[i])
in this line ans[i] represents single transaction right?
so in the same way , arr[i]-pmin will represent single transaction right?
so shouldn't the line be like below
re=max(re,(arr[i]-pMin)+ans[i+1],ans[i],arr[i]-pMin)

or is my understanding wrong?



Answer: Great question — your understanding is close, but there’s a subtle but important reason why the original line doesn't need the extra arr[i] - pMin.

Let’s walk through the logic to clarify it.

The Goal
You're solving the classic problem: find the maximum profit from at most two non-overlapping stock transactions.

Code Breakdown
You have:

sMax[i] = max of arr[i:] (i.e., future max prices from i)

ans[i] = max single-transaction profit starting from i to end (future window)

pMin = min of arr[:i] (past min prices up to i)

Then:
re=max(re,(arr[i]-pMin)+ans[i+1],ans[i])
Let’s interpret each term:
arr[i] - pMin: This is the first transaction profit if you buy at the lowest price before i and sell at i.

ans[i+1]: This is the second transaction profit from index i+1 onward.

So (arr[i]-pMin)+ans[i+1] is the sum of two transactions, first ending at i, second starting after i.

ans[i] is the best single transaction profit from index i onward (without combining with any earlier one).

So now your question:

Shouldn't it be:
re=max(re,(arr[i]-pMin)+ans[i+1], ans[i], arr[i]-pMin)?

Answer: No, you don’t need arr[i] - pMin separately, because:
It’s already implicitly included in the (arr[i] - pMin) + ans[i+1] case (when followed by a second transaction),

And if it's better to do just one transaction, then ans[i] already handles that,

Adding arr[i] - pMin alone would be a partial profit (only one transaction before i) — but it's not necessarily better than ans[i], which considers all future profits.

So the existing line is already optimal:
re = max(re, (arr[i]-pMin) + ans[i+1], ans[i])

You're correct that arr[i] - pMin is a single transaction, but it's a partial case that's already considered inside (arr[i]-pMin)+ans[i+1] and ans[i]. Including it separately would be redundant.

Would you like a visual example with numbers to see how each term plays out?

Tip: Debug examples for better understanding.



"""

#asked the below question in perplexity comparing my solution and tarun solution and it answered correctly!!! must check
"""
my solution:
---------------------
n=int(input())
arr=list(map(int,input().split()))

ans=[0]*n
smax=arr[-1]
for i in range(n-2,-1,-1):
smax=max(smax,arr[i])
ans[i]=max(ans[i+1],smax-arr[i])

res=0
pmin=arr[0]
for i in range(n-1):
pmin=min(pmin,arr[i])
res=max(res,arr[i]-pmin+ans[i])
print(res)


friend solution:
-----------------------
n=int(input())
arr=list(map(int,input().split()))

ans=[0]*n
smax=arr[-1]
for i in range(n-2,-1,-1):
smax=max(smax,arr[i])
ans[i]=max(ans[i+1],smax-arr[i])

res=0
pmin=arr[0]
for i in range(n-1):
pmin=min(pmin,arr[i])
res=max(res,arr[i]-pmin+ans[i+1],ans[i])
print(res)


Question:
res = max(res, arr[i] - pmin + ans[i+1], ans[i])

in this line isn't my friend missing  the case when : arr[i] - pmin + ans[i] ??


answer:
Think of it this way: for each index i, arr[i] - pmin + ans[i] is never strictly better than things your friend already checks.

Meaning of each term
arr[i] - pmin
Best profit of one transaction in prefix [0..i] that sells exactly at day i.

ans[i]
Best profit of one transaction in suffix [i..n-1].

ans[i+1]
Best profit of one transaction in suffix [i+1..n-1].

And ans is built as:
ans[i] = max(ans[i+1], smax - arr[i])

So for every i:

Either ans[i] = ans[i+1], or

ans[i] = smax - arr[i] > ans[i+1] (a transaction that buys at i).

These are the only two possibilities.

Case 1: ans[i] = ans[i+1]
Then:
arr[i]−pmin+ans[i]=arr[i]−pmin+ans[i+1]
So the “missing” term arr[i] - pmin + ans[i] is exactly the same number as the one your friend already uses: arr[i] - pmin + ans[i+1].
In this case, nothing is missed.


Case 2: ans[i] = smax - arr[i] > ans[i+1]
Here ans[i] is coming from a trade that buys at day i and sells later at some j > i.

So:

First part: arr[i] - pmin ⇒ best transaction in [0..i] that sells at i.

Second part: ans[i] = (sell at j) - arr[i] ⇒ second transaction buys at i, sells at some j > i.

Total:

arr[i]−pmin+ans[i]=(arr[i]−pmin)+((sell_price_at_j)−arr[i])=(sell_price_at_j)−pmin

This is exactly the profit of one single transaction: buy at the same pmin and sell at day j.
In other words, those “two” trades:

buy at pmin, sell at i

buy at i, sell at j

are equivalent in profit to:

buy at pmin, sell at j

So:

The value arr[i] - pmin + ans[i] is not a new kind of 2‑transaction profit.

It is just the profit of some single transaction that is already counted somewhere inside ans[k] for some k (because every best 1‑transaction interval lives in some suffix).

Your friend’s max(res, arr[i] - pmin + ans[i+1], ans[i]) already checks:

arr[i] - pmin + ans[i+1]: genuine 2‑transaction case, first in [0..i], second in [i+1..n-1].

ans[i]: best single transaction in [i..n-1].

The “fake 2‑transaction” value arr[i] - pmin + ans[i] reduces to a single interval profit (sell@j - pmin), and that single interval is included in some ans[k]. So it can never give a strictly larger answer than values obtained from:

some arr[x] - pmin_x + ans[x+1], or

some ans[x].

That is why skipping arr[i] - pmin + ans[i] does not lose any real optimal case, and both your solution and your friend’s still produce the same maximum profit.
"""





#asked perplexity regarding the weird looping conditions in tarun solution: can read , not mandatory
"""
n=int(input())
arr=list(map(int,input().split()))

sMax=[0]*n
sMax[-1]=arr[-1]
for i in range(n-2,-1,-1):
    sMax[i]=max(sMax[i+1],arr[i])
ans=[0]*n
for i in range(n-2,-1,-1):
    ans[i]=max(ans[i+1],sMax[i]-arr[i])
pMin=arr[0]
re=0
for i in range(1,n-2):     # here why the loop is from 1 to n-2?
    pMin=min(pMin,arr[i])
    re=max(re,(arr[i]-pMin)+ans[i+1],ans[i])
re=max(re,ans[0])
print(re)


Question: why the loop is from 1 to n-2?
The loop for i in range(1, n-2): is trying (a bit clumsily) to avoid using the extreme ends as split points between the two transactions, and then fixes remaining edge cases with re = max(re, ans[0]) at the end.​

What a split index means
Inside the loop:

python
pMin = min(pMin, arr[i])
re = max(re, (arr[i] - pMin) + ans[i+1], ans[i])
arr[i] - pMin = best first transaction in prefix [0..i].

ans[i+1] = best second transaction in suffix [i+1..n-1].

So i is the split point: first transaction uses days ≤ i, second transaction uses days ≥ i+1.​

To have two real transactions:

The prefix must have at least 2 days (to buy and sell).

The suffix must have at least 2 days as well.

That means:

First part [0..i] length ≥ 2 ⇒ i ≥ 1.

Second part [i+1..n-1] length ≥ 2 ⇒ n-1 - (i+1) + 1 = n - i - 1 ≥ 2 ⇒ i ≤ n-3.

So valid i for a genuine “2‑transaction split” are i ∈ [1, n-3], which is exactly what range(1, n-2) gives.

What about 1‑transaction answers?
Inside the loop it also checks ans[i] (best single transaction in [i..n-1]).

After the loop, re = max(re, ans[0]) ensures the best single transaction anywhere is considered.​

So:

i from 1 to n-3 → all valid 2‑transaction splits.

Final max with ans[0] → any best single transaction.

That’s why the loop is 1 to n-2: it’s implicitly enforcing “both sides big enough to contain a full transaction” and leaving pure 1‑transaction cases to ans[0].

Question: n-2 to n-1 is also a valid 2-transaction split right?
i = n-2 is not a valid split if you require both transactions to have at least 2 days (one buy day and one sell day).

Recall the split meaning in that code:

First transaction uses days in [0..i].

Second transaction uses days in [i+1..n-1].

If you choose i = n-2:

Prefix: [0..n-2] → length = n-1 (ok, enough days).

Suffix: [n-1..n-1] → length = 1.

A segment of length 1 cannot hold a full transaction (you would buy and sell on the same day, profit 0); effectively, there is no meaningful second transaction on [n-1..n-1].

That is why the mathematically valid 2‑transaction splits (where both sides have ≥ 2 days) are only for i in [1, n-3], implemented as range(1, n-2).

Question: then what happens to last 2 indices? are they not considered ?
They are considered, just not as part of a “second transaction segment that has at least 2 days” starting at i+1 in that loop. The profit that uses the last 2 indices is captured in ans[], not via the split loop.

Where last two indices are handled
Remember:

python
sMax[-1] = arr[-1]
for i in range(n-2,-1,-1):
    sMax[i] = max(sMax[i+1], arr[i])

ans[-1] = 0  # implicitly
for i in range(n-2,-1,-1):
    ans[i] = max(ans[i+1], sMax[i] - arr[i])
ans[i] is “best single-transaction profit in [i..n-1]”.

So:

ans[n-2] = best transaction in [n-2, n-1] (exactly the last two indices).

ans[n-3] can use [n-3..n-1], etc.

Then the combination loop:

python
for i in range(1, n-2):
    pMin = min(pMin, arr[i])
    re = max(re, (arr[i] - pMin) + ans[i+1], ans[i])

re = max(re, ans[0])
Any profit that uses indices n-2 and n-1 as a single transaction is inside ans[n-2] and thus inside ans[0] as well (because ans[0] is max over the whole array).

Any 2‑transaction combination where the second transaction uses the last two indices comes from some ans[i+1] with i+1 ≤ n-2, which the loop sees for i ≤ n-3.

So:

The last two indices are fully considered for:

A single transaction (via ans[n-2], ans[0]).

As part of the second transaction in a 2‑transaction split (via ans[i+1] for some i).

What is not considered is a degenerate split where the “second segment” is only [n-1] (length 1), because that cannot form a profitable second transaction anyway, so skipping i = n-2 in the loop does not lose any valid profit case.
"""