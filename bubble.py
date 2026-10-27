# BUBBLE.SORT

# 1.
# nums = [3, 8,5, 2,1]
# for i in range(len(nums) -1): 
#     for j in range(len(nums)-1 -i): 
#         if nums[j] > nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1]=a
# print(nums)

# TASKSSSSSSSSSSS...

# 1. Тоонуудыг өсөх дарааллаар эрэмбэлэх
# numbers=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(numbers)-1):
#     for j in range(len(numbers)-1 -i):
#         if numbers[j] > numbers[j+1]:
#             a = numbers[j]
#             numbers[j] = numbers[j+1]
#             numbers[j+1] = a
# print(numbers)



# 2. Тоонуудыг буурах дарааллаар эрэмбэлэх
# nums=list(map(int,input("toonuudaa ug: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] < nums[j+1]:
#             a = nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 3. Өсөх дарааллаар эрэмбэл.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 4. Өсөх дарааллаар эрэмбэл. Давхардсан тоонуудыг устгаж болохгүй.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)


# 5. Хэрэглэгч нэг мөрөнд зайгаар тусгаарлан тоонууд оруулна.
# nums=list(map(int,input("TOONUUDAA UG: ").split()))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 6. Нэрсийг цагаан толгойн дарааллаар эрэмбэлэх
#    Bubble Sort ашиглан нэрсийг цагаан толгойн дарааллаар эрэмбэл.
# names=list(map(str,input("NERSEE UG: ").split(",")))
# for i in range(len(names)-1):
#     for j in range(len(names)-1 -i):
#         if names[j] > names[j+1]:
#             a=names[j]
#             names[j] = names[j+1]
#             names[j+1] = a
# print(names)


# 7. Оноонуудыг өсөх дарааллаар эрэмбэлэх
# scores= list(map(int,input("ONOODUUDAA UG: ").split(",")))
# for i in range(len(scores)-1):
#     for j in range(len(scores)-1 -i):
#         if scores[j] > scores[j+1]:
#             a=scores[j]
#             scores[j] = scores[j+1]
#             scores[j+1] = a
# print(scores)



# 8. Хамгийн их тоог төгсгөлд гаргах 
#    Зөвхөн **нэг удаагийн** дотоод давталт ажиллуул. Хөрш хоёр элементийг харьцуулж,
#    шаардлагатай үед соль.
# nums= list(map(int,input("TOONUUDAAA UG: ").split(",")))
# for i in range(len(nums)-1):
#         if nums[i] > nums[i+1]:
#             a=nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = a
# print(nums)



# 9. Жагсаалт эрэмбэлэгдэхэд хэдэн тойрог хэрэгтэй вэ?
#    Bubble Sort-ийн гадна давталт хэдэн удаа ажиллахыг тодорхойл. 
#    Дараа нь эрэмбэлсэн жагсаалтыг хэвлэ.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1):
#     count += 1
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums,count)



# 10.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         count += 1
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums,count)



# 11.  Хамгийн ихээс хоёр дахь тоог олох. Bubble Sort ашиглан буурах дарааллаар 
#      эрэмбэлээд хоёр дахь хамгийн их тоог хэвлэ.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] < nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums,nums[1])



# 12. Bubble Sort ашиглан өсөх дарааллаар эрэмбэл. Сөрөг тоонууд эхэнд байрлах ёстой.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)



# 13. Гадна давталт бүр дуусахад жагсаалтын тухайн үеийн төлөвийг хэвлэ.
#     Ингэснээр сурагчид тойрог бүрд хамгийн их үлдсэн тоо хэрхэн 
#     төгсгөл рүү шилжиж байгааг ажиглана.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#     print(nums)



# 14. Bubble Sort ашиглан жагсаалтыг эрэмбэл. Хэрэв нэг ч солилцоо хийгдээгүй
#     бол эрэмбэлэгдсэн байна гэж үзээд давталтыг эрт зогсоо.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     count=False
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#             count = True
#     if count == False:
#         break
#     else:
#         print("sort bollooo")
# print(nums)



