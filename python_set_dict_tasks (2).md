# Python Set ба Dictionary — Дасгалууд

## I. Set дасгалууд

### 1. Давхардлыг арилгах
Өгөгдсөн жагсаалтаас давхардсан утгуудыг арилгаж, set хэлбэрээр хэвлэ.

```python
nums = [1, 2, 2, 3, 4, 4, 5]
```

Хүлээгдэж буй утгууд:

```text
{1, 2, 3, 4, 5}
```

---

### 2. Жимс нэмэх
Доорх set-д `"orange"` утгыг нэмээд хэвлэ.

```python
fruits = {"apple", "banana"}
```

---

### 3. Утга устгах
Доорх set-ээс `"banana"` утгыг устга.

```python
fruits = {"apple", "banana", "orange"}
```

---

### 4. Байгаа эсэхийг шалгах
Доорх set дотор `20` байгаа эсэхийг шалга.

```python
nums = {10, 20, 30, 40}
```

Байвал:

```text
YES
```

Үгүй бол:

```text
NO
```

гэж хэвлэ.

---

### 5. Хэдэн ялгаатай тоо байна вэ?
Хэрэглэгчээс 5 ширхэг бүхэл тоо авч, хэдэн ялгаатай тоо оруулсныг хэвлэ.

Жишээ:

```text
Input:
1 2 2 3 3

Output:
3
```

---

### 6. Давхардсан нэрс
Доорх жагсаалтад хэдэн өөр нэр байгааг ол.

```python
names = ["Bat", "Sara", "Bat", "Bold", "Sara", "Anu"]
```

---

### 7. Хоёр set-ийг нэгтгэх
Доорх хоёр set-ийн бүх утгыг давхардалгүйгээр нэг set болго.

```python
a = {1, 2, 3}
b = {3, 4, 5}
```

---

### 8. Ижил утгуудыг олох
Доорх хоёр set-д хоёуланд нь байгаа утгуудыг ол.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

---

### 9. Зөвхөн эхний set-д байгаа утгууд
Доорх `a` set-д байгаа боловч `b` set-д байхгүй утгуудыг хэвлэ.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

---

### 10. Хоёр хичээл хоёуланг нь сурдаг сурагчид
Python сурдаг сурагчид:

```python
python_students = {"Bat", "Sara", "Bold", "Anu"}
```

Java сурдаг сурагчид:

```python
java_students = {"Sara", "Bold", "Temuulen"}
```

Хоёр хичээл хоёуланг нь сурдаг сурагчдыг ол.

---

### 11. Зөвхөн нэг хичээл сурдаг сурагчид
Дээрх `python_students`, `java_students` set-үүдийг ашигла.

Зөвхөн нэг хичээлд байгаа сурагчдыг ол.

---

### 12. Оруулсан үсгүүд
Хэрэглэгчээс нэг үг ав. Тухайн үгэнд хэдэн өөр үсэг байгааг set ашиглан ол.

Жишээ:

```text
Input:
banana

Output:
3
```

Учир нь:

```text
b, a, n
```

гэсэн 3 өөр үсэг байна.

---

## II. Dictionary дасгалууд

### 13. Сурагчийн мэдээлэл
Доорх мэдээллээр `student` нэртэй dictionary үүсгэ.

- name: Bat
- age: 18
- score: 95

Dictionary-г бүхэлд нь хэвлэ.

---

### 14. Нэрийг хэвлэх
Доорх dictionary-с зөвхөн сурагчийн нэрийг хэвлэ.

```python
student = {
    "name": "Sara",
    "age": 19,
    "score": 90
}
```

---

### 15. Оноог өөрчлөх
Доорх dictionary-ийн `score` утгыг `98` болго.

```python
student = {
    "name": "Bat",
    "age": 18,
    "score": 85
}
```

---

### 16. Шинэ мэдээлэл нэмэх
Доорх dictionary-д:

```python
"city": "Ulaanbaatar"
```

гэсэн шинэ мэдээлэл нэм.

```python
student = {
    "name": "Anu",
    "age": 18
}
```

---

### 17. Мэдээлэл устгах
Доорх dictionary-с `age` мэдээллийг устга.

```python
student = {
    "name": "Bold",
    "age": 20,
    "score": 88
}
```

---

### 18. Key-үүдийг хэвлэх
Доорх dictionary-ийн бүх key-г хэвлэ.

```python
car = {
    "brand": "Toyota",
    "model": "Prius",
    "year": 2015
}
```

---

