n=int(input())
arr=list(map(int,input().split()))

smax=[0]*n
smax[-1]=arr[-1]
for i in range(n-2,-1,-1):
    smax[i]=max(smax[i+1],arr[i])

ans=float('-inf')
for i in range(n):
    ans=max(smax[i]-arr[i],ans)

if ans>0:print(ans)
else: print(0)    #print(ans if ans>0 else 0)

"""
tarun logic

n=int(input())
arr=list(map(int,input().split()))

pmin=arr[0]
ans=0
for i in range(1,n):
    pmin=min(arr[i],pmin)
    ans=max(ans,arr[i]-pmin)

print(ans)
"""