# 1.
# name=input()
# print("Sain uu,",name)


# 2.Хоёр мөрөнд өгсөн бүхэл тоонуудын нийлбэрийг хэвлэ.
# a=int(input())
# b=int(input())
# print(a+b)


# 3.Нэг барааны үнийг бутархай тоогоор унш. Ижил хоёр барааны нийт үнийг `Нийт үнэ: <дүн>` хэлбэрээр хэвлэ. (`float`, `str`)
# a=float(input())
# print("dvn",a*2)


# 4.Нэг бүхэл тооны бичвэрийг унш. Хөрвүүлэхээс өмнөх, дараах төрлийг тус бүр шинэ мөрөнд хэвлэ.
# too=input()
# print(type(too))
# print(type(int(too)))


# 5.Өгүүлбэрийн бүх тэмдэгтийг, дундах зайг оруулаад, тоол. (`len`)
# a=input()
# print(len(a))


# 6.Хоосон биш үгийн эхний болон сүүлийн тэмдэгтийг тус бүр шинэ мөрөнд хэвлэ. (`[]`)
# ug=input()
# print(ug[0])
# print(ug[-1])


# 7.`n` бүхэл тоог уншаад 1-ээс `n` хүртэлх бүх тоог тус бүр шинэ мөрөнд хэвлэ. `n` нь эерэг. (`range`)
# n=int(input())
# for i in range(1,n+1):
#     print(i)


# 8.Нэг мөрөнд зайгаар тусгаарласан бүхэл тоонуудын нийлбэрийг ол. (`split`, `append`, `sum`)
# a=list(map(int,input().split()))
# print(sum(a))


# 9.Нэг мөрийн тоонуудаас хамгийн бага, хамгийн их утгыг нэг мөрөнд энэ дарааллаар хэвлэ
# a=list(map(int,input().split()))
# print(min(a),end=" ")
# print(max(a))



# 10.Нэг мөрөнд өгсөн бүхэл оноонуудын дунджийг бутархайн ард хоёр орноор **тооцоолж** 
# тоймло. (`sum`, `len`, `round`)
# a=list(map(int,input().split()))
# b=(sum(a)/len(a))
# print(round(b,2))


# 11.Эхний мөрийн амьтдын нэрийг list болгоод хоёр дахь мөрийн нэрийг төгсгөлд нь нэм. 
# List-ийг хэвлэ. (`split`, `append`)
# a=input().split() # a gdg variable ruu olon utga split eer tusgaarlan ugugduj bainaa
# b=input()
# a.append(b)
# print(a)


# 12.Эхний мөрийн нэрсийг list болгоод хоёр дахь мөрийн нэрийг 1-р индекст оруул. (`insert`)
# a=input().split()
# b=input()
# a.insert(1,b)
# print(a)


# 13.Эхний мөрийн нэрсээс хоёр дахь мөрийн утгатай таарах **эхний** элементийг
# устгаад list-ийг хэвлэ. (`remove`)
# a=input().split()
# b=input()
# a.remove(b)
# print(a)

# 14.Эхний мөрөнд нэрс, хоёр дахь мөрөнд устгахэлементийн индексөгөгдөнө.Устгасан 
# нэрийг хэвлэ. Үлдсэн нэрсийг таслалаар нийлүүлээд дараагийн мөрөнд хэвлэ. (`pop`, `join`)
# name=input().split()
# index=int(input())
# remove=name.pop(index)
# print(remove)
# print(name)


# 15.Тоонуудыг эхлээд өсөх, дараа нь буурах дарааллаар хоёр мөрөнд 
# list хэлбэрээр хэвлэ. (`sort`)
# a=list(map(int,input().split()))
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)


# 16.Тоон list-ийн одоогийн дараалал урвуулж хэвлэ.Хэмжээгээр нь эрэмбэлэхгүй. (`reverse`)
# a=list(map(int,input().split()))
# a.reverse()
# print(a)


# 17.ZAHIIN ZAI ARILGAGAGA!
# x="   hello   "
# print(x.strip())
# print(x.lstrip())
# print(x.rstrip())


# 18.Өгүүлбэр хэдэн үгтэйг ол. Үгс зайгаар тусгаарлагдсан. (`split`, `len`)
# text=input().split()
# print(len(text))


