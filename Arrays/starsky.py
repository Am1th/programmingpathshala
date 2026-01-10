n, q, c = map(int, input().split())

brightnessGrid = [[[0] * 101 for _ in range(101)] for _ in range(c + 1)]
for _ in range(n):
    x, y, s = map(int, input().split())

    # For each cycle time t, update the brightness at (x, y)
    for t in range(0, c + 1):
        brightness = (s + t) % (c + 1)
        brightnessGrid[t][x][y] += brightness

psum = [[[0] * 101 for _ in range(101)] for _ in range(c + 1)]
# Precompute 2D prefix sums for each cycle time
for t in range(0, c + 1):
    for i in range(1, 101):  # rowwise psum
        for j in range(1, 101):  # 2,101 will NOT work
            psum[t][i][j] = brightnessGrid[t][i][j] + psum[t][i][j - 1]

    for j in range(1, 101):  # colwise psum
        for i in range(2, 101):  # 1,101 works
            # psum[t][i][j] = brightnessGrid[t][i][j] +psum[t][i-1][j] this would be wrong.Should use result from the row-wise pass.
            psum[t][i][j] = psum[t][i][j] + psum[t][i - 1][j]

for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    t = t % (c + 1)  # effective time
    ans = psum[t][x2][y2] - psum[t][x1 - 1][y2] - psum[t][x2][y1 - 1] + psum[t][x1 - 1][y1 - 1]
    print(ans)

"""
same above code small changes while practicing

n,q,c=map(int,input().split())
 
brightnessGrid=[[[0]*101 for _ in range(101)] for _ in range(c+1)]
for _ in range(n):
    x,y,s=map(int,input().split())
    for t in range(c+1):
        brightness=(s+t)%(c+1)
        brightnessGrid[t][x][y]+=brightness
 
for t in range(c+1):
    for i in range(1,101):
        for j in range(2,101):
            brightnessGrid[t][i][j]=brightnessGrid[t][i][j-1]+brightnessGrid[t][i][j]
            
    for i in range(2,101):
        for j in range(1,101):
            brightnessGrid[t][i][j]=brightnessGrid[t][i-1][j]+brightnessGrid[t][i][j]
            
for _ in range(q):
    t,x1,y1,x2,y2=map(int,input().split())
    t=t%(c+1)
    ans=brightnessGrid[t][x2][y2]-brightnessGrid[t][x1-1][y2]-brightnessGrid[t][x2][y1-1]+brightnessGrid[t][x1-1][y1-1]
    print(ans)


i thought like below but understood it is wrong . Must draw box diag and see
for t in range(c+1):
    for i in range(2,101):         # u are calculating row sum,but skipped 1st row
        for j in range(1,101):
            brightnessGrid[t][i][j]=brightnessGrid[t][i][j-1]+brightnessGrid[t][i][j]
            
    for i in range(1,101):
        for j in range(2,101):    # u are calculating col sum,but skipped 1st col
            brightnessGrid[t][i][j]=brightnessGrid[t][i-1][j]+brightnessGrid[t][i][j]

"""


"""
alternate way to compute prefix sums
--------------------------------------
# Precompute 2D prefix sums
prefix_sum = [[[0] * grid_size for _ in range(grid_size)] for _ in range(cycle)]
for t in range(cycle):
    for i in range(1, grid_size):
        for j in range(1, grid_size):
            prefix_sum[t][i][j] = (
                brightness_grid[t][i][j]
                + prefix_sum[t][i - 1][j]
                + prefix_sum[t][i][j - 1]
                - prefix_sum[t][i - 1][j - 1]
            )
"""



"""
#below is to print output at once.
# Process queries
output = []
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    effective_time = t % cycle
    ans = (
        prefix_sum[effective_time][x2][y2]
        - prefix_sum[effective_time][x1 - 1][y2]
        - prefix_sum[effective_time][x2][y1 - 1]
        + prefix_sum[effective_time][x1 - 1][y1 - 1]
    )
    output.append(str(ans))

# Print all results at once
print("\n".join(output))
"""



