import math
t = int(input())
def divisors(n):
    val = int(math.sqrt(n))
    if val * val == n: return 0  # if perfect square return immediately

    cnt = 0
    result = []
    for i in range(1, int(val) + 1):
        if n % i == 0:
            cnt += 1
            result.append(i)
            result.append(n // i)  # if i!=val:result.append(n//i)

        if cnt > 2:
            break

    if cnt < 2 or cnt > 2:
        return 0
    else:                   #when cnt == 2
        return sum(result)


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for num in arr:
        ans += divisors(num)
    print(ans)


#same solution as above, no need to store divisors , so i removed result array.
import math

t = int(input())
def divisors(n):
    val = int(math.sqrt(n))
    if val * val == n: return 0  # if perfect square return immediately
    cnt = 0
    s = 0
    for i in range(1, int(val) + 1):
        if n % i == 0:
            cnt += 1
            s += i
            s += n // i

        if cnt > 2:
            return 0

    return s if cnt == 2 else 0

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for num in arr:
        ans += divisors(num)
    print(ans)




#chatgpt solution
import math

t = int(input())

def divisors(n):
    val = int(math.sqrt(n))
    cnt = 0
    s = 0

    for i in range(1, val + 1):
        if n % i == 0:
            j = n // i

            # add divisor i
            cnt += 1
            s += i

            # add matching divisor j (if different)
            if i != j:
                cnt += 1
                s += j

            # early exit if already >4
            if cnt > 4:
                return 0

    return s if cnt == 4 else 0


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = sum(divisors(x) for x in arr)
    print(ans)
