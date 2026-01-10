n, m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

# below using psum array, will increase space complexity
# psum=[]
# for _ in range(n):
#     row=[0]*m
#     psum.append(row)

# # calculate row wise prefix sum
# for i in range(n):
#     for j in range(m):
#         if j==0:
#             psum[i][j]=arr[i][j]
#         else:
#             psum[i][j]=psum[i][j-1]+arr[i][j]

# # calculate column wise prefix sum
# for i in range(1,n):
#     for j in range(m):
#         psum[i][j]=psum[i-1][j]+psum[i][j]

# calculate row wise prefix sum,modifying given array
for i in range(n):
    for j in range(1, m):
        arr[i][j] = arr[i][j - 1] + arr[i][j]

# calculate column wise prefix sum
for i in range(1, n):
    for j in range(m):
        arr[i][j] = arr[i - 1][j] + arr[i][j]

q = int(input())
while q > 0:
    i1, j1, i2, j2 = map(int, input().split())
    sum = arr[i2][j2]
    if i1 - 1 >= 0:  # area1 is present
        sum -= arr[i1 - 1][j2]
    if j1 - 1 >= 0:  # area2 is there
        sum -= arr[i2][j1 - 1]
    if i1 - 1 >= 0 and j1 - 1 >= 0:  # commonarea subtractedtwice,soadd
        sum += arr[i1 - 1][j1 - 1]
    print(sum)
    q -= 1

# O(Q.(mxn)) solution. will timeout.
# q=int(input())
# for i in range(q):
#     i1,j1,i2,j2=map(int,input().split())
#     sum=0
#     for i in range(i1,i2+1):
#         for j in range(j1,j2+1):
#             sum+=arr[i][j]
#     print(sum)

"""

"""