"""
not required
#below both are same
#column wise prefix sum
 for i in range(1,n):
     for j in range(m):
         arr[i][j]=arr[i-1][j]+arr[i][j]

#column wise prefix sum
for j in range(m):
     for i in range(1,n):
         arr[i][j]=arr[i-1][j]+arr[i][j]

"""


#if input if fixed, can read like below. not required.
# input_data = """
# 2 3 3
# 1 1 1
# 3 2 0
# 2 1 1 2 2
# 0 2 1 4 5
# 5 1 1 5 5
# """

# # Split lines
# lines = input_data.strip().split('\n')

# # Parse first line
# n, q, c = map(int, lines[0].split())

# # Parse stars
# stars = []
# for i in range(1, 1 + n):
#     x, y, s = map(int, lines[i].split())
#     stars.append((x, y, s))

# # Parse queries
# queries = []
# for i in range(1 + n, 1 + n + q):
#     t, x1, y1, x2, y2 = map(int, lines[i].split())
#     queries.append((t, x1, y1, x2, y2))



#below i wrote just for ref. completely not required.
# input_data = """
# 2 3 3
# 1 1 1
# 3 2 0
# 2 1 1 2 2
# 0 2 1 4 5
# 5 1 1 5 5
# """

# # Split and parse into list of lists
# lines = input_data.strip().split('\n')
# parsed_data = [list(map(int, line.split())) for line in lines]

# # Print for inspection
# for idx, row in enumerate(parsed_data):
#     print(f"Line {idx + 1}: {row}")


#correct. But not required
# n,q,c=map(int,input().split())
# stars=[]
# for _ in range(n):
#     x,y,s=map(int,input().split())
#     stars.append((x,y,s))
# queries=[]
# for _ in range(q):
#     t,x1,y1,x2,y2=map(int,input().split())
#     queries.append((t,x1,y1,x2,y2))



"""
sree sanker solution from pp discussion forum


/* package codechef; // don't place package name! */


import java.lang.*;

import java.io.*;

import java.util.ArrayList;

import java.util.List;


/* Name of the class has to be "Main" only if the class is public. */

public class Main {

    public static void main(String[] args) throws java.lang.Exception {


        BufferedReader r = new BufferedReader(new InputStreamReader(System.in));

        String[] limits = r.readLine().split(" ");


        int n = Integer.parseInt(limits[0]);

        int q = Integer.parseInt(limits[1]);

        int maxBrightness = Integer.parseInt(limits[2]);


        Star[] stars = new Star[n];

        for (int i = 0; i < n; i++) {

            String[] starCordinates = r.readLine().split(" ");

            Star star = new Star(

                    Integer.parseInt(starCordinates[0]),

                    Integer.parseInt(starCordinates[1]),

                    Integer.parseInt(starCordinates[2])

            );

            stars[i] = star;

        }


        while (q > 0) {

            //ti, x1i, y1i, x2i, y2i

            String[] viewDesc = r.readLine().split(" ");

            int t = Integer.parseInt(viewDesc[0]);

            int x1 = Integer.parseInt(viewDesc[1]);

            int y1 = Integer.parseInt(viewDesc[2]);

            int x2 = Integer.parseInt(viewDesc[3]);

            int y2 = Integer.parseInt(viewDesc[4]);


            int brightness = 0;


            for (int i = 0; i < n; i++) {

                if (stars[i].x >= x1 && stars[i].y >= y1

                        && stars[i].x <= x2 && stars[i].y <= y2) {

                    brightness += ((stars[i].initialBrightness + t) % (maxBrightness + 1));

                }

            }


            System.out.println(brightness);

            q--;

        }



    }


    static class Star {

        int x;

        int y;

        int initialBrightness;


        public Star(int x, int y, int initialBrightness) {

            this.x = x;

            this.y = y;

            this.initialBrightness = initialBrightness;

        }

    }



}
"""



