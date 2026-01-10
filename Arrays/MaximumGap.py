t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().strip().split()))

    if n < 2:
        print(0)
        continue
    minNum = float('inf')
    maxNum = float('-inf')
    for i in range(n):
        minNum = min(nums[i], minNum)
        maxNum = max(nums[i], maxNum)

    if minNum == maxNum:
        print(0)
        continue

    gap = (maxNum - minNum) // (n - 1)

    if (maxNum - minNum) % (n - 1) != 0: gap += 1

    minArr = [float('inf')] * n
    maxArr = [float('-inf')] * n

    for i in range(n):
        bkt_no = (nums[i] - minNum) // gap
        minArr[bkt_no] = min(minArr[bkt_no], nums[i])
        maxArr[bkt_no] = max(maxArr[bkt_no], nums[i])

    # ans=float('-inf')
    # prev=float('-inf')
    # for i in range(n):
    #     if minArr[i]==float('inf'):
    #         continue
    #     if prev==float('-inf'):
    #         prev=maxArr[i]
    #     else:
    #         ans=max(ans,minArr[i]-prev)
    #         prev=maxArr[i]
    # print(ans)

    ans = float('-inf')
    for i in range(n - 1):
        if maxArr[i] != float('-inf'): prev = maxArr[i]
        if minArr[i + 1] != float('inf'):
            ans = max(ans, minArr[i + 1] - prev)

    print(ans)


