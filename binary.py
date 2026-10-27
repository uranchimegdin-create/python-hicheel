# 1. 
# lst=[5,10,15,20,25,30,35]
# target = int(input())
# left = 0
# right = len(lst)-1
# while left <= right:
#     mid = (left + right) // 2 
#     if lst[mid] == target:
#         print("olloo")
#         break
#     elif lst[mid]< target:
#         left = mid + 1
#     else : 
#         right = mid - 1


# # 
# BYNARY.SEARCH BODLOGOGOGOGOGO.


# 1. Хэрэглэгчээс нэг тоо авч, жагсаалтад байгаа эсэхийг шалга. Байвал `Олдлоо`,
#    байхгүй бол `Олдсонгүй` гэж хэвлэ.
# lst=[3, 7, 12, 18, 25, 31, 40]
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI")



# 2. Хэрэглэгчээс тоо авч, олдсон тооны индексийг хэвлэ. Байхгүй бол `-1` хэвлэ.
# lst=[5, 10, 15, 20, 25, 30]
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI")



# 3. Binary Search ашиглан `4` тоог олж, индексийг нь хэвлэ.
# lst=[4, 9, 14, 19, 24, 29, 34]
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI")



# 4.  hamgiin svvvlchiiin тоог хайж, индексийг хэвлэ.
# lst=list(map(int,input("jagsaaltaa ug: ").split(",")))
# a = lst[-1]
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==a:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < a:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("OLDSONGUI") 



# 5. Хэрэглэгчээс тоо авч хай. Олдохгүй бол `Хайж буй тоо байхгүй` гэж хэвлэ.
# lst=list(map(int,input("jagsaaltaa ug: ").split(",")))
# target=int(input("taah toogoo ug: "))
# left=0
# right=len(lst)-1
# while left <= right:
#     mid=(left+right)//2
#     if lst[mid]==target:
#         print("OLDLOOO", mid)
#         break
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# else:
#     print("haisan too chini algaaaaaa") 



# 6. Хэрэглэгчийн оруулсан тоог Binary Search ашиглан хайж, 
#    хэдэн удаа `mid` шалгасныг хэвлэ.
# lst=list(map(int,input("jagsaaltaaa ug: ").split()))
# target=int(input("taah toogoo ug: "))
# count=0
# left=0
# right=len(lst)-1
# while left <= right:
#     mid = (left+right)//2
#     count+=1
#     if lst[mid]==target:
#         return count
#     elif lst[mid] < target:
#         left = mid+1
#     else:
#         right = mid-1
# return -1
# else:
#     print("haisan too chini algaaaaaa") 



# 6. Хэрэглэгчийн оруулсан тоог Binary Search ашиглан хайж, хэдэн удаа 
#   `mid` шалгасныг хэвлэ.
# def benary(ist,target):
#     count=0
#     left=0
#     right=len(lst)-1
#     while left <= right:
#         mid = (left+right)//2
#         count+=1
#         if lst[mid]==target:
#             return count
#         elif lst[mid] < target:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1
# lst=list(map(int,input("jagsaaltaaa ug: ").split(",")))
# lst.sort()
# target=int(input("taah toogooon ug: "))
# print(benary(lst,target))



# 7.  