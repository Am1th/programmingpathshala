# import math
# n,m =map(int,input().split())
#
# # N=10**5
# # spf=list(range(N+1))
# #
# # for i in range(2,int(math.sqrt(N))+1):
# #     if spf[i]==i:
# #         for j in range(i*i,N+1,i):
# #             if spf[j]==j:
# #                 spf[j]=i
#
# def gcd(a,b):
#     maxm=max(a,b)
#     minm=min(a,b)
#     while(maxm%minm!=0):
#         temp=maxm
#         maxm=minm
#         minm=temp%minm
#     return minm
#
# # states=[0]*(N+1)
# states={}
# for _ in range(m):
#     flag,i=input().split(" ")
#     i=int(i)
#     if flag=="+":
#         if i in states.keys():
#             print("Already on")
#         else:
#             for key in states:   #for key in states.keys()
#                 if gcd(i,key)>1:
#                     print("Conflict with",key)
#                     break
#             else:
#                 states[i]=1
#                 print("Success")
#
#     elif flag=="-":
#         if i in states:   #if states[i]==1:
#             del states[i]
#             print("Success")
#         else:
#             print("Already off")



import math
n,m=map(int,input().split())
N=10**5
spf=list(range(N+1))
for i in range(2,int(math.sqrt(N))+1):
    if spf[i]==i:
        for j in range(i*i,N+1,i):
            if spf[j]==j:
                spf[j]=i

on=[False]*(n+1)


for _ in range(m):
    flag,collideri=map(int,input().split())











