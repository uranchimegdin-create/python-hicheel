# 1. 1-R INDEX-IIG GARGAH
# m=[[1,2,3],[4,5,6],[7,8,9]] 
# print(m[1])


# 2. 1-R INDEX-IIN DOTORH 2-R INDEX GARGAH.
# m=[[1,2,3],[4,5,6],[7,8,9]] 
# print(m[1][2])



# 3. OUTPUT HOISH TSUVUULNA.
# m=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(0,len(m)):
#     for o in m[i]:
#         print(o,end=" ")
    

# 4. OUTPUT DOOSH TSUVUULNA.
# m=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(0,len(m)):
#     for o in m[i]:
#         print(o)


# 5. 3 MUR BOLGON MUR MURUUR NI TSUVUULNA.
# m=[[1,2,3],[4,5,6],[7,8,9]]
# for i in range(0,len(m)):
#     for o in m[i]:
#         print(o,end=" ")
#     print()


# 6. (5 NI 0-R INDEX) (10,20 NI 1-R INDEX) (30 NI 2-R INDEX)
# b=[5,[10,20],30]
# print(b[1][1])


# TASKSSS...

# 1. 6 тоог хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in range(0,len(nums)):
#     for c in nums[i]:
#         print(c,end=" ")

    
# 2. "Bold"` нэрийг хэвлэ
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# print(students[2][0])


# 3.2 дахь мөрийг хэвлэ
# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# print(nums[1])


# 4.  `70` тоог хэвлэ
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print(nums[2][0])


# 5.Хамгийн эхний утгыг хэвлэ
# nums = [
#     [5, 10],
#     [15, 20]
# ]
# print(nums[0][0])


# # 6. Хамгийн сүүлийн утгыг хэвлэ
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# print(nums[2][1])


# 7. Бүх мөрийг хэвлэ
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for i in nums:
#     print(i)
 

# 8.Бүх тоог хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         print(x)


# 9.Бүх тоог нэг мөрөнд хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         print(x,end=" ")


# 10.  10-аас их тоонуудыг хэвлэ
# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         if x>10:
#             print(x,end=" ")


# 11. Нийт хэдэн тоо байгааг ол
# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]
# count=0
# for i in range(0,len(nums)):
#         for x in nums[i]:
#             count+=1
# print(count)


# 12.  Бүх тооны нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# sum=0
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         sum+=x
# print(sum)


# 13. Тэгш тоонуудыг хэвлэ
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(0,len(nums)):
#     for e in nums[i]:
#         if e % 2==0:
#             print(e,end=" ")

        
# 14.Сондгой тоонуудын тоог ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# count=0
# for i in nums:
#     for x in i:
#         if x %2  != 0:
#             count+=1
# print(count)



# 15.Тэгш тоонуудын нийлбэрийг ол.
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]
# sum=0
# for i in nums:
#     for x in i:
#         if x %2 ==0:
#             sum+=x
# print(sum)


# 16.Эерэг тоонуудын тоог ол
# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]
# count=0
# for i in nums:
#     for x in i:
#         if x >0:
#             count+=1
# print(count)


# 17.Сөрөг тоонуудын нийлбэрийг ол
# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]
# sum=0
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         if x<0:
#             sum+=x
# print(sum)



# 18.Хамгийн их тоог ол
# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]
# best=nums[0][0]
# for m in nums:
#     for num in m:
#         if num > best:
#             best=num
# print(best)


# 19.Хамгийн бага тоог ол.
# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]
# best=nums[0][0]
# for m in nums:
#     for num in m:
#         if num<best:
#             best=num
# print(best)

    
# 20.Мөр бүрийн нийлбэрийг ол
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in nums:
#     print(sum(i))


# 21.Мөр бүрийн хамгийн их тоог ол.
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     a=max(i)
#     b=a
#     print(b)
   

# 22.Мөр бүрийн хамгийн бага тоог ол
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for i in nums:
#     a=min(i)
#     b=a
#     print(b)


# 23. `7` тоо байгаа эсэхийг шалга. `7` байвал:"YES", байхгүй бол:"NO"
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# a=[]
# for i in nums:
#     for j in i:
#         a.append(j)
# if 7 in a:
#     print("YES")
# else:
#     print("NO")


# # 24.  Өгөгдсөн тоо хэдэн удаа байгааг ол. (`target` хэдэн удаа байгааг ол.)
# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]
# count=0
# target = 2
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         if x==target:
#             count+=1
# print(count)


# 25.  5-аас их тоонуудын нийлбэрийг ол.
# nums = [
#     [1, 7, 3], 
#     [9, 2, 6],
#     [4, 8, 5]
# ]
# sum=0
# for i in range(0,len(nums)):
#     for x in nums[i]:
#         if x > 5:
#             sum +=x
# print(sum)



# 26.  Хамгийн их нийлбэртэй мөрийг олоод хэвлэ...
# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]
# print(max(nums))


# 27.   Сурагч бүрийн нэр ба насыг хэвлэ
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# for i in students:
#     for j in i :
#         print(j, end= " ")
#     print()


# 28.  18-аас дээш настай сурагчдыг хэвлэ
# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]
# for name,age in students:
#     if age>18:
#         print(name)


# 29.  Сурагч бүрийн дундаж оноог ол
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80]
# ]
# for name, *scores in students:
#     dundaj = sum(scores)/len(scores)
#     print(name,dundaj)



# 30.   Хамгийн өндөр дундажтай сурагчийг ол
students = [
    ["Bat", 80, 90, 70],
    ["Sara", 100, 90, 95],
    ["Bold", 60, 70, 80],
    ["Anu", 90, 90, 90]
]
for name,*scores in students:
    dundaj=sum(scores)/len(scores)
    a=max.dundaj(students)
print(a)


    

    