# n=int(input())
# arr=list(map(int,input().split()))
# max_cnt=0
# for i in range(n):
#     if arr[i]>=0:
#         ind=arr[i]
#         val=i
#         cnt=0
#         while(ind!=i):
#             temp=arr[ind]
#             arr[ind]=-(val+1)
#             val=ind
#             ind=temp
#             cnt+=1
#         arr[ind]=-(val+1)
#         cnt+=1
#         max_cnt=max(max_cnt,cnt)
# print(max_cnt)


#second way
n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n
max_cnt = 0

for i in range(n):
    if not visited[i]:
        ind, cnt = i, 0
        while not visited[ind]:
            visited[ind] = True
            ind = arr[ind]
            cnt += 1
        max_cnt = max(max_cnt, cnt)
print(max_cnt)



#the exact same above can be done as below (same code , just skipped if condition, but chatgpt and perplexity suggesting to use the if condition):
n=int(input())
arr=list(map(int,input().split()))
visited=[False]*n
max_cnt=0

for i in range(n):
    cnt=0
    while not visited[i]:
        visited[i]=True
        i=arr[i]
        cnt+=1
    max_cnt=max(max_cnt,cnt)
print(max_cnt)



"""
while practicing used function, same code only

n=int(input())
arr=list(map(int,input().split()))

def cycle(arr,i):
    cnt=0
    ind,val=arr[i],i
    while ind!=i:
        temp = arr[ind]
        arr[ind]=-(val+1)
        
        val=ind
        ind=temp
        cnt+=1
    arr[ind]=-(val+1)
    cnt+=1
    return cnt


cycle_len,max_cnt=0,0
for i in range(n):
    if arr[i]>=0:
        cycle_len=cycle(arr,i)
    max_cnt=max(cycle_len,max_cnt)
print(max_cnt)
            
        


"""




"""
while practicing , glanced at second way of ( from original code, second way) and did below:

n=int(input())
arr=list(map(int,input().split()))
visited=[False]*n

max_cnt=0
for i in range(n):
    if not visited[i]:
        ind=arr[i]  #val=i
        cnt=0
        while ind!=i: //while not visited[ind]:   (if u want to write like this see below code versions)
            temp=arr[ind]
            visited[ind]=True
            
            # val=ind
            ind=temp
            cnt+=1
        visited[ind]=True
        cnt+=1
        max_cnt=max(cnt,max_cnt)
print(max_cnt)



same above if u want to change inner while loop condition:
n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n

max_cnt = 0
for i in range(n):
    if not visited[i]:
        ind = i  # Start from i itself
        cnt = 0
        while not visited[ind]:
            visited[ind] = True
            ind = arr[ind]
            cnt += 1         #removed next 2 lines.
        max_cnt = max(cnt, max_cnt)

print(max_cnt)



same above if u want to change inner while loop condition:
n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n

max_cnt = 0
for i in range(n):
    if not visited[i]:
        ind = arr[i]
        visited[i] = True  # visit i explicitly
        cnt = 1
        while not visited[ind]:
            visited[ind] = True
            ind = arr[ind]
            cnt += 1
        max_cnt = max(cnt, max_cnt)

print(max_cnt)

"""