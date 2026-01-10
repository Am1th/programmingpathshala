n, m = map(int, input().split())
arr = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

ans = 0
mod = 10 ** 9 + 7
# considering each and every ele in array and its contribution
for i in range(n):
    for j in range(m):
        contribution = ((i + 1) * (j + 1)) % mod * ((n - i) * (m - j)) % mod * arr[i][j] % mod
        ans = (ans % mod + contribution % mod) % mod
print(ans)

# n^6 solution.
# considering every element in matrix as TL and varying BR such that i2>=i1 and j2>=j1 and finding sum of every submatrix

# ans=0
# mod=10**9+7

# # no need to create psum array, modify original array. if you want to copy contents of array to psum array, u can do like : psum = [row[:] for row in arr]
# # psum=[]
# # for _ in range(n):
# #     row=[0]*m
# #     psum.append(row)
# # # psum = [[0] * m for _ in range(n)]

# #psum computation
# #row wise prefix sum
# for i in range(n):
#     for j in range(1,m):
#         arr[i][j]=arr[i][j-1]+arr[i][j]
# #column wise prefix sum
# for i in range(1,n):
#     for j in range(m):
#         arr[i][j]=arr[i-1][j]+arr[i][j]


# def getSum(i1,j1,i2,j2):
#     # sum=0
#     # for i in range(i1,i2+1):
#     #     for j in range(j1,j2+1):
#     #         sum+=arr[i][j]
#     # return sum
#     sum=arr[i2][j2]
#     if i1-1>=0:
#         sum-=arr[i1-1][j2]
#     if j1-1>=0:
#         sum-=arr[i2][j1-1]
#     if i1-1>=0 and j1-1>=0:
#         sum+=arr[i1-1][j1-1]
#     return sum


# for i1 in range(n):
#     for j1 in range(m):
#         for i2 in range(i1,n):
#             for j2 in range(j1,m):
#                 # ans+=getSum(i1,j1,i2,j2)
#                 ans=(ans%mod+getSum(i1,j1,i2,j2)%mod)%mod
# print(ans)

