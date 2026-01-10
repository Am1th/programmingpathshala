n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
# matrix=[list(map(int,input().split())) for _ in range(n)] tried while practicing
for i in range(0, n):
    for j in range(i, n):  # for upper triangle j>=i
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    row.reverse()

# alternate ways to reverse
# for i in range(n):
#     for j in range(n//2):
#         matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]

# for row in matrix:
#     row[:]=row[::-1]
#     row = row[::-1] this is wrong,This creates a new list object and assigns it to the local variable row

# for row in matrix:
#     left,right=0,len(row)-1
#     while left<right:
#         row[left],row[right]=row[right],row[left]
#         left+=1
#         right-=1


# def rev(row,s,e):   #did while practicing
#     while s<e:
#         row[s],row[e]=row[e],row[s]
#         s+=1
#         e-=1
# for row in matrix:
#     rev(row,0,len(row)-1)


for row in matrix:
    print(" ".join(map(str, row))) #print(*row) this is best, tried while practicing

# l,r=0,len(matrix)-1
# while l<r:
#     for i in range(r-l):
#         top,bottom=l,r
#         topLeft=matrix[top][l+i]

#         matrix[top][l+i]=matrix[bottom-i][l]

#         matrix[bottom-i][l]=matrix[bottom][r-i]

#         matrix[bottom][r-i]=matrix[top+i][r]

#         matrix[top+i][r]=topLeft
#     r-=1
#     l+=1

# for row in matrix:
#     # print(ele for ele in row)#It won’t print actual elements — it just prints a generator object:  <generator object <genexpr> at 0x000...>
#     # print([ele for ele in row])#printing 1D lists
#     # print(list(ele for ele in row))#same as above
#     print(" ".join(map(str,row)))

# alternate to above
# for row in matrix:
#     for ele in row:
#         print(ele,end=" ")
#     print()


# for row in arr:
#     print(" ".join(list(map(int,row))))#must be string
#     print(" ".join(list(map(str,row))))#valid but not required.
#     print(" ".join(map(str,row)))#correct


# #join() is used to concatenate elements of an iterable/list into a string, but the elements should be strings, not integers. So, when you try to join map(int, row), it throws an error because you're trying to join integers, not strings.


# list('123')  # Would give you ['1', '2', '3'], not ['123'] .  When you pass a string to the list() constructor, it iterates over the string, converting each character into an individual element of a list.
# The list() function expects an iterable (like a string, tuple, or another list) as its argument.
#few examples to understand.
# list('abc')	['a', 'b', 'c']	Each character becomes an element
# list('hello')	['h', 'e', 'l', 'l', 'o']	Character by character
# list([1, 2, 3])	[1, 2, 3]	Already a list → remains unchanged

# ✅ How to get ['123'] as the output
# list(['123'])


#points regarding shallow copy , can read in chatgpt