# Very bad solution, TLE for all test cases, first test case only accepted
# T × N log N   (worst case 10^6 × 10^6 — impossible)
import math

t = int(input())
N = 10 ** 6
primes = [1] * (N + 1)
primes[0] = primes[1] = 0
spf = [-1] * (N + 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i] == 1:
        for j in range(i, (N // i) + 1):
            if primes[i * j] == 1:
                primes[i * j] = 0
                spf[i * j] = i

for _ in range(t):
    n = int(input())
    res = []
    happyPrimes = 0
    for num in range(2, n + 1):
        cnt = 0
        while spf[num] != -1:
            p = spf[num]
            while num % p == 0:
                num = num // p
            cnt += 1
        if num > 1: cnt += 1
        if cnt == 2:
            happyPrimes += 1
    res.append(happyPrimes)
    print(*res)



#accepted
#computing divisors for all numbers till N ie 10^6 , and using prefixArray
import math

t = int(input())
N = 10 ** 6
primes = [1] * (N + 1)
primes[0] = primes[1] = 0
spf = [-1] * (N + 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i] == 1:
        for j in range(i, (N // i) + 1):
            if primes[i * j] == 1:
                primes[i * j] = 0
                spf[i * j] = i

cnt = [0] * (N + 1)
cnt[0] = cnt[1] = 0
for num in range(2, N + 1):
    x = num
    c = 0
    while spf[num] != -1:
        p = spf[num]
        while num % p == 0:
            num = num // p
        c += 1
    if num > 1: c += 1
    cnt[x] = c

pref = [0] * (N + 1)
for i in range(1, N + 1):
    pref[i] = pref[i - 1] + (1 if cnt[i] == 2 else 0)

for _ in range(t):
    n = int(input())
    print(pref[n])


#accepted
import math

t = int(input())
N = 10 ** 6
spf = list(range(N + 1))

for i in range(2, int(math.sqrt(N)) + 1):
    if spf[i] == i:
        for j in range(i * i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

cnt = [0] * (N + 1)
for num in range(2, N + 1):
    x = num
    c = 0
    while num > 1:
        p = spf[num]
        while num % p == 0:
            num = num // p
        c += 1
    cnt[x] = c

pref = [0] * (N + 1)
for i in range(1, N + 1):
    pref[i] = pref[i - 1] + (1 if cnt[i] == 2 else 0)

for _ in range(t):
    n = int(input())
    print(pref[n])






#suggested by chatgpt
#O(N log log N)
N = 10 ** 6
cnt = [0] * (N + 1)
for i in range(2,N+1):   # Count distinct prime divisors for every number
    if cnt[i]==0:    # i is prime
        for j in range(i,N+1,i):
            cnt[j]+=1

pref = [0] * (N + 1)
for i in range(1, N + 1):
    pref[i] = pref[i - 1] + (1 if cnt[i] == 2 else 0)

t = int(input())
for _ in range(t):
    n = int(input())
    print(pref[n])

"""
alternate loop to above         
for i in range(2, N + 1):
    if cnt[i] == 0: # i is prime
        for j in range(1, (N // i) + 1): 
            cnt[i * j] += 1
"""



# from below just read last note

"""
java solution : 
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws java.lang.Exception {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(sc.readLine().trim());

        int[] testCases = new int[T];

        int max = 0;

        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(sc.readLine().trim());
            testCases[i] = n;
            max = Math.max(max, n);
        }

        int[] primeCountArray = getSieveArray(max);

        StringBuilder output = new StringBuilder();
        for (int num : testCases) {
            if (num < 4) {
                output.append("0\n");
            } else {
                output.append(primeCountArray[num]).append("\n");
            }
        }
        System.out.print(output);

    }

    static int[] getSieveArray(int n) {
        if (n < 4) return new int[n + 1];

        int[] spf = new int[n + 1];
        int[] primeCountArray = new int[n+1];

        for (int i = 2; i <= n; i++) {
            spf[i] = i;
        }

        for (int i = 2; i <= n; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= n; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }


        int happyPrimeCount = 0;
        for (int i = 4; i <= n; i++) {
            int value = i;
            Set<Integer> distinctPrimes = new HashSet<>();

            while (value > 1) {
                distinctPrimes.add(spf[value]);
                value /= spf[value];
            }

            if (distinctPrimes.size() == 2) {
                happyPrimeCount++;
            }

            primeCountArray[i] = happyPrimeCount; 
        }

        return primeCountArray;
    }



}



the above can be optimized to below: 
------------------------------------
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static final int MAXN = 1_000_000;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());

        int[] queries = new int[T];
        int maxN = 0;

        for (int i = 0; i < T; i++) {
            queries[i] = Integer.parseInt(br.readLine().trim());
            maxN = Math.max(maxN, queries[i]);
        }

        int[] prefixHappyPrimeCount = precomputeHappyPrimes(maxN);

        StringBuilder sb = new StringBuilder();
        for (int n : queries) {
            sb.append(prefixHappyPrimeCount[n]).append('\n');
        }

        System.out.print(sb);
    }

    // Precompute prefix count of numbers with exactly 2 distinct prime factors
    static int[] precomputeHappyPrimes(int n) {

        int[] spf = new int[n + 1];

        // Step 1: Build SPF array
        for (int i = 2; i <= n; i++) {
            spf[i] = i;
        }

        for (int i = 2; i * i <= n; i++) {
            if (spf[i] == i) { // i is prime
                for (int j = i * i; j <= n; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }

        // Step 2: Build prefix array
        int[] prefix = new int[n + 1];
        int happyCount = 0;

        for (int i = 2; i <= n; i++) {
            int x = i;
            int distinctCount = 0;
            int prevPrime = -1;

            while (x > 1) {
                int p = spf[x];
                if (p != prevPrime) {
                    distinctCount++;
                    prevPrime = p;
                }
                x /= p;
            }

            if (distinctCount == 2) {
                happyCount++;
            }

            prefix[i] = happyCount;
        }

        return prefix;
    }
}





⚠️ Issues / Improvements
❌ 1️⃣ HashSet inside a loop (performance issue)

Set<Integer> distinctPrimes = new HashSet<>();
This is correct but slow.
Why?
	• You create up to 1,000,000 HashSet objects
	• HashSet involves hashing, resizing, object allocation
This won’t TLE in Java for 10^6, but it’s not interview-optimal.

✅ Better way (no HashSet, faster)
You only care about count, not the actual primes.
Replace this:

Set<Integer> distinctPrimes = new HashSet<>();
while (value > 1) {
    distinctPrimes.add(spf[value]);
    value /= spf[value];
}
if (distinctPrimes.size() == 2)



With this:

int prev = -1;
int count = 0;
while (value > 1) {
    int p = spf[value];
    if (p != prev) {
        count++;
        prev = p;
    }
    value /= p;
}

if (count == 2)


Note this part from above code:   ( will be useful while spf calculation )
------------------------------------------------
int prev = -1;
int count = 0;

while (value > 1) {
    int p = spf[value];
    if (p != prev) {
        count++;
        prev = p;
    }
    value /= p;
}

if (count == 2)

"""





