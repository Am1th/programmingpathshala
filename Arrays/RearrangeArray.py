# O(n) solution but sc also O(n)
# n=int(input())
# arr=list(map(int,input().split()))
# temp=[0]*n
# for i in range(n):
#     temp[arr[i]]=i
# print(*temp)



# n=int(input())
# arr=list(map(int,input().split()))

# for i in range(n):
#     if arr[i]>=0:
#         ind = arr[i]
#         val=i
#         while ind!=i:
#             temp=arr[ind]
#             arr[ind]=-(val+1)

#             val=ind
#             ind=temp
#         arr[ind]=-(val+1)

# for i in range(n):
#     arr[i]=-1*arr[i]-1

# print(*arr)

# alternate technique
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    old_val = arr[i] % n
    arr[old_val] = n * i + arr[old_val]

for i in range(n):
    arr[i] = arr[i] // n

print(*arr)


# tarun solution.  the index that you attack i am taking as ind, tarun took it as 'i' and stored it in 'i' itself.
#Remember the above point, it is important.

# cook your dish here

# n = int(input())
#
# arr = list(map(int, input().split(" ")))
#
#
# def cycle(i, arr):
#     new = i
#     i = arr[i]
#
#     while (arr[i] >= 0):
#         tmp = arr[i]
#         arr[i] = -(new + 1)
#         new = i
#         i = tmp
#
#
# for i in range(n):
#     if (arr[i] >= 0):
#         cycle(i, arr)
#
# for i in range(n):
#     arr[i] = -(arr[i] + 1)
#
# print(*arr)
