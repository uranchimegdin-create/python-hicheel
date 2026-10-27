# 1. SET NI DAVHARDSAN UTGA ARILGANA
# a={2 , 3 ,4,2,9,3,10}
# print(set(a))



# 2.
# a={"bat","bold","saraa"}
# b={"bat","naraa","saraa"}
# print(a & b)
# print(a|b)
# print(a-b)
# print(b-a)


# 3.
# a={"name":["TEMUULEN","TSEDO","BAT"],
#    "age": 24}
# print(a["name"][1])


# TASKS...

# 1. Давхардлыг арилгах
# Өгөгдсөн жагсаалтаас давхардсан утгуудыг арилгаж, set хэлбэрээр хэвлэ
# nums = [1, 2, 2, 3, 4, 4, 5]
# print(set(nums))


# 2.Доорх set-д `"orange"` утгыг нэмээд хэвлэ.
# fruits = {"apple", "banana"}
# fruits.add("orange")
# print(fruits)


# 3.Доорх set-ээс `"banana"` утгыг устга.
# fruits = {"apple", "banana", "orange"}
# fruits.remove("banana")
# print(fruits)


# 4.Доорх set дотор `20` байгаа эсэхийг шалга.
# nums = {10, 20, 30, 40}
# if 20 in nums:
#     print("YES")
# else:
#     print("NO")


# 5.Хэрэглэгчээс 5 ширхэг бүхэл тоо авч, хэдэн ялгаатай тоо оруулсныг хэвлэ.
# a = set(map(int, input().split()))
# print(len(a))



# 6.Доорх жагсаалтад хэдэн өөр нэр байгааг ол.
# names = ["Bat", "Sara", "Bat", "Bold", "Sara", "Anu"]
# print(len(set(names)))


# 7.Доорх хоёр set-ийн бүх утгыг давхардалгүйгээр нэг set болго.
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a|b)


# 8.Доорх хоёр set-д хоёуланд нь байгаа утгуудыг ол.
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a & b)


# 9.Доорх `a` set-д байгаа боловч `b` set-д байхгүй утгуудыг хэвлэ.
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a-b)


# 10.Хоёр хичээл хоёуланг нь сурдаг сурагчдыг ол.
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# print(python_students & java_students)


# 11.Дээрх `python_students`, `java_students` set-үүдийг ашигла.Зөвхөн нэг хичээлд байгаа сурагчдыг ол.
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# print(python_students - java_students)
# print(java_students - python_students)


# 12.Хэрэглэгчээс нэг үг ав. Тухайн үгэнд хэдэн өөр үсэг байгааг set ашиглан ол.
# a=set(input())
# print(len(a))


# 13.Доорх мэдээллээр `student` нэртэй dictionary үүсгэ.Dictionary-г бүхэлд нь хэвлэ.
# student={"name": "Bat",
#           "age":18,
#           "score":95,}
# print(student)

# 14.Доорх dictionary-с зөвхөн сурагчийн нэрийг хэвлэ.
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# print(student["name"])


# 15.Доорх dictionary-ийн `score` утгыг `98` болго.
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student["score"] = 98
# print(student)


# 16.Доорх dictionary-д: "city": "Ulaanbaatar" гэсэн шинэ мэдээлэл нэм.
# student = {
#     "name": "Anu",
#     "age": 18
# }
# student["city"]="Ulaanbaatar"
# print(student)


# 17.Доорх dictionary-с `age` мэдээллийг устга.
# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
# del student["age"]
# print(student)


# 18.Доорх dictionary-ийн бүх key-г хэвлэ.
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.keys())


# 19.Доорх dictionary-ийн бүх value-г хэвлэ.
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.values())


# 20.`items()` болон `for` ашиглан: dictionary-ийн key, value бүрийг (name Bat age 18 score 95) хэлбэрээр хэвлэ.
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# for name, score in student.items() :
#     print(name,score)


# 21.Доорх dictionary-д `"score"` гэсэн key байгаа эсэхийг шалга.
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 92
# }
# if student.get("score"):
#     print("YES")
# else:
#     print("NO")


# 22.Доорх dictionary байна. Хэрэв `stock` нь `0`-ээс их бол: Available үгүй бол: Out of stock гэж хэвлэ.
# product = {
#     "name": "Keyboard",
#     "price": 120000,
#     "stock": 5
# }
# if product["stock"] > 0:
#     print("Available")
# else:
#     print("Out of stock")


# 23.Доорх dictionary өгөгдөнө.80`-аас дээш оноотой сурагчдын нэрийг хэвлэ...
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# for name,score in scores.items():
#     if score>=80:
#         print(name, score)
        

# 24.Доорх dictionary-с хамгийн өндөр оноотой сурагчийн нэр болон оноог ол.
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }





# 25.Доорх dictionary-ийн бүх value-ийн нийлбэрийг ол.
# sales = {
#     "Monday": 10,
#     "Tuesday": 15,
#     "Wednesday": 20
# }
# total=sum(sales.values())
# print(total)



# 26.Хэрэглэгчээс өгүүлбэр ав. Өгүүлбэрт орсон үг бүр хэдэн удаа давтагдсаныг dictionary ашиглан тоол.
# text=input().split()
# d={}
# for i in text:
#     if i in d:



# 27.Доорх dictionary-д сурагч бүрийн сонгосон хичээлүүд байна. Бүх сурагчдын сонгосон **өөр өөр хичээлүүдийг** set ашиглан ол.
students = {
    "Bat": ["Python", "Java"],
    "Sara": ["Python", "C++"],
    "Bold": ["Java", "Python"]
}





# 28.Доорх dictionary-д сурагчдын хот байна.Хэдэн өөр хот байгааг set ашиглан ол.
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Temuulen": "Darkhan"
# }
# hotuud=set(students.values())
# print(len(hotuud))


29.Доорх dictionary ашиглан `"Ulaanbaatar"` хотод амьдардаг сурагчдын нэрийг хэвлэ.






