# cook your dish here
m, n, k = map(int, input().split())

matrix = []
for _ in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)

# taking input alternate way
# matrix=[list(map(int,input().split())) for _ in range(m)]


# precomputation logic:  Do rowwise psum and colwise psum to find psum for 2d array. wkt in 2d array psum means we consider every position as br and (0,0) as tl ie arr[i][j] means we consider that i,j as br and (0,0) as tl and sum from (0,0) to (i,j) is stored in arr[i][j]
# row wise psum
for i in range(m):
    for j in range(1, n):
        matrix[i][j] = matrix[i][j - 1] + matrix[i][j]

# col wise psum
for i in range(1, m):
    for j in range(n):
        matrix[i][j] = matrix[i - 1][j] + matrix[i][j]

# tl coords are i-k,j-k (starting point)
# br coords are i+k,j+k (ending point)

answer = []
for i in range(m):
    row = []
    for j in range(n):
        i1 = max(i - k, 0)  # tl coords, start point
        j1 = max(j - k, 0)
        # i1,j1=i-k,j-k# alternate
        # if i1<0:i1=0
        # if j1<0:j1=0
        # i2,j2=(i+k)%m,(j+k)%m  this is wrong
        i2 = min(i + k, m - 1)  # br coords ,end point
        j2 = min(j + k, n - 1)
        # i2,j2=i+k,j+k#alternate
        # if i2>=m:i2=m-1
        # if j2>=n:j2=n-1

        ans = matrix[i2][j2]
        if i1 - 1 >= 0:  # area1 is present
            ans -= matrix[i1 - 1][j2]
        if j1 - 1 >= 0:
            ans -= matrix[i2][j1 - 1]  # area2 is present
        if i1 - 1 >= 0 and j1 - 1 >= 0:  # commonarea subtractedtwice,soadd
            ans += matrix[i1 - 1][j1 - 1]
        row.append(ans)
    answer.append(row)

# instead of appending row each time, create answer as below
# answer=[[0 for _ in range(n)] for _ in range(m)] or ans=[[0]*n for _ in range(m)]
# and use like : answer[i][j]=matrix[i2][j2] ... also alterate code pasted below

for row in answer:
    for ele in row:
        print(ele, end=" ")
    print()

# for row in answer:
#     print(" ".join(map(str, row)))

# for i in range(m):
#     for j in range(n):
#         print(answer[i][j], end=' ')
#     print()

# for row in ans:
#     print(*row)

# code from comments
"""
def calculate_prefix_sum(matrix, n, m):
    prefix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            prefix[i][j] = matrix[i][j]
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]
    return prefix

def get_sum(prefix, r1, c1, r2, c2):
    total = prefix[r2][c2]
    if r1 > 0:
        total -= prefix[r1 - 1][c2]
    if c1 > 0:
        total -= prefix[r2][c1 - 1]
    if r1 > 0 and c1 > 0:
        total += prefix[r1 - 1][c1 - 1]
    return total

def matrix_block_sum(matrix, n, m, k):
    prefix = calculate_prefix_sum(matrix, n, m)
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            r1 = max(0, i - k)
            c1 = max(0, j - k)
            r2 = min(n - 1, i + k)
            c2 = min(m - 1, j + k)
            result[i][j] = get_sum(prefix, r1, c1, r2, c2)
    return result

# Input reading
dim = list(map(int, input().split()))
n, m, k = dim[0], dim[1], dim[2]
matrix = [list(map(int, input().split())) for _ in range(n)]

answer = matrix_block_sum(matrix, n, m, k)

for row in answer:
    print(" ".join(map(str, row)))

"""




