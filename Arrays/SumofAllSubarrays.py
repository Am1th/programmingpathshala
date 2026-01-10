n = int(input())
arr = list(map(int, input().split()))
m = 10 ** 9 + 7
ans = 0
for i in range(n):
    contribution = (((i + 1 % m) * (n - i) % m) % m * arr[i] % m) % m   #( ( (i+1)%m * (n-i)%m) % m * arr[i]%m )%m
    ans = (ans % m + contribution % m) % m
print(ans)

# n^2 solution , TLE for 2 test cases
# n=int(input())
# arr=list(map(int,input().split()))
# m=10**9 + 7
# ans=0
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum+=arr[j]
#         # ans+=sum
#         ans=(ans%m + sum%m) % m
# print(ans)



"""
tarun logic
n=int(input())
arr=list(map(int,input().split()))

re=0
for i in range(n):
    re+=arr[i]*((i+1)*(n-i))

print(re%1000000007)
"""


# practice answer. TLE for 2 test cases
n = int(input())
arr = list(map(int, input().split()))

# def getSum(i,j):
#     sum=0
#     for k in range(i,j+1):
#         sum+=arr[k]
#     return sum

psum = [0] * n
psum[0] = arr[0]
for i in range(1, n):
    psum[i] = psum[i - 1] + arr[i]


def getSum(i, j):
    if i == 0:
        return psum[j]
    else:
        return psum[j] - psum[i - 1]


ans = 0
for i in range(n):
    for j in range(i, n):
        ans = (ans + getSum(i, j)) % 1000000007
print(ans)


"""
explain me this in more detail: 


n=int(input())
arr=list(map(int,input().split()))

ans=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum+=arr[j]
        ans+=sum  # writing this outside inner for loop vs writing like this , i am not getting
print(ans)



First: what do the loops REPRESENT?

for i in range(n):
    for j in range(i, n):

This loop structure enumerates all subarrays: 
    
| i | j | Subarray |
| - | - | -------- |
| 0 | 0 | arr[0:1] |
| 0 | 1 | arr[0:2] |
| 0 | 2 | arr[0:3] |
| 1 | 1 | arr[1:2] |
| 1 | 2 | arr[1:3] |
| 2 | 2 | arr[2:3] |


👉 Each (i, j) pair = exactly ONE subarray

This fact is critical.

Now focus on sum

sum += arr[j]

What is sum at any moment?

For a fixed i:

j	sum represents
i	sum(arr[i:i+1])
i+1	sum(arr[i:i+2])
i+2	sum(arr[i:i+3])

👉 sum = sum of subarray [i..j]

Case 1 ❌: ans += sum OUTSIDE inner loop

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
    ans += sum

What happens?
Inner loop finishes completely
sum now equals:

arr[i] + arr[i+1] + ... + arr[n-1]

That is ONLY the last subarray starting at i

So for each i, you add ONE subarray sum.

Meaning in plain English:

“For each starting index, add only the largest subarray.”

❌ This is not “all subarrays”.


Case 2 ✅: ans += sum INSIDE inner loop

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        ans += sum

What happens?

For each (i, j):
You update sum
Immediately add it to ans

So:
Every subarray sum is counted
Nothing is skipped

Meaning in plain English:
“Every time a new subarray is formed, add its sum.”
✅ This matches the problem definition.


The key misunderstanding (THIS is the heart of it)
You are thinking:
“I am already summing inside the loop, so adding once should be enough.”
But that sum is cumulative, not individual.

"""