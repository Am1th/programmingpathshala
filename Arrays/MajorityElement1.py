# n=int(input())
# dict1={}
# arr=list(map(int,input().split()))
# for ele in arr:
#     if ele in dict1:
#         dict1[ele]+=1
#     else:
#         dict1[ele]=1

# for ele in dict1:
#     if dict1[ele]>n/2:
#         print(ele)
#         break


# hashmap, neetcde
# N=int(input())
# nums=list(map(int,input().split()))
# count={}
# res,maxCount=0,0
# for n in nums:
#     count[n]=1+count.get(n,0)
#     res=n if count[n]>maxCount else res
#     maxCount=max(count[n],maxCount)
#     # not required,just for testing
#     # maxCount=max(count[n],maxCount)
#     # res=n if count[n]==maxCount else res
# print(res)


# Boyer Moore Algorithm
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if cnt == 0: ele = arr[i]
    # if arr[i]==ele:cnt+=1
    # else:cnt-=1
    cnt += (1 if arr[i] == ele else -1)
print(ele)