"""
below code did while practicing , very clean code

m,n,k = map(int,input().split())

matrix=[]     #one liner would be : matrix=[list(map(int,input().split())) for _ in range(m)]
for _ in range(m):
    row=list(map(int,input().split()))
    matrix.append(row)

for i in range(m):
    for j in range(1,n):
        matrix[i][j]=matrix[i][j-1]+matrix[i][j]
        
for i in range(1,m):
    for j in range(n):
        matrix[i][j]=matrix[i-1][j]+matrix[i][j]


ans=[[0]*n for _ in range(m)]


def getSum(i1,j1,i2,j2):
    res=matrix[i2][j2]
    if i1-1>=0:
        res-=matrix[i1-1][j2]
    if j1-1>=0:
        res-=matrix[i2][j1-1]
    if i1-1>=0 and j1-1>=0:
        res+=matrix[i1-1][j1-1]
    return res

for i in range(m):
    for j in range(n):
        i1,j1=max(0,i-k),max(0,j-k)
        i2,j2=min(m-1,i+k),min(n-1,j+k)
        ans[i][j]=getSum(i1,j1,i2,j2)

for row in ans:
    print(*row)
        


"""



# from chatgpt regarding scope

"""
i understand the below code 100% , but whenever it comes to things like scope, gloabal , local,functional and when it comes to passing as value vs passing as reference, i get a lot scared and confused...so explain these in great detail


below is the code for one problem :

def calculate_prefix_sum(matrix, n, m):
    prefix = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            prefix[i][j] = matrix[i][j]
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]
    return prefix

def get_sum(prefix, r1, c1, r2, c2):
    total = prefix[r2][c2]
    if r1 > 0:
        total -= prefix[r1 - 1][c2]
    if c1 > 0:
        total -= prefix[r2][c1 - 1]
    if r1 > 0 and c1 > 0:
        total += prefix[r1 - 1][c1 - 1]
    return total

def matrix_block_sum(matrix, n, m, k):
    prefix = calculate_prefix_sum(matrix, n, m)
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            r1 = max(0, i - k)
            c1 = max(0, j - k)
            r2 = min(n - 1, i + k)
            c2 = min(m - 1, j + k)
            result[i][j] = get_sum(prefix, r1, c1, r2, c2)
    return result

# Input reading
dim = list(map(int, input().split()))
n, m, k = dim[0], dim[1], dim[2]
matrix = [list(map(int, input().split())) for _ in range(n)]
ChatGPT said:

I can definitely help clarify these concepts for you! Let’s break down the things you’re asking about—scope, global vs local variables, passing by value vs reference—in the context of the code you've shared.

1. Scope

Scope refers to the region of the program where a variable is accessible. In Python, the scope is determined by where the variable is defined.

Local Scope: A variable that is defined inside a function is local to that function. It can only be accessed within that function.

Global Scope: A variable defined outside of any function (at the top level) is global. It can be accessed by any function in the program, unless it is shadowed by a local variable with the same name.

In your code:

matrix, n, m, k, and dim are variables that are defined in the global scope because they are outside of any function.

prefix, result, r1, c1, r2, c2, and total are variables that are defined within specific functions (calculate_prefix_sum, get_sum, and matrix_block_sum), so they are local variables within their respective functions.

2. Global vs Local Variables

A global variable is a variable that is declared outside of all functions, and is accessible by all functions. Local variables are confined to the function they are defined in.

For example:

x = 10  # Global variable

def some_function():
    print(x)  # Accessing global variable


If you declare a variable inside a function, it is local to that function.

def some_function():
    y = 5  # Local variable
    print(y)


In your code, matrix, n, m, and k are global variables because they’re defined outside the functions and are accessible in any function. For example, the function matrix_block_sum uses them when calling calculate_prefix_sum.

3. Passing by Value vs Passing by Reference

This concept is a bit tricky but super important in programming.

Passing by Value:

In Python, primitive data types (like int, float, str) are passed by value. This means when you pass a variable to a function, the function gets a copy of the variable, not the actual variable itself. Any changes made to the variable inside the function won’t affect the original variable.

For example:

def modify_value(x):
    x = 20  # Modifies only the local copy

a = 10
modify_value(a)
print(a)  # Output will still be 10


Here, a remains 10 because modify_value worked on a copy of a.

Passing by Reference:

On the other hand, objects (like lists, dictionaries, and other mutable types) are passed by reference. This means when you pass an object to a function, the function works directly on the original object, not a copy.

For example:

def modify_list(my_list):
    my_list.append(5)  # This modifies the original list

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output will be [1, 2, 3, 5]


In your code:

When you pass matrix (which is a list of lists) to calculate_prefix_sum, you’re passing the reference to the original matrix.

Similarly, the prefix matrix that is generated and used within calculate_prefix_sum and get_sum is a mutable object (a list of lists), so if you modify it inside a function, it affects the original list, since they refer to the same object in memory.

Important Note on Python’s "Pass by Object Reference":

Technically, Python passes all variables by object reference, but it behaves like passing by value for immutable objects (like integers, floats, strings) and like passing by reference for mutable objects (like lists, dictionaries).

Applying This to Your Code

Let’s walk through a few key parts of your code and highlight where these concepts come into play.

def calculate_prefix_sum(matrix, n, m):
    prefix = [[0] * m for _ in range(n)]  # Local variable 'prefix' inside this function
    for i in range(n):
        for j in range(m):
            prefix[i][j] = matrix[i][j]  # Modifies the 'prefix' matrix, but 'matrix' remains unchanged


matrix is passed by reference because it is a list of lists. If you modify matrix inside this function, it would change the original matrix object. But in this function, you're not modifying the original matrix; instead, you're copying its values to the local prefix matrix.

    prefix[i][j] += prefix[i - 1][j]


Here, you’re modifying prefix, which is a local variable inside the function. Since prefix is a mutable list, you can modify its elements without affecting the matrix variable that was passed to the function.

def matrix_block_sum(matrix, n, m, k):
    prefix = calculate_prefix_sum(matrix, n, m)  # Here, 'prefix' is returned, and it is assigned to a new variable
    result = [[0] * m for _ in range(n)]  # Local variable 'result' is created


prefix in matrix_block_sum is the result of calling calculate_prefix_sum(matrix, n, m). So, prefix is essentially a new list that was created inside calculate_prefix_sum. Any changes to prefix in matrix_block_sum will not affect the original matrix.

Key Takeaways:

Local vs Global Scope: Variables inside a function are local to that function. Variables outside functions are global.

Passing by Value vs Reference: Immutable types (like integers) are passed by value (copies are made), while mutable types (like lists) are passed by reference (functions modify the original object).

Function Parameters: When you pass mutable objects like lists or dictionaries to a function, you’re passing a reference, which means changes to them inside the function will affect the original object. For immutable objects (like numbers), changes inside a function do not affect the original object.

I hope this clears up the concepts for you! Let me know if you have any more specific questions or need more examples!

You said:
what happens when local variable of  one function is passed to other function as parameter?



also i think your reg pass by value etc is not accurate...
in python everything is an object and everything is pass by reference...
when you pass an object that is immutable, functions gets a  copy of that 
if the object is mutable, function gets the original object as it is....

there is no concept of pass by value and pass by reference in python unlike languages like C. everything is pass by reference in python.



however in java , primitives are pass by value and objects are pass by reference if i am correct...
ChatGPT said:

You're absolutely on the right track, and it’s great that you're thinking critically about this — you’ve already cleared up a major misunderstanding that many people have.

Let’s unpack your questions and points carefully.

✅ Question 1:
What happens when a local variable of one function is passed to another function as a parameter?

When a local variable is passed as a parameter to another function in Python, the value (or reference) of that variable is passed, but not its scope.

In other words:

The called function gets access to the object that the local variable refers to.

The original variable name (from the calling function) is not known in the called function.

The two functions have separate namespaces, and they just share a reference to the same object (if mutable), or a copy of the object (if immutable).

Example:
def f1():
    x = [1, 2, 3]  # local to f1
    f2(x)          # pass local variable to f2

def f2(y):         # 'y' is a new local variable, pointing to same object as 'x'
    y.append(4)    # modifies the original list

f1()


x is local to f1, and y is local to f2.

But both refer to the same list object in memory.

Modifying the list in f2 affects it in f1 as well because lists are mutable.

✅ Question 2:
Clarifying Python’s “pass by value vs pass by reference”

You’re mostly correct in your understanding, but let’s tighten the language a bit for clarity.

🔍 What actually happens in Python?

Python uses "call by object reference" (also called "call by sharing").

When you pass a variable to a function, you’re passing the reference to the object, not the actual variable name.

But whether that object is mutable or immutable determines what happens inside the function.

So, is Python “pass by reference”?

Not quite in the traditional sense.

✅ Correct phrasing:

Python passes everything by object reference.
But since objects can be mutable or immutable, the effects can look like either “pass by value” (for immutables) or “pass by reference” (for mutables).

Example 1 – Immutable:
def modify(n):
    n += 1
    print("Inside modify:", n)

x = 10
modify(x)
print("Outside modify:", x)


Output:

Inside modify: 11
Outside modify: 10


x is an integer (immutable).

modify receives a reference to the object 10, but when you do n += 1, it creates a new int object (11) and binds n to it.

x remains untouched outside the function.

Example 2 – Mutable:
def modify(lst):
    lst.append(4)
    print("Inside modify:", lst)

x = [1, 2, 3]
modify(x)
print("Outside modify:", x)


Output:

Inside modify: [1, 2, 3, 4]
Outside modify: [1, 2, 3, 4]


lst and x both refer to the same list object.

Modifications are seen outside the function because the object is mutable.

✅ Java Comparison

Yes, you're mostly correct here too.

In Java:

Primitives (like int, float, char) are passed by value — the function gets a copy of the value.

Objects are also passed by value, but the value is a reference to the object.

This causes confusion.

Key point:

Java is pass-by-value for everything.
But when you pass an object, you're passing a value that is a reference.

So you're passing the reference by value, not passing by reference.

Example:
void changeValue(int x) {
    x = 10;
}

int a = 5;
changeValue(a);
// a is still 5

void modifyList(List<Integer> list) {
    list.add(4);
}

List<Integer> myList = new ArrayList<>();
modifyList(myList);
// myList now has 4


You can change the object, but you can’t reassign the reference inside the function and have it affect the original.

🧠 Summary (Python vs Java):
Language	Primitives	Objects	Summary
Python	Immutable objects	Mutable objects	Everything passed by object reference (call-by-sharing)
Java	Pass by value	Pass by value (of reference)	You can modify object, but not reference itself
Final Thought

So your instinct is absolutely right:

✅ In Python, everything is an object, and everything is passed by object reference.
But understanding mutability is the key to understanding the behavior.

Let me know if you want to explore mutability further or want real visual memory diagrams to cement this understanding!

You said:
You can modify object, but not reference itself..?
elaborate with examples
ChatGPT said:

Great question. This is one of the most commonly misunderstood points in programming, especially when comparing Python and Java (or other statically typed languages). Let’s dive into:

🔍 The Meaning of:
“You can modify the object, but not the reference itself”

This means:

Inside a function, you can change the contents of the object the reference points to (if the object is mutable).

But you cannot change what the caller's variable points to — i.e., you cannot reassign the caller’s reference from inside the function.

🔸Python Example
✅ Modifying the object:
def modify_list(lst):
    lst.append(100)  # Modifies the list object

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # ✅ [1, 2, 3, 100]

❌ Reassigning the reference (doesn’t affect original):
def reassign_list(lst):
    lst = [9, 9, 9]   # This creates a new list and rebinds 'lst' locally

my_list = [1, 2, 3]
reassign_list(my_list)
print(my_list)  # ❌ Still [1, 2, 3], not [9, 9, 9]


In reassign_list(), lst = [9, 9, 9] creates a new list and makes lst point to it.

But this does not change what my_list in the caller points to.

So the reassignment has no effect outside the function.

🔸Java Example

Java behaves similarly — references are passed by value. You get a copy of the reference, not the reference itself.

✅ Modifying the object:
void modifyList(List<Integer> list) {
    list.add(100);  // Modify the object
}

List<Integer> myList = new ArrayList<>();
myList.add(1);
myList.add(2);
modifyList(myList);
System.out.println(myList);  // ✅ [1, 2, 100]

❌ Reassigning the reference (doesn’t affect caller):
void reassignList(List<Integer> list) {
    list = new ArrayList<>();  // New object
    list.add(9);
    list.add(9);
    list.add(9);
}

List<Integer> myList = new ArrayList<>();
myList.add(1);
myList.add(2);
reassignList(myList);
System.out.println(myList);  // ❌ Still [1, 2], not [9, 9, 9]


Inside reassignList, the parameter list is a copy of the reference to myList.

When you do list = new ArrayList<>(), you just change the local reference, not the original.

The original reference myList in the caller is unaffected.

🧠 Analogy (to drive it home):

Imagine your friend gives you the address of their house.

You can go inside the house and rearrange furniture (modify the object).

But you can’t make your friend’s pointer change to a different house — if you write a new address on your copy, your friend still points to the original house.

🔄 Summary Table
Operation	Python	Java
Modifying object content	✅ Works (if mutable)	✅ Works
Reassigning reference	❌ No effect on caller	❌ No effect on caller
✅ Final Note:

So when we say:

“You can modify the object, but not the reference itself,”

We're saying:

Inside a function, you can change the contents of what the reference points to, but you cannot make the caller's variable point to a new object.

Let me know if you'd like a diagram to visualize this — or if you'd like to test it live in code!

You said:
yes !
also this line: But you cannot change what the caller's variable points to — i.e., you cannot reassign the caller’s reference from inside the function.
why is this the case?



ChatGPT said:

Excellent — this is a deep and subtle question, and understanding why this behavior exists will really solidify your grasp of how variables and function calls work in Python (and similar languages like Java).

Let’s explore why you cannot change what the caller’s variable points to (i.e., you can’t reassign the caller’s reference inside the function).

🔁 First, Let’s Break It Down:

When you call a function in Python, here’s what happens under the hood:

📦 Step-by-step process:

Python evaluates the arguments and passes them to the function by object reference.

Inside the function, the parameters become new local variable names that refer to the same objects.

Any reassignment of the parameter inside the function only changes the local reference, not the original reference in the calling scope.

🔥 Because the function only receives a copy of the reference, it can’t reassign the original variable — it doesn’t have access to it.

📌 Analogy:

Think of the caller’s variable as a label on a box.

When you pass the variable into a function, Python gives the function a copy of the label, not the box.

You can take things in and out of the box, but if you put the label on a different box, it doesn’t change the original label outside the function — that one still points to the old box.

🧪 Code Example (Python)
def try_to_reassign(a):
    print("Before reassignment inside function:", a)
    a = [9, 9, 9]  # This only changes local 'a'
    print("After reassignment inside function:", a)

x = [1, 2, 3]
try_to_reassign(x)
print("Outside function:", x)


Output:

Before reassignment inside function: [1, 2, 3]
After reassignment inside function: [9, 9, 9]
Outside function: [1, 2, 3]


Why did x not change?

Because:

a = [9, 9, 9] inside the function created a new list, and rebound the local variable a to that new list.

The original variable x outside the function still points to the old list.

The function never had access to the variable name x — only to the object that x was pointing to.

🔧 Java Analogy
void reassignArray(int[] arr) {
    arr = new int[]{9, 9, 9}; // New array assigned to local 'arr'
}

int[] myArray = {1, 2, 3};
reassignArray(myArray);
System.out.println(Arrays.toString(myArray));  // Still [1, 2, 3]


Same story. The local reference is reassigned, but the caller’s reference isn’t changed.

📚 Why is it Designed This Way?
✅ 1. Namespace Isolation

Functions are designed to have their own local scope to avoid accidental interference with the caller's variables.

This keeps code modular and predictable.

✅ 2. Avoiding Side Effects

If you could rebind the caller's variables from inside a function, it would be much harder to reason about code.

Unexpected side effects would be common, breaking encapsulation and clarity.

✅ 3. Consistency with Value Semantics

Python chooses object reference semantics consistently, regardless of whether you’re dealing with primitives or complex types.

But since names are just labels, reassigning them in local scope doesn’t affect other scopes.

🧠 Final Summary
🔑 Why can't you reassign the caller's reference inside a function?

Because:

The function receives a copy of the reference (not the variable itself).

The parameter is a local name inside the function.

Reassigning the local name doesn’t change what the caller’s variable points to — just like renaming your own label doesn’t change someone else’s label for the same box.

Let me know if you’d like a visual diagram to make this more intuitive — or if you want to try code experiments together!

You said:
so like java , in python also is reference value copied into parameters? just now we discussed it is pass by ref in python and pass by val in java(where value of ref is passed)



this line is awesome to remember:
The function never had access to the variable name x — only to the object that x was pointing to.
ChatGPT said:

Yes — your instinct is absolutely right, and you're now deep in the heart of the real truth behind Python and Java function behavior. Let’s clarify this finally and precisely:

✅ The Golden Rule:

Both Python and Java pass arguments by value of the reference.
That is, the reference (pointer to the object) is copied, not the object itself.
So:
✅ You can modify the object via the reference.
❌ But you can’t reassign the caller’s variable.

⚙️ So yes — to your question:

"So like Java, in Python also is reference value copied into parameters?"

✅ Yes. 100%.

In both languages, the reference itself is passed by value.

That’s why the function cannot reassign the caller’s variable, but can mutate the object (if it’s mutable).

🔍 Let’s Compare:
Concept	Java	Python
What is passed	Copy of reference (pointer)	Copy of reference (pointer)
Can mutate object?	✅ Yes (if mutable)	✅ Yes (if mutable)
Can reassign caller's variable?	❌ No	❌ No
Is it pass-by-reference?	❌ Not technically	❌ Not technically
Is it pass-by-value?	✅ Yes (value = reference)	✅ Yes (value = reference)
✅ So what's the right terminology for Python?

"Pass-by-object-reference" (also called "call-by-sharing")

The reference (to the object) is copied into the function parameter.

This is not traditional pass-by-reference (like in C++ with &), where the actual variable is passed and can be reassigned.

This is also not traditional pass-by-value, where a copy of the object is passed.

🧠 Remember This:

❝ The function never had access to the variable name x — only to the object that x was pointing to. ❞

That quote really is a perfect mental model. Hold onto it.

💬 Want a visual?

Imagine you have this variable assignment:

x = [1, 2, 3]

When you call:
def modify(a):
    a.append(4)    # modifies object
    a = [9, 9, 9]  # reassigns local 'a'

modify(x)


Here's what happens:

x points to:

[1, 2, 3]


a is assigned the same reference (a copy of the reference) — so it also points to [1, 2, 3].

a.append(4) modifies the shared object → [1, 2, 3, 4]

a = [9, 9, 9] creates a new list, and makes a point elsewhere.

x still points to [1, 2, 3, 4].

✅ TL;DR Final Summary:

Python is not pass-by-reference.

Python is not pass-by-value in the traditional sense.

Python passes a copy of the reference — just like Java.

This is known as pass-by-object-reference or call-by-sharing.

And yes — that line:

“The function never had access to the variable name x — only to the object that x was pointing to.”

is 🔥 and nails the concept perfectly.


"""