t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    i=0
    while i<len(arr):
        correctIndex=arr[i]-1
        if arr[i]<=len(arr) and arr[i]>0 and arr[i]!=arr[correctIndex]:   #here don't write arr[i]!=i+1 , debug for [2,2] will lead to infinite loop
            arr[i],arr[correctIndex]=arr[correctIndex],arr[i]
        else:
            i+=1
    flag=False
    for i in range(len(arr)):
        if arr[i]!=i+1:
            flag=True
            print(i+1)
            break
    if not flag:
        print(len(arr)+1)



#same as above , did while practicing
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        correctIndex = arr[i] - 1
        while 0 < arr[i] <= n and arr[i] != arr[correctIndex]:
            arr[i], arr[correctIndex] = arr[correctIndex], arr[i]
            correctIndex = arr[i] - 1

    ans = n + 1
    for i in range(n):
        if arr[i] != i + 1:
            ans = i + 1
            break
    print(ans)


# i noticed in for loop
"""
so the i inside for loop indeed referes to the same i that for loop is referring , 
but the value of i is discarded when it gets to for loop and the counting continues as it is in which for loop is counting..

for i in range(5):
    print(f"Before: i = {i}")
    i += 10               #wkt this 'i' value wont change for loop
    print(f"After : i = {i}")  

"""



# tarun solution
t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    # Step 1: Replace invalid numbers (<=0 or >n) with a placeholder (n+1)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n: nums[i] = n + 1

    # Step 2: Mark presence of numbers 1..n using index-based marking
    for i in range(n):
        num = abs(nums[i])   # get the original value (since we might flip signs)
        if num>n:continue #skip invalid nos
        if nums[num - 1] > 0: nums[num - 1] = -nums[num - 1]  # if not already marked,flip the sign to mark it. if an index is already marked -ve,skip it
    """
    For each number num from 1 to n, we flip the sign at index num - 1.
    If num = 3, we flip the sign at nums[2] → this marks that 3 exists.
    We use abs(nums[i]) to read the value without being affected by previous sign flips.
    """

    # Step 3: Find the first index with a positive value
    missing = n + 1
    for i in range(n):
        if nums[i] > 0:
            missing = i + 1
            break

    print(missing)




# i wrote based on above solution:
t = int(input())


def fmp(arr, n):
    for i in range(n):
        if arr[i] > n or arr[i] <= 0:
            arr[i] = n + 1

    for i in range(n):
        if abs(arr[i]) > n: continue  # if invalid number, skip it(we already marked invalid numbers >n , zero and -ve nos with n+1
        arr[abs(arr[i]) - 1] = -abs(arr[abs(arr[i]) - 1])  # if arr[abs(arr[i])-1]>0: arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        # if duplicates are there same no can be flipped again
        # flipping twice will make that number positive, so taking abs and then making it -ve forces it to be negative
        # even if it already is -ve. so marking is not lost.
        # see RHS we took abs and flipped ,-abs(...)

        # or if you think: why take an already -ve number , take abs of that, and again mark it -ve, we can simply skip
        # already marked numbers ie -ve numbers , see below
        # if arr[abs(arr[i])-1]>0: arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
        # and this abs(arr[i]) is 'actual number' before some other number flipped it to -ve.
        # can debug with arr = [3, 4, 1, 1] or [3, 4, -1, 1]

    for i in range(n):
        if arr[i] > 0:
            return i + 1
    return n + 1


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    res = fmp(arr, n)
    print(res)

# did while practicing , same as above solutions , but easy to read
"""
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    for i in range(n):
        if arr[i]<=0 or arr[i]>n:
            arr[i]=n+1
        
    for i in range(n):
        num=abs(arr[i])
        if 0<num<=n:
            arr[num-1]=-abs(arr[num-1])
       
    ans=n+1     
    for i in range(n):
        if arr[i]>0:
            ans=i+1
            break
    print(ans)            
"""












