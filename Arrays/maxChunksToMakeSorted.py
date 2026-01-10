n = int(input())
arr = list(map(int, input().split()))

# def canBeChunked(i,j):
#     cnt=0
#     for k in range(i,j+1):
#         if arr[k]>=i and arr[k]<=j:
#             cnt=cnt+1
#     if cnt==j-i+1: return True
#     else: return False

# i=0
# ans=0
# while(i<n):
#     for j in range(i,n):
#         if canBeChunked(i,j):
#             break;
#     i=j+1
#     ans+=1
# print(ans)


# optimized solution
cmax = float('-inf')
ans = 0
for i in range(n):
    cmax = max(cmax, arr[i])
    if cmax == i:
        ans += 1
print(ans)


"""
ex1.
arr = list(map(int, '123'))  # works, map expects iterable and string is iterable
ex2.
arr = list(map(int, 123))    #TypeError: 'int' object is not iterable
ex3.
arr=list(map(int,input()))  if input is 1 2 3, you are passing '1 2 3' ie '1'' ''2'' ''3' ie the string: 1space2space3
ValueError: invalid literal for int() with base 10: ' '
and int(' ') throws the ValueError because ' ' (a space) is not a valid integer.

so correct way is 
arr = list(map(int, input().split())) 
input().split() converts '1 2 3' into ['1', '2', '3'].Then int() converts each element to integer → [1, 2, 3]
 
 
ex4.
arr = list(map(int, input().split())) if input is : 1,2,3
Then input().split() gives: 
['1,2,3'] # ← only one string, because split() by default splits on spaces
Then int('1,2,3') → ❌ ValueError: invalid literal for int() with base 10: '1,2,3'
so correct way is :
arr = list(map(int, input().split(',')))
How it works:
input() → '1,2,3'

.split(',') → ['1', '2', '3']

map(int, ...) → [1, 2, 3]
"""