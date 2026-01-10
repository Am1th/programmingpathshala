n, k = map(int, input().split())
arr = list(map(int, input().split()))

cntLegalElements = 0

for i in range(n):
    if arr[i] <= k:
        cntLegalElements += 1

max_cnt = 0
cnt = 0
for i in range(0, cntLegalElements):
    if arr[i] <= k:
        cnt += 1
max_cnt = max(max_cnt, cnt)

for j in range(cntLegalElements, n):
    if arr[j] <= k:
        cnt += 1
    if arr[j - cntLegalElements] <= k:
        cnt -= 1
    max_cnt = max(max_cnt, cnt)
print(cntLegalElements - max_cnt)


"""
tarunlogic
# cook your dish here

n,k=map(int,input().split())

arr=list(map(int,input().split()))

maxi=0
cnt=0
soFar=0
for i in range(n):
    
    if(arr[i]<=k):
        cnt+=1

reMax=0
cur=0

for i in range(cnt):
    if(arr[i]<=k):
        cur+=1
        

reMax=cur

for i in range(cnt,n):
    if(arr[i]<=k):
        cur+=1
    if(arr[i-cnt]<=k):
        cur-=1
    reMax=max(reMax,cur)

print(cnt-reMax)
"""