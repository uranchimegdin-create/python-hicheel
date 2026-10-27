# 1.colors` нэртэй tuple-д дараах 3 өнгийг хадгалаад бүтнээр нь хэвлэ.
# colors=('ulaan','nogoon','tsenher')
# print(colors)



# 2.Дараах амьтдаар tuple үүсгэ.
# animals=("nohoi","muur","tuulai","mori")
# print(f"{animals[0]}\n{animals[2]}\n{animals[-1]}")


# 3. 100 гэсэн ганц утгатай tuple үүсгээд төрлийг нь хэвлэ.
# a=(100,)
# print(type(a))


# 4.утгуудыг индекс ашиглан хэвлэ:
# subjects=("math","mongol hel","anglish","python")
# print(f"{subjects[0]}\n{subjects[1]}\n{subjects[-1]}")


# 5. Эхний гурван тоо
# numbers=tuple(map(int,input().split()))
# print(numbers[0:3])


# 6.Сүүлийн гурван тоо
# numbers=tuple(map(int,input().split()))
# print(numbers[-1:-4:-1])


# 7.len()` ашиглан хэдэн жимс байгааг хэвлэ.
# jims=tuple(input().split(","))
# print(len(jims))


# 8.Хамгийн их ба хамгийн бага
# too=tuple(map(int,input().split()))
# print(f"hamgiin ih: {max(too)}\nhamgiin baga: {min(too)}")


# 9.Нийлбэр ба дундаж
# onoo=tuple(map(int,input().split()))
# print(sum(onoo))
# print(sum(onoo)/len(onoo))


# 10.Эрэмбэлэх
# too=tuple(map(int,input().split()))
# print(sorted(too))


# 11. 10-iin Тоо хэдэн удаа байна вэ?
# too=tuple(map(int,input().split()))
# print(too.count(10))


# 12.index()` ашиглан `"жүрж"`-ийн индексийг ол.
# jims=tuple(input().split(","))
# ol=input()
# print(jims.index(ol))


# 13.Хэрэглэгчээс амьтны нэр ав. 
# animals=tuple(input().split(","))
# aw=input()
# if aw in animals:
#         print("bnaaa")
# else:
#     print("bhgueenaaa")


# 14. Сурагчийн мэдээлэл
# student=tuple(map(str,input().split()))
# name,age,angi=student
# print(f"Name:{name}\nAge:{age}\nAngi:{angi}")


# 15.Утгуудыг `x`, `y` хувьсагчдад unpacking хийгээд хэвлэ.
# coordinate=tuple(map(int,input().split(",")))
# x,y=coordinate
# print(f"x={x}\ny={y}")


# 16.Утгуудыг `title`, `author`, `pages` хувьсагчдад задлаад хэвлэ.
# a=tuple(map(str,input().split(",")))
# nom, zohiolch, huudas = a  
# print(f"Nom:{nom}\nZohiolch:{zohiolch}\nHuudas:{huudas}")


# 17.Tuple unpacking ашиглан `a`, `b` хоёрын утгыг соль.
# too=tuple(map(int,input().split()))
# a,b=too
# print(f"a={b},b={a}")


# 18.Эхний утга ба үлдсэн утгууд
numbers=(10,20,30,40,50)