# using cycle approach
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    maxm=max(arr)
    for i in range(n):
        if arr[i] <= 0 or arr[i] >= n: #this approach wkt is diff from above, here if ( arr[i] is =n ) we have to attack index n which is not possible.so that's when arr[i]=n also we place zero, see below line.
            arr[i] = 0

    def cycle(i, arr):
        i = arr[i]
        while arr[i] >= 0:
            tmp = arr[i]
            arr[i] = -1
            i = tmp


    for i in range(0, n):
        if arr[i] >= 0:
            cycle(i, arr)

    ans = 1
    for i in range(1, n):
        if arr[i] != -1:
            break
        ans += 1

    if ans == maxm:
        ans += 1

    print(ans)

    # i wrote
    # ans = n
    # for i in range(1, n):
    #     if arr[i] != -1:
    #         ans = i
    #         break
    # if ans == maxm: ans = n + 1
    # print(ans)


"""
Why skip index 0 in the final loop

During the cleaning step:

if arr[i] <= 0 or arr[i] > (n - 1):
    arr[i] = 0


You explicitly set invalid numbers (like negatives and zeros) to 0.

So index 0 can contain anything — maybe 0, maybe replaced later during cycles —
but it doesn’t represent any actual positive number (since there’s no “number 0”).

Therefore, checking arr[0] to decide the smallest positive missing number doesn’t make sense.

That’s why the search starts from i = 1 — the first index that corresponds to a real positive integer (1).
"""

"""
for debugging tarun last code:
Perfect 👏 let’s dry-run your exact code for this input:

Input:
1          ← (only one test case)
3          ← n = 3
2 3 4      ← array elements

🧩 Step 1: Initialization
t = 1
n = 3
arr = [2, 3, 4]

maxi = max(arr) = 4

🧹 Step 2: Cleaning invalid elements

Loop:

for i in range(n):
    if arr[i] <= 0 or arr[i] > (n - 1):
        arr[i] = 0


Here (n - 1) = 2.

Now check each element:

i	arr[i]	Condition (<=0 or >2)	Result
0	2	2 > 2 → ❌ (false)	keep 2
1	3	3 > 2 → ✅ (true)	set arr[1] = 0
2	4	4 > 2 → ✅ (true)	set arr[2] = 0

After loop:

arr = [2, 0, 0]

🧮 Step 3: Define cycle(i, arr) function
def cycle(i, arr):
    i = arr[i]
    while arr[i] >= 0:
        tmp = arr[i]
        arr[i] = -1
        i = tmp

⚙️ Step 4: Run cycle for all positive elements
for i in range(0, n):
    if arr[i] >= 0:
        cycle(i, arr)


We go one by one:

i = 0

arr[0] = 2 → ≥ 0 ✅ → call cycle(0, arr)

Inside cycle:

i = arr[0] = 2


Now i = 2

while arr[i] >= 0: → arr[2] = 0 → condition true
Inside while:

tmp = arr[2] = 0
arr[2] = -1
i = tmp = 0


Now i = 0

Next check:
arr[i] = arr[0] = 2 → still ≥ 0 ✅
Inside while:

tmp = arr[0] = 2
arr[0] = -1
i = tmp = 2


Now i = 2 again.

Check again:
arr[2] = -1 → not ≥ 0 ❌ → exit loop.

After this cycle:

arr = [-1, 0, -1]

i = 1

arr[1] = 0 → ≥ 0 ✅ → call cycle(1, arr)

Inside cycle:

i = arr[1] = 0


Now i = 0

arr[0] = -1 → not ≥ 0 ❌ → loop doesn’t run.
Return immediately.

So after this:

arr = [-1, 0, -1]

i = 2

arr[2] = -1 → skip (not ≥ 0)

✅ End of loop.
"""

"""
i loop like this to detect cycle, vivek sir approach

# for this problem this approach doesnt work. Because loop stops when index that you attack == i ,
but the main thing about this problem is , the number may not be there, that's the whole point of this problem,
to find this missing number. Ex : [2,3,4] try with this
#also other thing ,this approach doensn't care if the index that you are going to attack is already -ve, it just checks ind!=i

def cycle(i, arr):                
    ind = arr[i] 
    while ind != i: 
        tmp = arr[ind] 
        arr[ind] = -1 
        ind = tmp 

for i in range(0, n):
    if arr[i] >= 0:
        cycle(i, arr)
        
        
        
tarun wrote:
def cycle(i, arr): 
    i = arr[i]
    while arr[i] >= 0:
        tmp = arr[i]
        arr[i] = -1
        i = tmp

for i in range(0, n):
    if arr[i] >= 0:
        cycle(i, arr)

"""