"""

Asked chatgpt below doubt:

can i do the same above , without using 3d array, ie just by using 2d array

ChatGPT said:
Great question!

Short Answer:
No, you cannot fully solve this problem using only a 2D array, because the star brightness changes over time, and you need to track different brightness states at each time modulo (c+1).

🔍 Why You Need a 3D Array
Let’s recap the problem:

Each star's brightness changes over time:
At time t, a star with initial brightness s will have brightness (s + t) % (c + 1).

You must answer queries that ask:
"What is the total brightness in a given rectangle at time t?"

To handle this efficiently:

For each time modulo (c+1), you need a snapshot of the brightness at all grid points.

There are c+1 different time states (because of modulo cycling), so you need to precompute brightness grids for each of them → Hence the 3D array:
brightnessGrid[time][x][y].

❓ What If You Used Only One 2D Array?
If you tried to store only one brightness[x][y], then:

You’d be overwriting data from different times.

You’d have no way to quickly answer queries for different time points.

To compute the answer in constant time per query, you must precompute all possible states for (c+1) different brightness levels — that’s what the 3D array gives you.

🧠 Analogy
Think of it like this:

You’re trying to keep track of the weather for each city across 7 days of the week.

You can’t just use a single 2D table of [city][temperature], because you lose track of what the weather was on different days.

You need a 3D table: [day][city][temperature].

✅ Alternatives That Still Use 3D
If you're concerned about space efficiency, here are a few ideas:

c + 1 is at most 11 (since 0 ≤ c ≤ 10), so memory usage is not too big.

If you don’t precompute, you’d have to compute the brightness dynamically per query — that will be much slower (up to O(n) per query), not O(1).

✅ Summary
Approach	Time per Query	Space Used	Feasible?
3D array (your way)	O(1)	O((c+1) * 100 * 100)	✅ Best choice
2D array only	O(n) per query	Less	❌ Too slow
Dynamic calculation	O(n * q)	Low	❌ Inefficient for big n/q

Let me know if you'd like a memory-optimized version (e.g., using 3D arrays more smartly or with compression).



You said:
brightessGrid[x][y] and everytime , i will see time and do brightnessGrid[x][y]+t % c+1

ChatGPT said:
I see what you're suggesting — you're trying to store only the initial state in a 2D grid, and then calculate the brightness dynamically for a given time t, using this logic:

python
Copy
Edit
brightnessGrid[x][y] + t % (c + 1)
Unfortunately, that won't work for this specific problem. Here's why it fails and what you can do instead if you want to avoid a full 3D grid.

❌ Why brightnessGrid[x][y] + t % (c + 1) is Incorrect
This assumes:

There's only one star per cell.

Each star has fixed brightness, and +t is enough to determine the brightness.

But that’s not true. In this problem:

Multiple stars can be at the same position (x, y).

Each star has its own initial brightness s, so:

At time t, its brightness is (s + t) % (c + 1).

So you can’t combine all stars at a cell with a single number and adjust brightness by adding t.

🔴 Example That Breaks Your Logic
Suppose:

You have 2 stars at (3, 3)

Star 1: initial brightness 1

Star 2: initial brightness 3

c = 4

At time t = 2, their brightness will be:

Star 1: (1 + 2) % 5 = 3

Star 2: (3 + 2) % 5 = 0

Total brightness at (3,3) = 3 + 0 = 3

But if you only store:

python
Copy
Edit
brightnessGrid[3][3] = 1 + 3 = 4
Then:

python
Copy
Edit
brightnessGrid[3][3] + t % 5 = 4 + 2 = 6 % 5 = 1 (WRONG)
So this logic doesn’t reflect individual contributions correctly.

✅ What You Can Do If You Want to Avoid a Full 3D Grid
You can instead:

Store stars as a list of (x, y, s) entries.

For each query:

Iterate through all stars

If the star is within the query rectangle, compute its brightness at time t: (s + t) % (c + 1)

Add up

Example (Brute-force Query):
python
Copy
Edit
stars = []
for _ in range(n):
    x, y, s = map(int, input().split())
    stars.append((x, y, s))

for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for x, y, s in stars:
        if x1 <= x <= x2 and y1 <= y <= y2:
            total += (s + t) % (c + 1)
    print(total)
✅ Pros:
Uses only a list and 2D coordinates.

No 3D arrays.

❌ Cons:
Slower per query: O(n) for each query.

Not acceptable for large n or q (e.g., n, q = 10^5).

✅ Final Recommendation
Goal	Best Approach
Speed (large input)	Use 3D grid + prefix sum (your original solution)
Memory saving (small input)	Use list of stars and compute per query

Let me know your constraints — I can help you pick or code the best one.



You said:
what if there isonly one star per cell?

ChatGPT said:
Great follow-up!

✅ If there is only one star per cell, then yes — you can use a 2D array brightnessGrid[x][y] to store the initial brightness s, and compute brightness on the fly at time t using:
python
Copy
Edit
(current_brightness) = (brightnessGrid[x][y] + t) % (c + 1)
⚠️ However, you still can't get away with only one 2D prefix sum, unless you want to do O(n) per query.
To get fast queries (O(1)), you still need to precompute (c+1) prefix sums, one for each possible t mod (c+1), like this:

✅ Optimized 2D Prefix Sum Version (One Star Per Cell)
Step 1: Store one star per cell
python
Copy
Edit
brightnessInit = [[-1] * 101 for _ in range(101)]  # -1 = no star
for _ in range(n):
    x, y, s = map(int, input().split())
    brightnessInit[x][y] = s
Step 2: Precompute (c+1) brightness snapshots
For each time modulo t % (c + 1):

python
Copy
Edit
brightnessAtTime = [[[0] * 101 for _ in range(101)] for _ in range(c + 1)]

for t in range(c + 1):
    for i in range(1, 101):
        for j in range(1, 101):
            if brightnessInit[i][j] != -1:
                brightnessAtTime[t][i][j] = (brightnessInit[i][j] + t) % (c + 1)
Step 3: Build 2D prefix sums for each t
python
Copy
Edit
prefix = [[[0] * 101 for _ in range(101)] for _ in range(c + 1)]
for t in range(c + 1):
    for i in range(1, 101):
        for j in range(1, 101):
            prefix[t][i][j] = (
                brightnessAtTime[t][i][j]
                + prefix[t][i - 1][j]
                + prefix[t][i][j - 1]
                - prefix[t][i - 1][j - 1]
            )
Step 4: Query in O(1) using prefix sum
python
Copy
Edit
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    t %= (c + 1)
    result = (
        prefix[t][x2][y2]
        - prefix[t][x1 - 1][y2]
        - prefix[t][x2][y1 - 1]
        + prefix[t][x1 - 1][y1 - 1]
    )
    print(result)
✅ Summary
Condition	Can Use 2D Array Only?	Prefix Sum Needed?	Fast Query Support
Multiple stars per cell	❌ No	✅ Yes (3D)	✅ O(1)
One star per cell only	✅ Yes (initial state)	✅ Yes (c+1 grids)	✅ O(1)
One star per cell + small n	✅ Yes	❌ No (brute-force)	❌ Slow (O(n))

Let me know if you'd like this version implemented end-to-end — it's a bit more memory efficient when you have the "one star per cell" guarantee.


"""


"""
below precomputation i did while practicing. Below precomputation is correct only, but u already did it in simpler way. Both are same only.
for t in range(0,c+1):
    for x in range(1,101):
        for y in range(1,101):
            brightnessGrid[t][x][y]=brightnessGrid[t][x][y-1]+brightnessGrid[t][x][y]

for t in range(0,c+1):
    for x in range(1,101):
        for y in range(1,101):
            brightnessGrid[t][x][y]=brightnessGrid[t][x-1][y]+brightnessGrid[t][x][y]


simple way which i already did:(you can see code at top)
for t in range(0,c+1):
    for x in range(1,101):
        for y in range(1,101):
            brightnessGrid[t][x][y]=brightnessGrid[t][x][y-1]+brightnessGrid[t][x][y]

    for x in range(1,101):
        for y in range(1,101):
            brightnessGrid[t][x][y]=brightnessGrid[t][x-1][y]+brightnessGrid[t][x][y]


"""