### 19. Value-уудыг хэвлэх
Доорх dictionary-ийн бүх value-г хэвлэ.

```python
car = {
    "brand": "Toyota",
    "model": "Prius",
    "year": 2015
}
```

---

### 20. Key болон value-г хамтад нь хэвлэх
`items()` болон `for` ашиглан:

```python
student = {
    "name": "Bat",
    "age": 18,
    "score": 95
}
```

dictionary-ийн key, value бүрийг дараах хэлбэрээр хэвлэ.

```text
name Bat
age 18
score 95
```

---

### 21. Key байгаа эсэх
Доорх dictionary-д `"score"` гэсэн key байгаа эсэхийг шалга.

```python
student = {
    "name": "Sara",
    "age": 19,
    "score": 92
}
```

Байвал:

```text
YES
```

Үгүй бол:

```text
NO
```

---

### 22. Барааны мэдээлэл
Доорх dictionary байна.

```python
product = {
    "name": "Keyboard",
    "price": 120000,
    "stock": 5
}
```

Хэрэв `stock` нь `0`-ээс их бол:

```text
Available
```

үгүй бол:

```text
Out of stock
```

гэж хэвлэ.

---

### 23. Сурагчдын оноо
Доорх dictionary өгөгдөнө.

```python
scores = {
    "Bat": 80,
    "Sara": 95,
    "Bold": 70,
    "Anu": 88
}
```

`80`-аас дээш оноотой сурагчдын нэрийг хэвлэ.

---

### 24. Хамгийн өндөр оноо
Доорх dictionary-с хамгийн өндөр оноотой сурагчийн нэр болон оноог ол.

```python
scores = {
    "Bat": 80,
    "Sara": 95,
    "Bold": 70,
    "Anu": 88
}
```

---

### 25. Dictionary-ийн бүх value-ийн нийлбэр
Доорх dictionary-ийн бүх value-ийн нийлбэрийг ол.

```python
sales = {
    "Monday": 10,
    "Tuesday": 15,
    "Wednesday": 20
}
```

Хүлээгдэж буй output:

```text
45
```

---

### 26. Үгийн давтамж
Хэрэглэгчээс өгүүлбэр ав.

Өгүүлбэрт орсон үг бүр хэдэн удаа давтагдсаныг dictionary ашиглан тоол.

Жишээ:

```text
Input:
cat dog cat bird dog cat
```

Output ойролцоогоор:

```text
cat 3
dog 2
bird 1
```

---

## III. Set + Dictionary хосолсон дасгалууд

### 27. Давхардалгүй хичээлүүд
Доорх dictionary-д сурагч бүрийн сонгосон хичээлүүд байна.

```python
students = {
    "Bat": ["Python", "Java"],
    "Sara": ["Python", "C++"],
    "Bold": ["Java", "Python"]
}
```

Бүх сурагчдын сонгосон **өөр өөр хичээлүүдийг** set ашиглан ол.

Хүлээгдэж буй утгууд:

```text
Python
Java
C++
```

---

### 28. Хэдэн өөр хот байна вэ?
Доорх dictionary-д сурагчдын хот байна.

```python
students = {
    "Bat": "Ulaanbaatar",
    "Sara": "Darkhan",
    "Bold": "Ulaanbaatar",
    "Anu": "Erdenet",
    "Temuulen": "Darkhan"
}
```

Хэдэн өөр хот байгааг set ашиглан ол.

---

### 29. Нэг хотод амьдардаг сурагчид
Доорх dictionary ашиглан `"Ulaanbaatar"` хотод амьдардаг сурагчдын нэрийг хэвлэ.

```python
students = {
    "Bat": "Ulaanbaatar",
    "Sara": "Darkhan",
    "Bold": "Ulaanbaatar",
    "Anu": "Erdenet"
}
```

---

### 30. Давхардалгүй утгуудтай dictionary
Доорх dictionary-ийн value-уудыг set болгон хувиргаад хэвлэ.

```python
data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20
}
```

Хүлээгдэж буй утгууд:

```text
{10, 20, 30}
```

---

# Санамж

## Set дээр голчлон ашиглах зүйлс

```python
set()
add()
remove()
discard()
clear()
union()
intersection()
difference()
symmetric_difference()
```

Мөн:

```python
|
&
-
^
```

operator-уудыг ашиглаж болно.

## Dictionary дээр голчлон ашиглах зүйлс

```python
dict()
keys()
values()
items()
get()
pop()
```

Мөн dictionary-ийн утгыг:

```python
data["key"]
```

хэлбэрээр авч болно.
