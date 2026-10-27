# YRONHIII EREMBELEH CODE: 


# def merge_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# numbers = list(map(int,input("TOONII JAGSAALT UG: ").split()))
# print(merge_sort(numbers))



# TASKSSSSSSSSSSSSS

# 1. Тоон массивыг merge sort ашиглан багаас их рүү эрэмбэл.
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result=[]
#     i=0
#     j=0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# arr = list(map(int,input("TOONUUDAA UG: ").split()))
# print(merge_sort(arr))



# 2. Тоон массивыг merge sort ашиглан ихээс бага руу эрэмбэл. Эхлээд өсөхөөр 
#    эрэмбэлээд дараа нь эргүүлж болохгүй, merge хэсгийг өөрчилж шийд.
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)
     
#     result=[]
#     i=0
#     j=0

#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# nums=list(map(int,input("TOONUUDAA UG: ").split()))
# print(merge_sort(nums))



# 3. Ижил тоо хэд хэд орсон массивыг өсөхөөр эрэмбэл. Давхардсан
#    тоонууд **алга болж болохгүй**, бүгд үлдэх ёстой.
# def merge(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums)//2
#     left = nums[:mid]
#     right = nums[mid:]

#     left = merge(left)
#     right = merge(right)

#     result=[]
#     i=0
#     j=0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# nums=list(map(int,input("TOONUUDAA UG: ").split()))
# print(merge(nums))            



# 4.  Сөрөг, эерэг тоо болон 0 холилдсон массивыг өсөхөөр эрэмбэл.
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result=[]
#     i=0
#     j=0
#     while i < len(left) and j < len(right):
        # if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# arr = list(map(int,input("TOONUUDAA UG: ").split()))
# print(f"OSOHOOR EREMBELEBEL: {merge_sort(arr)}")

# a,b = list(map(int,input("TOONUUDAA UG: ").split()))
# if a > b:
#     print(f"IH TOO NI: {a}")
# else: 
#     print(f" IH TOO NI: {b}")



# 5. Массивын **тэгш тоонуудыг эхэнд нь** өсөхөөр, 
#    **сондгой тоонуудыг араас нь** өсөхөөр байрлуул.
# def merge_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# numbers=list(map(int,input("TOONUUDAA UG: ").split(",")))
# a=merge_sort(numbers)
# p=[]
# s=[]
# for i in a:
#     if i % 2 == 0:
#         p.append(i)
#     else:
#         s.append(i)
# k=p+s
# print(f"UGSUN JAGSAALT: {numbers}")
# print(f"YLGAGDSAN GARALT: {k}")
# print(f"USUH DARAALAL: {a}")
# print(f"TEGSH TOO: {p}")
# print(f"SONDGOI TOO: {s}")



# 6. Аль хэдийн өсөхөөр эрэмбэлэгдсэн хоёр массив өгөгдөнө. 
#    Тэдгээрийг нэг эрэмбэлэгдсэн массив болгож нэгтгэ. Хоёуланг нь
#    залгаад дахин эрэмбэлж болохгүй, зөвхөн `merge` функцийг ашигла.
# def merge(numbers):
#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge(left)
#     right = merge(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# a=list(map(int,input("TOONUUDAA UG: ").split(",")))
# b=list(map(int,input("TOONUUDAA UG: ").split(",")))
# print(merge(a+b))



# 7. Массивын хамгийн бага 3 тоог багаас их рүү буцаа. 
#    Массив дор хаяж 3 элементтэй гэж үзнэ.
# def smallest_three(numbers):

#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = smallest_three(left)
#     right = smallest_three(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result[:3]

# numbers = list(map(int,input("TOONII JAGSAALT UG: ").split(",")))
# print(smallest_three(numbers))



# 8. Merge sort ажиллах явцад:
#    **харьцуулалтын тоо** — merge хийх үед `left[i] <= right[j]`
#    шалгалт нийт хэдэн удаа хийгдсэн,
#    **merge-ийн тоо** — `merge` функц нийт хэдэн удаа дуудагдсан

#    гэдгийг тоолж, эрэмбэлэгдсэн массивтай хамт хэвлэ.
#    Массивыг `mid = len(arr) // 2` гэж хуваана.
# def merge_sort(numbers):

#     if len(numbers) <= 1:
#         return numbers

#     mid = len(numbers) // 2
#     left = numbers[:mid]
#     right = numbers[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:

#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
#    

# numbers = list(map(int,input("TOONII JAGSAALT UG: ").split(",")))
# print(f"EREMBELEGDSEN: {merge_sort(numbers)}")
# print(f"HARITSUUALT TOO: {haritsuulalt}")
# print(f"MERGE TOO: {merge}")


# 9.  Массивын хамгийн их 2 тоог ихээс бага руу буцаа.
#     Массив дор хаяж 2 элементтэй гэж үзнэ.
# def largest_two(nums):
#     if len(nums) <= 1:
#         return nums
#     mid= len(nums) // 2
#     left = nums[:mid]
#     right = nums[mid:]

#     left = largest_two(left)
#     right = largest_two(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] >= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result[:2]

