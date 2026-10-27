# class player:
#     def __init__(self, name , skins):
#         self.name = name
#         self.skins = skins
# player1 = player("tsedo",1)
# player2 = player("fenrir",1)

# print(player1.name)
# print(player1.skins)

# print(player2.name)
# print(player2.skins)


# TASKKKSSSSSSSSSSSSSSSSSSSS
# 2.  Student` гэсэн class ашиглан хоёр сурагч үүсгээрэй.
#     - Эхний сурагч: **Нараа**, 17 настай
#     - Хоёр дахь сурагч: **Тэмүүлэн**, 19 настай
# class students:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# students1 = students("NARAA",17)
# students2 = students("TEMUULEN",19)

# print(students1.name)
# print(students1.age)

# print(students2.name)
# print(students2.age)


# 3. `Student` class-д `name`, `age`, `grade` гэсэн 3 мэдээлэл хадгалдаг болгоорой.
# class students:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
# students1 = students("BATA",17,"12B")

# print(students1.name)
# print(students1.age)
# print(students1.grade)



# 4. `Student` class-д сурагчийн нэр болон оноог хадгалдаг болгоорой.
# class students:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
# students1 = students("BAT",85)
# students2 = students("SARAA",95)

# print(students1.name)
# print(students1.score)
# print(students2.name)
# print(students2.score)



# 5.  Student` class ашиглан сурагчийн оноог хадгална.
#     Сурагчийн оноонд `5` оноо нэмдэг `add_score()` нэртэй method бичээрэй.
# class students:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5

# students1 = students("BATAA",80)
# students1.add_score()
# print(students1.name)
# print(students1.score)




# 6.  Student` class дотор `show_info()` нэртэй method бичээрэй.
#     Энэ method нь сурагчийн нэр, нас, ангийг хэвлэнэ.
# class student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         print(f"NER: {student1.name}\nNAS: {student1.age}\nANGI: {student1.grade}")
# student1 = student("SARAA",19,"12B")
# student1.show_info()




# 6.  Student` class дотор `show_info()` нэртэй method бичээрэй.
#     Энэ method нь сурагчийн нэр, нас, ангийг хэвлэнэ.
# class students:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         students.show_info()
# students1 = students("SARAA",19,"12B")
# print(f"NER: {students1.name}")
# print(f"NAS: {students1.age}")
# print(f"ANGI: {students1.grade}")




# 7.  Student` class нь сурагчийн нэр, шалгалтын оноог хадгална.
#    `check_result()` нэртэй method бичээрэй.
# class students:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60:
#             print(f"{self.name}: TENTSSEN")
#         else:
#             print(f"{self.name}: TENTSEEGUI")
# students1 = students("BAT",75)
# students2 = students("NARAA",45)

# students1.check_result()
# students2.check_result()


# 8.  Student` class нь сурагчийн нэр, оноог хадгална.
#    `add_score()` method нь сурагчийн оноог 5-аар нэмэгдүүлдэг байна
# class students:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5

# students1 = students("BATAA",80)
# students1.add_score()
# print(students1.name)
# print(students1.score)


# 9.  Student` class дотор `birthday()` method бичээрэй.
#     Уг method дуудагдах бүрд сурагчийн нас 1-ээр нэмэгдэнэ.
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age += 1
# student1 = student("SARAA",18)
# student1.birthday()
# student1.birthday()
# student1.birthday()
# print(student1.age)



# 10.   Student` class нь сурагчийн нэр, оноог хадгална.
#      `get_grade()` method бичээрэй. Method нь тохирох үнэлгээг хэвлэнэ.
# class student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if 90 <= self.score <= 100:
#             print(f"{self.name}: A")
#         elif 80 <= self.score <=89:
#             print(f"{self.name}: B")
#         elif 70 <= self.score <=79:
#             print(f"{self.name}: C")
#         elif 60 <= self.score <= 69:
#             print(f"{self.name}: D")
#         else:
#             print(f"{self.name}: F")
# student1 = student("BAT",97)
# student2 = student("SARA",84)
# student1.get_grade()
# student2.get_grade()


# 11.  Student` class нь сурагчийн нэр, ирцийн тоог хадгална.
#      - Эхний ирцийн тоо `0` байна.
#      - attend()` method дуудагдах бүрд ирц 1-ээр нэмэгдэнэ.
#      - show_attendance()` method ирцийн тоог хэвлэнэ.
# class student:
#     def __init__(self,ner,irts):
#         self.ner = ner 
#         self.irts = irts
#     def attend(self):
#         self.irts += 1
#     def show_attendance(self):
#         print(f"{self.ner} IRTS NI: {self.irts}")
# student1 = student("BATAA",0)
# student2 = student("SARAA",0)
# student1.attend()
# student1.attend()
# student1.attend()
# student2.attend()
# student2.attend()    

# student1.show_attendance()
# student2.show_attendance()



# 12.  Student` class нь сурагчийн нэр, шалгалтын оноо, ирцийн хувийг хадгална.
#    ` check_result()` method дараах нөхцөлийг шалгана.
# class student:
#     def __init__(self,ner,onoo,irts):
#         self.ner = ner 
#         self.onoo = onoo
#         self.irts = irts
#     def check_result(self):
#         if self.onoo >= 60:
#             if self.irts >= 80:
#                 print(f"{self.ner}: TENTSSEN")
#             else:
#                 print(f"{self.ner}: TENTSEEGUI")
#         else:        
#             print("OGT TENTSEEGUI")
# student1 = student("BAT",85,90)
# student2 = student("SARAA",60,75)
# student1.check_result()
# student2.check_result()



# 13.