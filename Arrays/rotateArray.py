n, k = map(int, input().split())
arr = list(map(int, input().split()))


# meth1, using k%n and reducing number of rotations
# t=k%n
# while(t>0):
#     x=arr[-1]
#     for i in range(n-2,-1,-1):
#         arr[i+1]=arr[i]
#     arr[0]=x
#     t=t-1
# print(*arr) #list unpacking

# meth2, using slicing
# above is timeout for 1 testcase, so used slicing
# k=k%n
# arr=arr[-k:]+arr[:-k]
# print(*arr)

# meth3, using temp array
# temp=[0]*n
# for i in range(n):
#     temp[(i+k)%n]=arr[i]
# print(*temp)


# meth4 , linking reversal of array with rotation of array

# def reverseArray(arr, s, e):
#     arr[s:e+1] = [arr[i] for i in range(e, s-1, -1)]
def reverseArray(arr, s, e):
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s = s + 1
        e = e - 1


k = k % n
reverseArray(arr, 0, n - k - 1)  # -1 to exclude end index
reverseArray(arr, n - k, n - 1)
reverseArray(arr, 0, n - 1)
print(*arr)




"""
tarun logic
def reverseArr(arr,i,j):
    
    while(i<=j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    
k = k % n
reverseArr(arr,0,n-1)
# print("aa",*arr)
reverseArr(arr,0,k-1)
# print("aaa",*arr)
reverseArr(arr,k,n-1)
# print("aaaa",*arr)
print(*arr)
"""



"""
for easy understanding
For right-rotation by k:
The last k elements should move to the front.
The first n - k elements should move to the back.

Part	     Start	  End  	     Notes
First part	  0	     n-k-1	 First n-k elements
Second part	  n-k	  n-1	 Last k elements
Whole array	   0	  n-1	 For final reversal

If confused , see below:
print("First:", arr[0:n-k])
print("Second:", arr[n-k:n])


also learned in sliding window that 
The last subarray of size k , starts at index n-k
"""




"""
Core difference (one line summary)
Line	What happens
arr = arr[-k:] + arr[:-k]	Rebinds the name arr to a NEW list object
arr[:] = arr[-k:] + arr[:-k]	Modifies the EXISTING list object in-place



1️⃣ arr = arr[-k:] + arr[:-k]
What happens internally

arr[-k:] → creates a new list

arr[:-k] → creates a new list

+ → creates another new list (concatenation)

arr = ... → arr now points to this new list

📌 The original list object is untouched
📌 Only the variable name arr is updated

Memory picture

Before:

arr ──► [1,2,3,4,5,6,7]


After:

arr ──► [5,6,7,1,2,3,4]   (NEW object)
(old list still exists if referenced elsewhere)

⚠️ Important consequence

If another variable was pointing to the same list:

b = arr
arr = arr[-k:] + arr[:-k]


Then:

b  # ❌ still old list


Because arr was rebound, not mutated.

2️⃣ arr[:] = arr[-k:] + arr[:-k]
What happens internally

RHS creates a new list (same as above)

arr[:] = ... means:

Replace all elements of the existing list with new elements

📌 The list object remains the SAME
📌 Only its contents change

Memory picture

Before:

arr ──► [1,2,3,4,5,6,7]


After:

arr ──► [5,6,7,1,2,3,4]   (SAME object, modified)

🔥 Why [:] matters

[:] means full slice assignment:

arr[start:end] = iterable


So:

arr[:] = new_list


is equivalent to:

arr.clear()
arr.extend(new_list)

🚨 Consequence with multiple references
b = arr
arr[:] = arr[-k:] + arr[:-k]


Now:

b  # ✅ updated list


Because same object was modified.

3️⃣ When does the difference actually matter?
❌ No difference when:

arr is local

No other reference exists

Competitive programming

✅ Difference matters when:

arr is passed to a function

Shared references exist

Mutable objects are expected to update

Libraries / frameworks / APIs

4️⃣ Example that proves the difference
def rotate(arr, k):
    arr = arr[-k:] + arr[:-k]

a = [1,2,3,4]
rotate(a, 2)
print(a)   # ❌ unchanged


Now:
def rotate(arr, k):
    arr[:] = arr[-k:] + arr[:-k]

a = [1,2,3,4]
rotate(a, 2)
print(a)   # ✅ rotated

"""