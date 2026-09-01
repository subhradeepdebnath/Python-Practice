# # # arr=[1,2,2,3,1,2]
# # # n={}
# # # for i in arr:
# # #     if i in n:
# # #         n[i]+=1
# # #     else:
# # #         n[i]=1
# # # print(n)

# # # arr = [4, 2, 4, 3, 2, 4, 5]
# # # a=[]
# # # for i in range(len(arr)):
# # #     if arr[i] not in a:
# # #         count=1
# # #         for j in range(i+1,len(arr)):
# # #             if arr[i]==arr[j]:
# # #                 count+=1
# # #         a.append(arr[i])
# # #         print(arr[i],count)


# # arr = [4, 2, 4, 3, 2, 4, 5]
# # n={}
# # for i in arr:
# #     if i in n:
# #         n[i]+=1
# #     else:
# #         n[i]=1
# # print(n)


# arr = [5, 2, 8, 3, 5, 9]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]==arr[j]:
#             print(arr[i])
#             break
        
        
# arr = [2, 7, 11, 15]
# target = 9
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]+arr[j]==target:
#             print(arr[i],arr[j])



# arr = [4, 2, 4, 3, 2, 5]
# a=[]
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]== arr[j]:
#             a.append(arr[i])
# for i in range(len(arr)):
#     if arr[i] not in a:
#         print(arr[i])
#         break


# arr = [1, 5, 7, -1, 5]
# target = 6
# count=0
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i]+arr[j]==target:
#             count+=1
# print(count)

# s1 = "listen"
# s2 = "silent"
# s1=sorted(s1)
# s2=sorted(s2)
# if len(s1)!=len(s2):
#     print(False)
# else:
#     flag=True
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             flag=False
#             break
#     print(flag)
            

# s = "({[]})"
# stack=[]
# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if not stack:
#             print("Invalid")
#             break
#         top=stack.pop()
#         if (ch==")" and top !="(" ) or  (ch == "}" and top!= "{") or (ch == "]" and top!= "["):
#             print("Invalid")
#             break
# else:
#     if not stack:
#         print("valid")
#     else:
#         print("invalid")

# s = "hello"
# stack=[]
# for ch in s:
#     stack.append(ch)
# result=""
# while stack:
#     result+=stack.pop()
# print(result)

# arr = [4, 5, 2, 10]
# a=[]
# for i in range(len(arr)):
#     found=False
#     for j in range(i+1,len(arr)):
#         if arr[i]<arr[j]:
#             a.append(arr[j])
#             found=True
#             break
#     if not found:
#         a.append(-1)
# print(a)