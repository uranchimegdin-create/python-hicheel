# 1. Хоёр дахь хамгийн их тоо. Давхардсан утгыг нэг утга гэж үзээд 2 дахь хамгийн их тоог ол.
# nums = list(map(int,input().split()))
# nums=list(set(nums))
# nums.sort()
# print(nums[-2])


# 2.Хоёр дахь хамгийн бага тоо.List дотроос 2 дахь хамгийн бага ялгаатай тоог ол.
# too=list(map(int,input().split()))
# too=list(set(too))
# too.sort()
# print(too[1])


# 3.Хамгийн урт дараалсан сондгой хэсэг.List дотор дараалсан сондгой тоонуудын хамгийн урт хэсгийн уртыг ол.
# nums = [2, 1, 3, 5, 4, 7, 9, 11, 6]
# count=0
# ist=[]
# for i in range(0,len(nums)-1):
#     if i % 2 !=0:
#         count+=1
#     elif 






# 4.Хамгийн урт өсөх дараалал.Зөвхөн зэрэгцээ элементүүд өсөж байгаа хэсгээс хамгийн уртыг ол.
# too=[1, 2, 4, 2, 3, 5, 7, 9]
# count = 0
# lst = []
# for i in range(0,len(too)-1):
#     if too[i] < too[i+1]:
#         count += 1
#     else:
#         lst.append(count)
#         count=0
# count=0
# lst.append(count)
# print(lst)
# print(max(lst))



# # 5. List дотор хамгийн олон удаа орсон тоог ол.Хэрэв ижил давтамжтай хэд хэдэн тоо байвал хамгийн бага тоог сонго.
# a=[2,3,4,3,5,6,5,5,8]
# max_count=0
# davtalt=0
# for i in a:
#     if a.count(i)>max_count:
#         max_count=a.count(i)
#         davtalt=i
# print(davtalt)




# 6.






# 7.Хоёр list өгөгдөнө. Аль алинд нь байгаа элементүүдийг шинэ list-д оруул. Давхардахгүй байх ёстой.
# a = {1, 2, 3, 4, 5}
# b = {3, 5, 7, 8, 1}
# print(a & b)


# 8. List доторх хоёр өөр байрлалтай элементүүдээс нийлбэр нь хамгийн их байх хосыг ол.
# a=[4, 7, 2, 9, 5]
# a.sort()
# print(a[-2],end=" ",a[-1])


# 9.Нийлбэр нь target.List болон target өгөгдөнө.Нийлбэр нь target болох хоёр элементийн index-ийг ол.
# nums = [4, 8, 2, 7, 5]
# target = 9





# 10. List доторх хоёр өөр тооны абсолют зөрүү хамгийн бага байх хосыг ол.
# a=[2,15,20,18,14,33]
# a.sort()



# 11.List-ийн сүүлийн элементийг эхэнд нь аваач.insert(), slicing ашиглахгүй.
# number=[1,2,3,4,5]
# new_list = [number[-1]]
# for i in range(len(number) - 1):
#     new_list.append(number[i])
# print(new_list)


# 12.List-ийг баруун тийш K удаа rotate хий.
nums = [1,2,3,4,5]
k = 2
for i in range(k):
    last=nums.pop()
    nums.insert(0,last)
print(nums)








