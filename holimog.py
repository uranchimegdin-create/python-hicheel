# HOLIMOG BODLOGONUUUD...

# 1.  Бүхэл тоо уншаад эерэг/сөрөг, тэгш/сондгой эсэхийг хэвлэ. 0 бол Тэг гэж хэвлэ.
# n=int(input("SHALGAH TOOGOO UG: "))
# if n == 0:
#     print("TEG")
# else:
#     if n > 0:
#         print("EYREG")
#     else:
#         print("SOROG")
#     if n //2==0:
#         print("TESGH")
#     else:
#         print("SONDGOI")



# 2. 0–100 оноо уншаад үнэлгээг хэвлэ: A (90–100), B (80–89), C (70–79), D (60–69),
#    F (0–59). Оноо 0-ээс бага эсвэл 100-аас их бол Буруу оноо гэж хэвлэ.
# s=int(input("ONOO UG: "))
# if s >= 90 and s<=100:
#     print("A")
# elif s >=80 and s <=89:
#     print("B")
# elif s >= 70 and s <= 79:
#     print("C")
# elif s >= 60 and s <=69:
#     print("D")
# elif s >=0 and s <=59:
#     print("F")
# else:
#     print("BURUU ONOO")



# 3. Он уншаад өндөр жил мөн эсэхийг хэвлэ. Он 4-т хуваагддаг ба
#    100-д хуваагддаггүйбол, эсвэл 400-д хуваагддаг бол өндөр жил.
# n=int(input("SHALGAH ON ORUUL: "))
# if n % 4 ==0 and n % 100 !=0 or n % 400 == 0:
#     print("UNDUR JIL MUN")
# else: 
#     print("ENGIIN JIL BNA")



# 4. Гурвалжны 3 талын уртыг уншина. Аль нэг хоёр талын нийлбэр гурав дахь талаасаа их
#    биш бол Гурвалжин үүсэхгүй. Үгүй бол Тэгш талт, Адил хажуут эсвэл Энгийн гэж хэвлэ.
# a=int(input("A TAL: "))
# b=int(input("B TAL: "))
# c=int(input("C TAL: "))
# if a == b ==c:
#     print("TEGSH TALT GURVALJIN")
# elif a == b >c or a == b <c or a == c <b or a==c>b or b==c>a or b==c <a:
#     print("ADIL HAJUUT GURVALJIN")
# elif a+b<c or a+c<b or c+b<a:
#     print("GURVALJIN UUSEHGUI")
# else:
#     print("ENGIIN GURVALJIN")



# 5. Эхний 2 км 3000₮, түүнээс хойшх км бүр 1500₮. Шөнийн цагаар (22:00–05:59) 
#    нийт дүн дээр 2000₮ нэмэгдэнэ. Км (бүхэл тоо) ба цаг (0–23) уншаад төлбөрийг хэвлэ.
# km=int(input("KM UG: "))
# tsag=int(input("TSAG UG: "))
# if tsag < 22 and tsag >6: 
#     if km <= 2:
#         print(3000)
#     else:
#         print(km*1500)
# elif tsag >=22 and tsag <= 24 or tsag >= 0 and tsag <=6:
#     print(km*1500+2000)



# 6. n уншаад 1-ээс n хүртэлх тэгш тоонуудын нийлбэрийг for давталтаар ол
# total=0
# n=int(input("TOOGOO UG: "))
# for i in range(1,n+1):
#     if i % 2==0:
#        total+=i
# print(total)



# 7. Эерэг бүхэл тоо уншаад цифрүүдийнх нь нийлбэрийг
#    while давталтаар ол. str() ашиглахгүй.
# total=0
# n=int(input("TOOGOO UG: "))
# while n > 0:
#     b=n%10
#     total += b
#     n=n//10
# print(total)



