# 1.Хоёр дахь хамгийн их тоо
# nums = list(map(int, input().split()))

# nums.sort()

# print(nums[-2])



# 2. Давхардсан тоонуудыг арилгах
# nums = list(map(int, input().split()))
# result = []
# for i in nums:
#     if i not in result:
#         result.append(i)
# print(result)



# 3.  Палиндром эсэх
# text = input()
# reverse = ""
# for i in range(len(text)):
#     reverse += text[-1 -i]
# if text == reverse:
#     print("YES")
# else:
#     print("NO")


# 4. Хамгийн урт үгийг олох
# words = input().split()
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)


# 5. Эгшгийн тоо
# text = input().lower()
# vowels = "аэиоуөү"
# count = 0

# for ch in text:
#     if ch in vowels:
#         count += 1
# print(count)


# 6. 1-ээс N хүртэлх тэгш тоонуудын нийлбэр
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i % 2 == 0: 
#         total += i
# print(total)




# 7.Тооны цифрүүдийн нийлбэр
# n = int(input())
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print(total)


# 8.Тоог урвуу болгох
# n = int(input())
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse*10 + digit
#     n //= 10
# print(reverse)


# 9.Анхны тоо шалгах
# n = int(input())
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")


# 10.List дэх хамгийн бага тоог `min()` ашиглахгүй олох
nums = list(map(int, input().split()))
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)