# 15. Солилцоо хийгдээгүй тойргийн дараа давталтыг зогсоодог алгоритм бич.
#     Эцэст нь жагсаалт зөв эрэмбэлэгдсэн эсэх болон хэдэн тойрог ажилласныг хэвлэ.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# total=0
# for i in range(len(nums)-1):
#     count=False
#     total+=1
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#             count=True
#     if count == False:
#         break 
# print(count)
# print(nums)


# 16. Bubble Sort ашиглан оюутнуудыг оноогоор нь өсөх дарааллаар эрэмбэл.
#     Нэр болон оноо хамт шилжих ёстой.
# n=int(input("HEDIIG ORUULAH VE: "))
# students=[]
# for i in range(n):
#     name=str(input("NEREE ORUUL: "))
#     score=int(input("ONOOG NI ORUUL: "))
#     students.append([name,score])
# for i in range(len(students)-1):
#     for j in range(len(students)-1 -i):
#         if students[j][1] > students[j+1][1]:
#             a=students[j]
#             students[j] = students[j+1]
#             students[j+1] = a
# print(students)



# 17. Хүмүүсийг насаар нь багаас их рүү эрэмбэл. Хамгийн залуу болон 
#     хамгийн ахмад хүний нэрийг хэвлэ.
# n=int(input("HEDEN HVN ORUULAH VE?: "))
# people=[]
# for i in range(n):
#     name=str(input("NEREE UG: "))
#     age=int(input("NASAA UG: "))
#     people.append([name,age])
# for i in range(len(people)-1):
#     for j in range(len(people)-1 -i):
#         if people[j][1] > people[j+1][1]:
#             a=people[j]
#             people[j] = people[j+1]
#             people[j+1] = a
# print(people)
# print(f"hamgiin zaluu : {people[0]}\nhamgiin hogshin : {people[-1]}")



# 18. Bubble Sort ашиглан эрэмбэл. Дараа нь `4` тоо хэдэн удаа байгааг 
#     давталтаар тоол.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# for i in nums:
#     if i == 4:
#         count += 1
# print(nums)
# print(f"{count} bainaa")



# 19. Бараануудыг үнээр нь буурах дарааллаар эрэмбэл. 
#     Хамгийн үнэтэй гурван барааны нэр, үнийг хэвлэ.
# n=int(input("HEDEN BARAA ORUULAH VE?: "))
# baraa=[]
# for i in range(n):
#     name=str(input("BARAANII NEREE UG: "))
#     une=int(input("UNEE UG: "))
#     baraa.append([name,une])
# for i in range(len(baraa)-1):
#     for j in range(len(baraa)-1 -i):
#         if baraa[j][1] < baraa[j+1][1]:
#             a=baraa[j]
#             baraa[j] = baraa[j+1]
#             baraa[j+1] = a
# print(baraa)
# print(f"HAMGIIN UNETEI 3 BARAA {baraa[0:3]} BNAAA")



# 20. Дараах бүх даалгаврыг гүйцэтгэ:
#     1. Bubble Sort ашиглан өсөх дарааллаар эрэмбэл.
#     2. Нийт харьцуулалтын тоог тоол.
#     3. Нийт солилцооны тоог тоол.
#     4. Гадна давталтын нийт тойргийг тоол.
#     5. Эцсийн жагсаалтыг хэвлэ.
#     6. `sort()` болон `sorted()` ашиглахгүй.

# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# count=0
# soliltsoo = 0
# haritsuulalt = 0
# for i in range(len(nums)-1):
#     count+=1
#     for j in range(len(nums)-1 -i):
#         soliltsoo += 1
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
#             haritsuulalt += 1

# print(f"GADNA DAVTALT: {count}")
# print(f"SOLILTSOO: {soliltsoo}")
# print(f"HARITSUULALT: {haritsuulalt}")
# print(nums)

