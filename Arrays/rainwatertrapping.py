n=int(input())
arr=list(map(int,input().split()))

pmax=[0]*n
smax=[0]*n
pmax[0]=arr[0]
smax[-1]=arr[-1]
for i in range(1,n):
    pmax[i]=max(pmax[i-1],arr[i])
for i in range(n-2,-1,-1):
    smax[i]=max(smax[i+1],arr[i])

ans=0
for i in range(1,n-1):
    h1=pmax[i] #h1=pmax[i-1] this is correct actually
    h2=smax[i] #h2=smax[i+1]
    h=arr[i]
    decide_h=min(h1,h2)
    if decide_h>h:
        ans+=(decide_h-h)
print(ans)