# 8. Эерэг бүхэл тоог while давталтаар урвуулж хэвлэ. str() ашиглахгүй.
# n=int(input("TOOGOO UG: "))
# a=[]
# total=0
# while n > 0:
#     b=n%10
#     a.append(b)
#     n=n//10
# for i in a:
#     total=total *10+i
# print(total)



# 9. 1-ээс n хүртэлх тоог нэг мөрөнд зайгаар тусгаарлаж хэвлэ. 3-т хуваагдвал 
#    тооны оронд Физ, 5-д хуваагдвал Базз, хоёуланд нь хуваагдвал ФизБазз гэж хэвлэ.
# n=int(input("TOOGOO UG: "))
# for i in range(1,n+1):
#     if i %3==0 and i % 5 ==0:
#         print("PIZBAZZ",end=" ")
#         continue
#     if i % 3==0:
#         print("PIZ",end=" ")
#         continue
#     if i % 5 ==0:
#         print("BAZZ",end=" ")
#         continue
#     else:
#         print(i,end=" ")



# 10. Програмдаа secret = 37 гэж нууц тоо хадгал. Хэрэглэгч зөв таах хүртэл тоо уншиж, Их байна эсвэл Бага байна гэж хэвлэ. 
# Зөв таавал хэдэн оролдлогоор таасныг хэвлэ.
# secret=int(input("OLOH YSTOI TOO: "))
# count=0
# while secret > 0:
#     n=int(input("TAAJ BUI TOO: "))
#     count += 1
#     if n >secret:
#         print("IH BNA")
#     elif n<secret:
#         print("BAGA BNA")
#     else:
#         print(f"ZOW BAINA: {count} OROLDLOGOOR TAALAA.")
#     if count >=5:
#         print(f"BOLOMJIT {count} OROLDLOGO DUUSLAA,YLAGDLAA.")
#         break




# 11.  n уншаад n × n хэмжээтэй үржүүлэх хүснэгтийг хэвлэ. Тоонуудыг зайгаар тусгаарла.
# n=int(input("TOOGOO ORUUL: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j,end=" ")
#     print()


# 12. n мөртэй пирамид хэвлэ. i-р мөрөнд эхлээд n − i зай, дараа нь 2i − 1 од байна.
# n=int(input("HEDEN MUR?: "))
# for i in range(1,n+1):  
#     print(" "*(n-i),end=" ")
#     print("*"*((2*i)-1))
    

# 13. Даалгавар: Нийлбэр нь target болох бүх хосыг (arr[i], arr[j]) 
#     tuple хэлбэрээр, i < j байхаар, олдсон дарааллаар нь буцаа.
# def find_pairs(nums,target):
#     result=[]
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j]==target:
#                 result.append((nums[i],nums[j]))
#     return result
# nums=list(map(int,input("JAGSAALTAA UG: ").split(",")))
# target=int(input("NIILBER BOLOH HOS TOO UG: "))
# print(find_pairs(nums,target))

        
# 14. Хамгийн олон давтагдсан тоо болон давтамжийг (тоо, давтамж) хэлбэрээр буцаа. Давтамж 
#     тэнцүү бол жагсаалтад түрүүлж орсныг нь сонго. dict ашиглахгүй, давхар давталтаар шийд.
# def most_frequent(nums):
#     olon_too=nums[0]
#     ih_davtamj=0 
#     for i in range(len(nums)):
#         davtamj=0
#         for j in range(len(nums)):
#             if nums[i] == nums[j]:
#                 davtamj += 1
#         if davtamj > ih_davtamj:
#             ih_davtamj = davtamj
#             olon_too = nums[i]
#     return (olon_too,ih_davtamj)
# nums=list(map(int,input("JAGSAALT UG: ").split(",")))
# print(most_frequent(nums))



# 15. 2 хэмжээст жагсаалтын мөр бүрийн болон багана 
#     бүрийн нийлбэрийг (мөрүүд, баганууд) хэлбэрээр буцаа.
def row_col_sums(matrix):
    for i in range(n+1):
        for j in i:
            
            





