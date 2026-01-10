def check(dict1, dict2):
    # doesnt work
    # if dict1.keys() == dict2.keys() and set(dict1.values())==set(dict2.values()):
    #     return True
    # else:
    #     return False

    """
    The reason dict1.values() == dict2.values() doesn't work  is that dict.values() returns a view of the values in the dictionary, not a list. This view contains the values in an unordered collection.

    say dict1 is {a: 3, b: 1} and dict2 is {b: 1, a: 3}, dict1.values() and dict2.values() will both return the set of values [3, 1], but they represent different frequencies, which means the dictionaries are actually different.

    to make it work u can do as below:
    sorted(dict1.values()) == sorted(dict2.values())

    or

    from collections import Counter
    Counter(dict1.values()) == Counter(dict2.values()) # will correctly compare the frequency of values, regardless of order.

    dict.keys() comparision works correctly because keys are unique and have no duplicates

    """

    # working
    # for key in dict1:
    #     if dict1.get(key)!=dict2.get(key):
    #         return False
    # return True

    # working
    # if dict1==dict2:return True
    # else:return False

    # method3
    # Check if both dictionaries have the same keys
    if dict1.keys() != dict2.keys():
        return False

    # Check if both dictionaries have the same values for each key
    for key in dict1.keys():
        if dict1[key] != dict2[key]:
            return False
    return True


# alternate check function tarn solution
"""
def check(dict1,dict2):
    for key in dict2:
        if(dict2[key]>0):
            if(key not in dict1 or dict1[key]!=dict2[key]):
                return False
    return True
"""

t = int(input())
for i in range(t):
    dict1 = {}
    dict2 = {}
    s1 = input().strip()
    s2 = input().strip()
    n = len(s1)
    m = len(s2)

    # If s1 is longer than s2, it's impossible to find a permutation of s1 in s2
    if n > m:
        print(False)
        continue

    # Build dict1 for s1
    for ele in s1:
        if ele in dict1:
            dict1[ele] += 1
        else:
            dict1[ele] = 1
        # dict1[ele]=dict1.get(ele,0)+1 alternate to above lines

    # first window
    for i in range(n):
        if s2[i] in dict2:  # index out of bounds error if n>m
            dict2[s2[i]] += 1
        else:
            dict2[s2[i]] = 1

    # first window check
    if check(dict1, dict2):
        print(True)
        continue

    # sliding the window over s2 from index n to m
    re = False
    for j in range(n, m):
        if s2[j] in dict2:
            dict2[s2[j]] += 1
        else:
            dict2[s2[j]] = 1

        if dict2[s2[j - n]] > 1:
            dict2[s2[j - n]] -= 1
        elif dict2[s2[j - n]] == 1:
            del dict2[s2[j - n]]
            # dict2.pop(s2[j-n])

        if check(dict1, dict2):
            re = True
            break

    print(re)
#same above code, little improvements in way of writing
# t = int(input())
# def check(dict1, dict2):
#     return dict1 == dict2
#
# for _ in range(t):
#     s1 = input().strip()  #if strip not used this happened s1="ab " , dict1={'a':1,'b':1,' ':1}
#     s2 = input().strip()
#     dict1 = {}
#     dict2 = {}
#     n = len(s1)
#     m = len(s2)
#     if m < n:
#         print(False)
#         continue
#
#     for i in range(n):
#         dict1[s1[i]] = 1 + dict1.get(s1[i], 0)
#         dict2[s2[i]] = 1 + dict2.get(s2[i], 0)
#
#     if check(dict1, dict2):
#         print(True)
#         continue
#
#     re = False
#     for j in range(n, m):
#         dict2[s2[j]] = 1 + dict2.get(s2[j], 0)
#         dict2[s2[j - n]] -= 1
#         if dict2[s2[j - n]] == 0:
#             del dict2[s2[j - n]]
#
#         if check(dict1, dict2):
#             re = True
#             break
#     print(re)



# Alternate code
# below code works, used array
# def checkInclusion(s1,s2):
#     n=len(s1)
#     m=len(s2)

#     if n>m:return False

#     s1_count=[0]*26
#     s2_count=[0]*26

#     #count frequency of characters in first window for s1 and s2
#     for i in range(n):
#         s1_count[ord(s1[i])-ord('a')]+=1
#         s2_count[ord(s2[i])-ord('a')]+=1

#     #compare frequency arrays for the first window
#     if s1_count==s2_count:
#         return True

#     #sliding window
#     for j in range(n,m):
#         s2_count[ord(s2[j])-ord('a')]+=1
#         s2_count[ord(s2[j-n])-ord('a')]-=1

#         if s1_count==s2_count:
#             return True

#     return False


# t=int(input())
# for _ in range(t):
#     s1=input()
#     s2=input()
#     if checkInclusion(s1,s2):
#         print("True")
#     else:
#         print("False")

#few points to take care in above code using array
"""
s1=input().strip()
s2=input().strip() #if strip is not used,ord could break
#ex if input is 'abc\n' or 'abc '
#ord('\n') - ord('a')  → 10 - 97 = -87
# ord(' ') - ord('a')   → 32 - 97 = -65
s1_count=[0]*26 # s1_count=[0]*len(s1) wrong
s2_count=[0]*26 # s2_count=[0]*len(s2)
# s1=input().split() if i use split ord function getting error. say s1="abc".split() gives s1=["abc"]
# ord(s1[0]) then means ord("abc"). ord function expects character , not string. so this will give error.
"""



"""
java: 'a' - 'a' works directly (gives 0).

Python: You need to use ord('a') - ord('a') (gives 0).
"""

# Alternate code
# the below code will not consider characters frequency
# t=int(input())
# while t>0:
#     s1=input()
#     s2=input()
#     cnt,max_cnt=0,0
#     for i in range(len(s1)):
#         if s2[i] in s1:
#             cnt+=1
#     max_cnt=max(max_cnt,cnt)

#     for j in range(len(s1),len(s2)):
#         if s2[j] in s1:
#             cnt+=1
#         if s2[j-len(s1)] in s1:
#             cnt-=1
#         max_cnt=max(max_cnt,cnt)

#     if max_cnt==len(s1):
#         print("True")
#     else: print("False")
#     t-=1


"""
points reg dictionary during practice

In Python, trying to increment a key that does not exist in a dictionary will raise a KeyError. For example:

d = {}
d['a'] += 1   # ❌ KeyError: 'a'
    
    
But using .get() allows you to provide a default value if the key doesn't exist:
d['a'] = d.get('a', 0) + 1   # ✅ works fine; adds 'a' with value 1


When is dict[key] += 1 fine?
Only if you know for sure the key already exists:

if key in dict:
    dict[key] += 1
else:
    dict[key] = 1
    
    or

from collections import defaultdict
dict = defaultdict(int)
dict[key] += 1   # ✅ safe because default is 0



note:
dict1 == dict2 # compares content
dict1 is dict2  # compares reference

not required now should see in future:
dict1 == dict2
Internally becomes:
dict.__eq__(dict1, dict2)
And dict.__eq__ is implemented as content comparison

"""