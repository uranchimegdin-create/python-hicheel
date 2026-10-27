# SELECTION.SORT AJILLAH ALHAM:

# numbers=[5,3,8,1,2]
# for i in range(len(numbers)-1):
#     min_index=i
#     for j in range(i+1,len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j
#     temp = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = temp
#     print(numbers)



# 1. Selection Sort ашиглан жагсаалтыг өсөх дарааллаар эрэмбэл.
# numbers = list(map(int,input("TOONUUDAA UG: ").split())) [ 1, 2 , 3 , 42 , 5]
# for i in range(len(numbers)-1):
#     min_index = i
    # for j in range(i+1 , len(numbers)): 
#         if numbers[j] < numbers[min_index]:
#             min_index = j
#     too = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = too
# print(numbers)



# 2. Selection Sort ашиглан хамгийн бага 3 тоог жагсаалтын эхний 
#    3 байрлалд өсөх дарааллаар байрлуул. Үлдсэн тоонуудыг заавал эрэмбэлэх шаардлагагүй.
# numbers = list(map(int,input("toogoo ug: ").split()))
# for i in range(3):
#     min_index = i
#     for j in range(i+1 , len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j
#     too = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = too
#     print(numbers)



# 3. Selection Sort ашиглан жагсаалтыг буурах дарааллаар эрэмбэл.
# numbers = list(map(int,input("TOONUUDAA UG: ").split()))
# for i in range(len(numbers)-1):
#     min_index = i
#     for j in range(i+1 , len(numbers)):
#         if numbers[j] > numbers[min_index]:
#             min_index = j
#     too = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = too
# print(numbers)


# 4. Selection Sort ашиглан жагсаалтыг өсөх дарааллаар эрэмбэл.
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     min_index = i
#     for j in range(1+i, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     too = nums[i]
#     nums[i] = nums[min_index]
#     nums[min_index] = too
# print(nums)



# 5. Жагсаалтын давхардсан тоонуудыг арилгаж, үлдсэн тоонуудыг 
#    Selection Sort ашиглан өсөх дарааллаар эрэмбэл.
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     min_index = i
#     for j in range(1+i, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     too = nums[i]
#     nums[i] = nums[min_index]
#     nums[min_index] = too
# print(f"EREMBELEVEL: {nums}")
# b=set(nums)
# print(f"DAVHARDSAN UTGA ARILGAVAL: {b}")



# 6. Selection Sort-ийн эхний алхмын дараа жагсаалт ямар болсон байх вэ?
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     min_index = i
#     for j in range(1+i, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     too = nums[i]
#     nums[i] = nums[min_index]
#     nums[min_index] = too
#     break
# print(nums)



# 7. Selection Sort-ийн эхний алхмын дараах жагсаалтыг ол.
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     min_index = i
#     for j in range(1+i, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     too = nums[i]
#     nums[i] = nums[min_index]
#     nums[min_index] = too
#     break
# print(nums)



# 8. Selection Sort-ийн эхний хоёр алхмын дараах жагсаалтыг ол.
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# for i in range(2):
#     min_index = i
#     for j in range(1+i, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     too = nums[i]
#     nums[i] = nums[min_index]
#     nums[min_index] = too
# print(nums)




# 9. Өсөх дарааллаар эрэмбэлэхэд Selection Sort хэдэн удаа хоёр өөр 
#    байрлал дахь утгыг солих вэ? Нэг байрлал дахь утгыг өөртэй нь солихыг тооцохгүй.
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# count=0
# for i in range(len(nums)-1): 
#     min_index = i
#     for j in range(1+i, len(nums)):
#         if nums[j] < nums[min_index]:
#             min_index = j
#     if min_index != i:
#         too = nums[i]
#         nums[i] = nums[min_index]
#         nums[min_index] = too
#         count+=1
#     print(nums)
# print(count)



# 10. Дээрх гурван жагсаалтаас өсөх дарааллаар аль хэдийн эрэмбэлэгдсэн жагсаалтыг ол.
# def selection(list):
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             return False
#     return True
# a = [2, 4, 1, 5, 3]
# b = [1, 2, 3, 4, 5]
# c = [3, 1, 2, 5, 4]

# print(f"a: {selection(a)}\nb: {selection(b)}\nc: {selection(c)}")





# 11. selection_sort(arr)  нэртэй функц бич. Функц нь
#     жагсаалтыг өсөх дарааллаар эрэмбэлдэг байна.
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(1+i, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         too = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = too
#     return arr
# numbers=list(map(int,input("TOONUUDAA UG: ").split()))
# print(selection_sort(numbers))



# 12. selection_sort_desc(arr)` нэртэй функц бич. Функц нь 
#     жагсаалтыг буурах дарааллаар эрэмбэлдэг байна
# def selection_sort(arr):
#     for i in range(len(arr)-1):
#         min_index = i
#         for j in range(1+i, len(arr)):
#             if arr[j] > arr[min_index]:
#                 min_index = j
#         too = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = too
#     return arr
# numbers=list(map(int,input("TOONUUDAA UG: ").split()))
# print(selection_sort(numbers))



# 13. Selection Sort-ийн эхний алхамд хамгийн бага элементийн
#     индексийг олж хэвлэх код бич.
# nums=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# min_index = 0
# for j in range(1, len(nums)):
#     if nums[j] < nums[min_index]:
#         min_index = j
# print(min_index)


# 14. Selection Sort ашиглан жагсаалтыг өсөх дарааллаар эрэмбэл. 
#     Алхам бүрийн дараа жагсаалтын төлөвийг хэвлэдэг код бич.
# nums=list(map(int,input("TOOGOO UG: ").split(",")))
# for i in range(len(nums)-1):
#     min_idx = i
#     for j in range(i+1, len(nums)):
#         if nums[j] < nums[min_idx]:
#             min_idx = j
#     too = nums[i]
#     nums[i] = nums[min_idx]
#     nums[min_idx] = too
#     print(nums)


# 15. Нэг жагсаалтыг Bubble Sort, нөгөөг нь Selection Sort 
#     ашиглан өсөх дарааллаар эрэмбэл. Хоёр алгоритмын эцсийн үр дүн ижил 
#     эсэхийг шалгадаг код бич.
# nums=list(map(int,input("TOONUUDAA UG: ").split(",")))
# for i in range(len(nums)-1):
#     for j in range(len(nums)-1 -i):
#         if nums[j] > nums[j+1]:
#             a=nums[j]
#             nums[j] = nums[j+1]
#             nums[j+1] = a
# print(nums)

# numbers=list(map(int,input("TOOMUUDAA UG: ").split(",")))
# for i in range(len(numbers)-1):
#     min_index = i
#     for j in range(1+i, len(numbers)):
#         if numbers[j] < numbers[min_index]:
#             min_index = j
#     too = numbers[i]
#     numbers[i] = numbers[min_index]
#     numbers[min_index] = too
# print(numbers)

# if nums == numbers:
#     print("VR DVN IJIL")
# else:
#     print("IJIL BISH")



