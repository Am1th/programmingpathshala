m, n = map(int, input().split())
matrix = []
for _ in range(m):  # i used n and TCs failed
    row = list(map(int, input().split()))
    matrix.append(row)

res = []
left, right = 0, len(matrix[0])
top, bottom = 0, len(matrix)
while left < right and top < bottom:
    # get every i in the top row
    for i in range(left, right):
        res.append(matrix[top][i])
    top += 1

    # get every i in the right col
    for i in range(top, bottom):
        res.append(matrix[i][right - 1])
    right -= 1

    if not (left < right and top < bottom):
        break

    # get every i in the bottom row
    for i in range(right - 1, left - 1, -1):
        res.append(matrix[bottom - 1][i])
    bottom -= 1

    # get every i in the left col
    for i in range(bottom - 1, top - 1, -1):
        res.append(matrix[i][left])
    left += 1
print(*res)

"""
Why below line is required?if not (left < right and top < bottom):
    break

Here are concrete examples showing what happens with and without the guard line for different edge cases.

1. Single row (m = 1)
Matrix:

text
[1, 2, 3, 4]
• With guard:

text
[1, 2, 3, 4]
• Without guard (no if not (left < right and top < bottom): break):

text
[1, 2, 3, 4, 3, 2, 1]
Duplicate elements 3, 2, 1 appear because after taking the top row, the algorithm still tries to take a “bottom row” and “left column” even though there is no remaining height.

2. Single column (n = 1)
Matrix:

text
[1]
[2]
[3]
[4]
• With guard:

text
[1, 2, 3, 4]
• Without guard:

text
[1, 2, 3, 4, 3, 2]
The bottom part gets traversed again upward (3, 2) because after shrinking top and right, there is no valid width, but the bottom and left traversals still run.

3. Odd square (e.g., 3×3)
Matrix:

text
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
• With guard:

text
[1, 2, 3, 6, 9, 8, 7, 4, 5]
• Without guard:

text
[1, 2, 3, 6, 9, 8, 7, 4, 5]
For this case, both versions coincidentally give the same correct result because the inner layer is exactly one cell, and the conditions happen to line up so that no extra bottom/left traversal runs.
This shows the guard is mainly critical when the remaining submatrix degenerates into a single row or a single column during an iteration.

4. Rectangular, more columns than rows (e.g., 3×4)
Matrix:

text
[ 1,  2,  3,  4]
[ 5,  6,  7,  8]
[ 9, 10, 11, 12]
• With guard:

text
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
• Without guard:

text
[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7, 6]
Extra trailing 6 appears because after shrinking top and right, there is no valid rectangle left, but the code still executes the bottom-row traversal and revisits that cell.

Takeaway
The guard:

python
if not (left < right and top < bottom):
    break
is what prevents:
• Re-traversing when the remaining space collapses to zero height or zero width in the middle of an iteration.
• Duplicates like the ones shown above for single-row, single-column, and some rectangular matrices.






i understood the imp of line, but why is it being written only after first two loops?

can we write each seperately after first for loop and second for loop instead of one single line after two for loops?


Yes, you can write separate checks after each loop, but the single check after both is more efficient and follows the standard pattern. Here's why it's placed there specifically.
Why after the first TWO loops only?

text
while left < right and top < bottom:          # 1. Check before STARTING
    # 1. Top row ✓ (always safe)
    top += 1
    
    # 2. Right col ✓ (always safe if top row ran)
    right -= 1
    
    # 3. ? Bottom row  ← DANGER ZONE after top+right shrink
    # 4. ? Left col    ← DANGER ZONE after top+right shrink
After top += 1 and right -= 1, the remaining space might have zero height (top >= bottom) or zero width (left >= right). You only need one check to protect both the bottom row AND left column traversals.
Alternative: Separate checks (works but less efficient)

python
while left < right and top < bottom:
    # Top row
    for i in range(left, right): res.append(mat[top][i])
    top += 1
    
    if top >= bottom: break  # ← Check 1: after top row
    
    # Right col  
    for i in range(top, bottom): res.append(mat[i][right-1])
    right -= 1
    
    if left >= right: break  # ← Check 2: after right col
    
    # Bottom row (now safe)
    # Left col (now safe)
This works correctly but:
• Does 2 redundant checks instead of 1 decisive check
• top >= bottom already implies no bottom row needed
• left >= right already implies no left column needed
• Checking both conditions separately is wasteful since either one is enough to stop
Visual proof with single row example

text
Single row: [1,2,3,4]    top=0, bottom=1, left=0, right=4
1. Top row: [1,2,3,4] ✓  → top=1
2. Right col: range(1,1) → empty ✓ → right=3  
   ↓ NOW: top=1==bottom=1 AND left=0<right=3
3. Single check: top==bottom → BREAK ✓ (protects bottom+left)
If you checked only after top row: top=1==bottom=1 → break (misses right col, empty anyway)
If you checked only after right col: right col is safe anyway.
Standard pattern (most efficient)

python
# Process first 2 directions (always safe)
top_row(); top++
right_col(); right--
# Single check protects last 2 directions
if invalid_bounds(): break
bottom_row()
left_col()

One check after two loops = optimal. Separate checks = correct but verbose/redundant.
"""