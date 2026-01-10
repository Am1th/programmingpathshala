n,m=map(int,input().split())
arr=list(map(int,input().split()))
psum=[0]*n
psum[0]=arr[0]
for i in range(n):
    psum[i]=psum[i-1]+arr[i]

ans=0
sum=0
while (m>0):
    l,r= map(int,input().split())
    l=l-1
    r=r-1 #in sum  indexing starting from 1
    if l==0:  #in sum indexing starts from 1, so if l is 1, above we are decrementing it , so l becomes 0
        sum=psum[r]
    else:
        sum=psum[r]-psum[l-1]
    if sum>0:
        ans+=sum
    #ans+=max(0,sum) can write this instead of above if condition
    m=m-1
print(ans)



