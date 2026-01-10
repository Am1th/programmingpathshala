# t=int(input())
# for _ in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     dict1={}
#     for ele in arr:
#         dict1[ele]=1+dict1.get(ele,0)

#     # flag=False
#     # for key in dict1:
#     #     if dict1[key]>n//3:
#     #         flag=True
#     #         print(key,end=" ")
#     # if flag==False:print(-1)
#     # print()


#     result=[]
#     for key in dict1:
#         if dict1[key]>n//3:
#             result.append(key)
#     if result:
#         result.sort()
#         print(" ".join(map(str,result)))
#     else:
#         print(-1)


# hashmap
# t=int(input())
# for _ in range(t):
#     N=int(input())
#     nums=list(map(int,input().split()))
#     count={}
#     ls=[]
#     for n in nums:
#         count[n]=1+count.get(n,0)
#         if count[n]==(N//3)+1:
#             ls.append(n)
#         if len(ls)==2:break
#     if ls:
#         ls.sort()
#         print(*ls)
#     else:print(-1)


# t=int(input())
# for _ in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     ele1,cnt1=float('-inf'),0
#     ele2,cnt2=float('-inf'),0
#     for i in range(n):
#         if cnt1==0 and arr[i]!=ele2:
#             ele1=arr[i]
#             cnt1=1
#         elif cnt2==0 and arr[i]!=ele1:
#             ele2=arr[i]
#             cnt2=1
#         elif arr[i]==ele1:cnt1+=1
#         elif arr[i]==ele2:cnt2+=1
#         else:
#             cnt1-=1
#             cnt2-=1
#     result=[]
#     cnt1,cnt2=0,0
#     for i in range(n):
#         if arr[i]==ele1:cnt1+=1
#         if arr[i]==ele2:cnt2+=1

#     if cnt1>n//3:result.append(ele1)
#     if cnt2>n//3:result.append(ele2)
#     if result:
#         result.sort()
#         print(*result)
#     else:print(-1)


# neetcode
# logic: when length of hashmap becomees >2 (or =3),decrement count of every single number. if count of any of the elements is equal to zero, remove that ele from hashmap.
# we can put all ele of array into dictionary and then traverse dict and check, but to reduce space complexity, we are adding elements from array one by one to dict, and if length of hashmap becomes>2 .. perform logic
from collections import defaultdict

t = int(input())
for _ in range(t):
    N = int(input())
    nums = list(map(int, input().split()))
    count = defaultdict(int)
    for n in nums:
        count[n] += 1

        if len(count) <= 2: continue

        new_count = defaultdict(int)
        for n, c in count.items():
            if c > 1:
                new_count[n] = c - 1

        count = new_count

    # res=[]
    # if not count:
    #     print(-1)
    #     continue
    # for n in count:
    #     if nums.count(n)>N//3:res.append(n)
    # res.sort()
    # print(*res)

    res = [n for n in count if nums.count(n) > N // 3]
    """ print(*res if res else -1)
    the above line is evaluated as below
    val = res if res else -1
    print(*val)
    """
    # works
    # if res:res.sort()
    # print(*(res if res else [-1])) #can remove braces after * and will wrk

    print(*(sorted(res) if res else [-1]))

    # works
    # if res:
    #     res.sort()
    #     print(*res)
    # else:
    #     print(-1)




# did below while practing, working solution same replicate of above.
# from collections import defaultdict
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     dict1=defaultdict(int)
#     for i in range(n):
#         dict1[arr[i]]+=1
#         if len(dict1)<3:continue
#         dict2=defaultdict(int)
#         for key in dict1:
#             if dict1[key]>1:
#                 dict2[key]=dict1[key]-1
#         dict1=dict2
#     result=[]
#     for key in dict1:
#         if arr.count(key)>n//3:result.append(key)
#     print(*sorted(result) if result else [-1])






"""
is below correct?
result=[key for key in dict1 if nums.count(key)>n//3 else -1]


The code you've written:

result = [key for key in dict1 if nums.count(key) > n // 3 else -1]


is not valid Python syntax. The issue lies in the use of else inside a list comprehension's if clause — that's not how conditionals work in list comprehensions.

🔍 What You're Trying to Do

It looks like you want to build a list of keys from dict1 where each key occurs in nums more than n // 3 times — otherwise, maybe append -1.

Let’s clarify your intention:

Option A: You want a list of qualifying keys, or if none qualify, just [-1]

Option B: You want to include -1 in the result list for each key that doesn’t satisfy the condition.

Can you confirm which one you're trying?

✅ Correct Version for Option A:

If you want to include only the keys that meet the condition:

result = [key for key in dict1 if nums.count(key) > n // 3]
if not result:
    result = [-1]
    
    
(the same above, while coding i did as below) : 
res = [n for n in count if nums.count(n) > N // 3]
print(*res if res else -1)




✅ Correct Version for Option B:

If you want to include either the key (if it satisfies) or -1 (if it doesn't):

result = [key if nums.count(key) > n // 3 else -1 for key in dict1]


This version uses a ternary expression, which is the correct way to use if-else inside list comprehensions.
"""