# 19.Эхний мөрийн текстэд хоёр дахь мөрийн **нэг үсэг** хэдэн удаа орсныг том,
# жижиг үсгийг ялгалгүй тоол. (`lower`, `count`)
# text=("BaNaNa")
# print(text.count("a"))


# 20.
# text=input() # banana
# ol=input() # na
# a=text.find(ol) # banana na na
# if ol in text:
#     print("oldson")
#     print(a)
# else:
#     print("oldsongui!")
#     print(a)


# 21.Нэг мөрийн файлын нэрсээс `report` гэж эхэлж, `.pdf` гэж төгссөн 
#    нэрсийг тус бүр шинэ мөрөнд хэвлэ. Нэг ч таарахгүй бол `Олдсонгүй` 
#    гэж хэвлэ. (`startswith`, `endswith`)
# a=input().split()
# for i in a:
#     if i.startswith("report") and i.endswith(".pdf"):
#         print(i)
#     else:
#         print("oldsongui!")



# 22.Эхний мөрөнд өгүүлбэр, хоёр дахь мөрөнд хуучин үг, гурав дахьмөрөнд шинэ үг 
# өгөгдөнө. Хуучин үгийн **бүх тохиолдлыг** соль. Хуучин үг хоосон биш. (`replace`)
# oguulber=("Python surch bna.Python goy")
# oguulber=oguulber.replace("Python","JS")
# print(oguulber)


# 23.Эхний мөрөнд зайгаар тусгаарласан нэрс, хоёр дахь мөрөнд хайх нэг нэр өгөгдөнө. 
# Том, жижиг үсгийг ялгахгүйгээр шалга. Байвал `YES`, байхгүй бол `NO` хэвлэ. (`lower`, `split`, `in`)
# names=input().lower().split()
# search=input().lower()
# if search in names:
#     print("YES")
# else:
#     print("NO")


# 24.Хамгийн багадаа зургаан тэмдэгттэй үгийн эхний гурав, сүүлийн
#    гурван тэмдэгтийг хоёр мөрөнд хэвлэ. (`[:]`)
# vg=input()
# print(vg[:3])
# print(vg[-3:])


# 25.Үгийн хоёр захын зайг арилгаж, жижиг үсэг болгон урвуулахад өөртэйгөө 
#    ижил байвал `YES`, үгүй бол `NO`хэвлэ. (`strip`, `lower`, `[::-1]`)
# vg=input()
# vg=vg.strip()
# vg=vg.lower()
# if vg==vg[::-1]:
#     print("YES")
# else:
#     print("NO")

# 26.Нэг мөрийн үгсээс хамгийн уртыг хэвлэ.

# ners=input().split()
# print(max(ners,key=len))

# 27.Нэр, нас, хот` хэлбэрийн мөр өгөгдөнө. Хэсэг бүрийн хоёр захын зайг арилгаад насыг 
#    1-р нэм. `Нэр | Ирэх жил: <нас> | Хот` хэлбэрээр хэвлэ. (`split`, `strip`, `int`, `str`)
# ugugdul=input().split(",")
# name=ugugdul[0].strip()
# age=int(ugugdul[1].strip())
# city=ugugdul[2].strip()
# print(name,"|IREH JIL: ",age+1, "|",city)


# 28.Нэг мөрийн үгсийг жижиг үсэг болгож, давхардлыг арилгаад цагаан толгойн
#    дарааллаар нэг мөрөнд **зайгаар** тусгаарлан хэвлэ.
#    (`lower`, `split`, `in`, `append`, `sort`, `join`) -->
# a=input().lower().split()
# b=[]
# for a in a:
#     if a not in b:
#         b.append(a)
# b.sort()
# print(",".join(b))        


# 29.Нэг мөрийн тоонуудаас **ялгаатай утгаараа** хоёр дахь ихийг ол.
# too=list(map(int,input().split()))
# a=[]
# for i in too:
#     if i not in a:
#         a.append(i)
# a.sort(reverse=True)
# print(a[1])


# 30.
# suragchid=int(input())
# ner,onoo=


# a=(10,20,30)
# b,c,d=a
# print(b,c,d)