# nums = list(map(int,input("TOONII JAGSAALT UG: ").split(",")))
# print(largest_two(nums))



# 10. Нэрсийн жагсаалтыг цагаан толгойн дарааллаар эрэмбэл. 
#     Бүх нэр том үсгээр эхэлнэ.
# def merge_sort(names):

#     if len(names) <= 1:
#         return names

#     mid = len(names) // 2
#     left = names[:mid]
#     right = names[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     result = []

#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# names = list(map(str,input("NERSIIN JAGSAALT UG: ").split()))
# print(merge_sort(names))


# 11. Сурагч бүр `(нэр, оноо)` хэлбэрийн tuple-ээр өгөгдөнө. Сурагчдыг:
#     1. **оноогоор ихээс бага руу**,
#     2. оноо **тэнцүү** бол **нэрээр цагаан толгойн дарааллаар**
# def sort_students(students):
#     if len(students) <= 1:
#         return students
#     mid = len(students)//2
#     left = students[:mid]
#     right = students[mid:]

#     left = sort_students(left)
#     right = sort_students(right)

#     result=[]
#     i=0
#     j=0

#     while i < len(left) and j < len(right):
#         if left[i][1] > right[j][1] or (left[i]==right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i<len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result
# n=int(input("HEDEN NER UGUH?: "))
# students=[]
# for i in range(n):
#     name = input("NEREE UG: ")
#     score=int(input("ONOOG NI UG: "))
#     students.append((name,score))
# print(sort_students(students))



# 12. Үгсийг **богиноос урт руу** эрэмбэл. Ижил урттай үгс 
#     байвал **цагаан толгойн дарааллаар** байрлуул.
# def sort_words(words):
#         if len(words) <= 1:
#                 return words
#         mid = len(words) // 2
#         left = words[:mid]
#         right = words[mid:]

#         left = sort_words(left)
#         right = sort_words(right)

#         result=[]
#         i=0
#         j=0

#         while i < len(left) and j < len(right):
#                 if len(left[i]) < len(right[j]) or (left[i]) == len(right[j]):
#                         result.append(left[i])
#                         i += 1
#                 else:
#                         result.append(right[j])
#                         j += 1
#         while i < len(left):
#                 result.append(left[i])
#                 i += 1
#         while j < len(right):
#                 result.append(right[j])
#                 j += 1
#         return result
# words = list(map(str,input("UGSEE UG: ").split()))
# print(sort_words(words))



# 13. Эрэмбэлэгдээгүй массивыг эхлээд merge sort-оор эрэмбэл.
#     Дараа нь binary search ашиглан өгөгдсөн тоог хай. Олдвол 
#     **эрэмбэлэгдсэн массив дахь индексийг**, олдохгүй бол `-1` буцаа.
# def merge_sort(nums):
#         if len(nums) <= 1:
#                 return nums
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid:]
        
#         left = merge_sort(left)
#         right = merge_sort(right)
#         result=[]
#         i=0
#         j=0
#         while i < len(left) and j < len(right):
#                 if left[i] <= right[j]:
#                         result.append(left[i])
#                         i += 1
#                 else:
#                         result.append(right[j])
#                         j += 1
#         while i < len(left):
#                 result.append(left[i])
#                 i += 1
#         while j < len(right):
#                 result.append(right[j])
#                 j += 1
#         return result

# def binary_search(nums,oloh):
#         nums=merge_sort(nums)
#         left=0
#         right=len(nums)-1
#         while left <= right:
#                 mid=(left+right)//2
#                 if nums[mid] == oloh:
#                         print("HAIJ BUI TOO OLDLOO:" ,f"INDEX NI:  {mid}")
#                         break
#                 elif nums[mid] < oloh:
#                         left = mid+1
#                 else:
#                         right = mid-1
#         return  -1


# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# oloh=int(input("OLOH TOOGOO UG: "))
# print(f"EREMBELEGDSEN JAGSAALT: {merge_sort(nums)}")
# print(binary_search(nums,oloh))



# 14. Хоёр үг өгөгдөнө. Хоёр үг ижил үсгүүдээс бүтсэн 
#     (зөвхөн дараалал нь өөр) бол `True`, үгүй бол `False` буцаа.
#     Үг бүрийн үсгүүдийг merge sort-оор эрэмбэлээд харьцуул.
# def merge_sort(words):
#         if len(words) <= 1:
#                 return words
#         mid = len(words)//2
#         left = words[:mid]
#         right = words[mid:]
        
#         left = merge_sort(left)
#         right = merge_sort(right)
#         result=[]
#         i=0
#         j=0

#         while i < len(left) and j < len(right):
#                 if left[i] <= right[j]:
#                         result.append(left[i])
#                         i += 1
#                 else:
#                         result.append(right[j])
#                         j += 1
#         while i < len(left):
#                 result.append(left[i])
#                 i += 1
#         while j < len(right):
#                 result.append(right[j])
#                 j += 1
#         return result
# def is_anagram(word1,word2):
#         if word1==word2:
#                 return True
#         return False

# word1=input("EHNII UGEE UG: ")
# word2=input("NEXT UGEE UG: ")
# print(is_anagram(word1,word2))

   
