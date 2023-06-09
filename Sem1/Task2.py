# В некоторой школе решили набрать три новых математических класса
# и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждой из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# **Input:**
# 20
# 21
# 22
# **Output:**
# 32

# import math # решение через math.ceil

# a = 20
# b = 21
# c = 22
# k = (a + b + c) / 2

# print(math.ceil(k))

# Решение с переменными, от целого числа плюс 1 при делении на 2, с учетом каждого класса.

first = int(input("Ученики первого класса: "))
second = int(input("Ученики второго класса: "))
third = int(input("Ученики третьего класса: "))

total = (first + 1) // 2 + (second + 1) // 2 + (third + 1) // 2

print(total)