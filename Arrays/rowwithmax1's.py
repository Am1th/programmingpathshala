class Solution:
    # def rowWithMax1s(self, arr):
    #     max_cnt=0
    #     max_row_index=-1
    #     for i,row in enumerate(arr):
    #         cnt=0
    #         f=self.firstOccurence(row,0,len(row)-1)
    #         if f!=-1:cnt=(len(row)-1-f+1)
    #         if cnt>max_cnt:
    #             max_cnt=cnt
    #             max_row_index=i
    #     return max_row_index
    """
    while practice wrote below one, exact same above logic but see cnt declared only when f!=-1. also  wrote nested if.
    def rowWithMax1s(self, arr):
        max_cnt=0
        max_row_index=-1
        for i,row in enumerate(arr):
            f=self.firstOccurence(row,0,len(row)-1)
            if f!=-1:
                cnt=len(row)-f
                if cnt>max_cnt:  #max_cnt=max(max_cnt,cnt)
                    max_cnt=cnt
                    max_row_index=i
        return max_row_index



    """
    # """
    # enumerate(arr): This function returns an enumerate object, which is an iterator that generates pairs of the index and the value from the iterable.
    # For example, if arr = [[1, 0], [0, 1], [1, 1]], calling enumerate(arr) would return:

    # (0, [1, 0]),
    # (1, [0, 1]),
    # (2, [1, 1])

    # without enumerate u might have to write like this:
    # for i in range(len(arr)):
    # row = arr[i]

    # Question: for i,row in arr:  #why this doesn't work?
    # Answer:
    # arr is a list of lists:   In for i, row in arr:,   Python expects arr to yield pairs (tuples), but a list of lists (2D array) only yields individual lists, not pairs of an index and a list. So, Python doesn't know how to unpack these individual lists into i and row correctly.

    # In other words, this would work only if arr was a list of tuples, like this:
    # arr = [(0, [1, 0]), (1, [0, 1]), (2, [1, 1])]
    # Then, the below code would work because each element in arr is already a tuple of (index, row):
    # for i, row in arr:
    #     # Here, i would be the index, and row would be the list.

    # However, since arr is not a list of tuples (but a list of lists), you need to use enumerate to get both the index and the value during iteration:
    # for i, row in enumerate(arr):
    #     # i is the index, and row is the list at that index

    # """
    # def firstOccurence(self,row,low,high):
    #     if low>high:
    #         return -1

    #     mid=(low+high)//2
    #     if row[mid]<1:
    #         return self.firstOccurence(row,mid+1,high)
    #     elif row[mid]==1:
    #         if mid==0 or row[mid-1]!=row[mid]:
    #             return mid
    #         else:
    #             return self.firstOccurence(row,low,mid-1)

    # approach: traverse the matrix column by column from left to right. As soon as we encounter a 1, we can conclude that the current row is the first row with the maximum number of 1s
    # def rowWithMax1s(self, arr):
    #     m=len(arr)
    #     n=len(arr[0])  #in few cases can write as len(arr[i]) instead of hardcoding as  len(arr[0])
    #     for j in range(n):
    #         for i in range(m):
    #             if arr[i][j]==1:
    #                 return i
    #     else:
    #         return -1

    # someones code
    # def rowWithMax1s(self, arr):
    #     l=[]
    #     for i in range(len(arr)):
    #         countofOnesInRow=arr[i].count(1)
    #         l.append(countofOnesInRow)
    #     return l.index(max(l))

    def rowWithMax1s(self, arr):
        m = len(arr)  # Number of rows
        n = len(arr[0])  # Number of columns
        r = 0
        c = n - 1  # starting from top right of the matrix
        max_row_index = -1
        while r < m and c >= 0:
            if arr[r][c] == 1:
                c -= 1  # Move left if 1 is found
                max_row_index = r
            elif arr[r][c] == 0:
                r += 1  # Move down if 0 is found
        return max_row_index


    # same above with better naming convention that's it.
    # def rowWithMax1s(self, arr):
    #     m = len(arr)
    #     n = len(arr[0])
    #
    #     i = 0
    #     j = n - 1
    #
    #     ans = -1
    #     while (i < m and j >= 0):
    #         if arr[i][j] == 1:
    #             ans = i
    #             j -= 1
    #         elif arr[i][j] == 0:
    #             i += 1
    #     return ans






