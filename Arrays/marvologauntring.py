n,p,q,r=map(int,input().split())
arr=list(map(int,input().split()))
pmax=[0]*n
smax=[0]*n
pmax[0]=arr[0]*p
smax[-1]=arr[-1]*r
for i in range(1,n):
    pmax[i]=max(pmax[i-1],arr[i]*p)

for i in range(n-2,-1,-1):
    smax[i]=max(smax[i+1],arr[i]*r)

ans=float('-inf')
for i in range(n):
    ans=max(ans,pmax[i]+arr[i]*q+smax[i])
print(ans)
