# Python шалгалт — Алдаа засах 28 бодлого

**Заавар:**  
Сурагч бүр 1 бодлого сугалж авна. Кодыг ажиллуулж, алдааг нь олж засна.  
Зөвхөн syntax алдаа биш, логикийн алдаа ч байж болно.

---

## 1. Хоёр дахь хамгийн их тоо

```python
nums = list(map(int, input().split()))

nums.sort()

print(nums[-1])
```

---s

## 2. Давхардсан тоонуудыг арилгах

```python
nums = list(map(int, input().split()))
result = []

for i in nums:
    if i  in result:
        result.append(i)

print(result)
```

---

## 3. Палиндром эсэх

```python
text = input()

reverse = ""

for i in range(len(text)):
    reverse += text[i]

if text == reverse:
    print("YES")
else:
    print("NO")
```

---

## 4. Хамгийн урт үгийг олох

```python
words = input().split()

longest = words[0]

for word in words:
    if len(word) < len(longest):
        longest = word

print(longest)
```

---

## 5. Эгшгийн тоо

```python
text = input().lower()
vowels = "аэиоуөү"
count = 0

for ch in text:
    if ch not in vowels:
        count += 1

print(count)
```

---

## 6. 1-ээс N хүртэлх тэгш тоонуудын нийлбэр

```python
n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 2 != 0: 
        total += 1

print(total)
```

---

## 7. Тооны цифрүүдийн нийлбэр

```python
n = int(input())
total = 0

while n > 0:
    digit = n % 10
    total = digit
    n //= 10

print(total)
```

---

## 8. Тоог урвуу болгох

```python
n = int(input())
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse + digit
    n //= 10

print(reverse)
```

---

## 9. Анхны тоо шалгах

```python
n = int(input())
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = True
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")
```

---

## 10. List дэх хамгийн бага тоог `min()` ашиглахгүй олох

```python
nums = list(map(int, input().split()))

smallest = 0

for num in nums:
    if num > smallest:
        smallest = num

print(smallest)
```

---

## 11. List дэх тэгш тоонуудын тоо

```python
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if num % 2 == 0:
        count = num

print(count)
```

---

## 12. Хамгийн олон давтагдсан тоог олох

```python
nums = list(map(int, input().split())) 

best = nums[0]
best_count = 0

for num in nums:
    count = nums.count(num)

    if count < best_count:
        best_count = count
        best = num

print(best)
```

---

## 13. Давхардсан үгийн тоо

```python
words = input().split()
target = input()

count = 0

for word in words:
    if word != target:
        count += 1

print(count)
```

---

## 14. List-ийг урвуу хэвлэх

```python
nums = list(map(int, input().split()))

for i in range(len(nums) - 1, 0, -1):
    
    print(nums[i], end=" ")
```

---

## 15. Нийлбэр нь хамгийн их дараалсан 2 тоо

```python
nums = list(map(int, input().split()))

max_sum = 0

for i in range(len(nums)):
    current = nums[i] + nums[i + 1]

    if current > max_sum:
        max_sum = current

print(max_sum)
```

---

## 16. Өгүүлбэрийн үг бүрийг урвуу болгох

```python
words = input().split()
result = []

for word in words:
    result.append(word)

print(" ".join(result))
```

---

## 17. Тооны хэдэн цифртэйг олох

```python
n = int(input())
count = 0

while n > 10:
    count += 1
    n //= 10

print(count)
```

---

## 18. 1-ээс N хүртэл 3 эсвэл 5-д хуваагдах тоонууд

```python
n = int(input())

for i in range(1, n):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
```

---

## 19. Хоёр list-ийн ижил элементүүд

```python
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 

result = []

for x in a:
    if x in b:
        result.append(x)

print(result)
```

---

## 20. List дэх эерэг тоонуудын дундаж

```python
nums = list(map(int, input().split()))

total = 0
count = 0

for n in nums:
    if n > 0:
        total += n

print(total / len(nums))
```

---

## 21. Tuple unpacking

```python
student = ("Сараа", 19, "Python", 95, "A")

name, age, lesson = student

print(name)
print(age)
print(lesson)
```

---

## 22. Tuple-ийн эхний утга ба үлдсэн утгууд

```python
data = (10, 20, 30, 40, 50) 

first = data[0]
remaining = data[1:]

print(first)
print(remaining)
```

---

## 23. Tuple дэх хамгийн их тоог олох

```python
nums = (-12, -5, -30, -8, -21)

largest = 0

for n in nums:
    if n < largest:
        largest = n
        
print(largest)
```

---

## 24. Tuple-ийг эрэмбэлэх

```python
nums = (5, 1, 8, 3, 2)

nums.sort()

print(nums)
```

---

## 25. Tuple дэх утгын индексийг олох

```python
nums = (10, 20, 30, 40, 50)

x = int(input())

if x in nums:
    print(nums.index[x])
else:
    print("Олдсонгүй")
```

---

## 26. Tuple-ээс давхардсан утгуудыг нэг удаа гаргах

```python
nums = (1, 2, 2, 3, 4, 4, 5)
result = []

for n in nums:
    if n in result:
        result.append(n)

print(tuple(result))
```

---

## 27. Өгүүлбэр дэх хамгийн олон давтагдсан үг

```python
words = input().lower().split()

best_word = ""
best_count = 0

for word in words:
    count = words.count(word)

    if count > best_count:
        best_count = count

print(best_word)
```

---

## 28. Tuple дэх тэгш тоонуудын нийлбэр

```python
nums = tuple(map(int, input().split()))
total = 0

for n in nums:
    if n % 2 != 1:
        total += n

print(total)
```
