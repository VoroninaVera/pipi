#1

# N = int(input("Введите N: "))
# sum_even = 0
# for i in range(2, N + 1, 2):
#     sum_even += i
# print(f"Сумма чётных чисел до {N}: {sum_even}")

#2

# N = int(input("Введите N: "))
# factorial = 1
# for i in range(2, N + 1):
#     factorial *= i
# print(f"{N}! = {factorial}")

#3

# N = int(input("Введите N: "))
# count = 0
# for i in range(1, N):
#     if N % i == 0:
#         count += 1
# print(f"Кол-во делителей {N}, меньших самого числа: {count}")

#4

# N = int(input("Введите N: "))
# if N < 2:
#     print("Не простое")
# else:
#     is_prime = True
#     for i in range(2, int(N ** 0.5) + 1):
#         if N % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{N} - простое число")
#     else:
#         print(f"{N} - не простое число")

#5

# N = int(input("Сколько чисел будете вводить? "))
# max_num = float('-inf')
# for i in range(N):
#     x = float(input(f"Число {i + 1}: "))
#     if x > max_num:
#         max_num = x
# print(f"Наибольшее число: {max_num}")

#6

# min_positive = None
# count_min = 0

# while True:
#     num = int(input("Введите целое число (0 для выхода): "))
#     if num == 0:
#         break
#     if num > 0:
#         if min_positive is None or num < min_positive:
#             min_positive = num
#             count_min = 1
#         elif num == min_positive:
#             count += 1
#     if min_positive is None:
#         print("Положительных чисел не было")
#     else:
#         print(f"Наименьшее положительное: {min_positive}")
#         if count_min > 1:
#             print(f"Оно повторяется {count_min} раза")
#         else:
#             print("Оно единственное")

#7

# summa = 0
# count = 0

# while True:
#     num = float(input("Введите целое число (0 для выхода): "))
#     if num == 0:
#         break
#     summa += num
#     count += 1

# if count == 0:
#     print("Чисел не введено")
# else:
#     average = summa / count
#     print(f"Среднее арифметическое: {average}")

#-------------------------------------------------------------------

#1

# positive = negative = 0
# while True:
#     num = int(input("Введите целое число (0 для выхода): "))
#     if num == 0:
#         break
#     elif num > 0:
#         positive += 1
#     else:
#         negative += 1

# total = positive + negative
# if total > 0:
#     print(f"Положительных: {positive/total*100:1f}%")
#     print(f"Отрицательных: {negative/total*100:1f}%")
# else:
#     print("Нет чисел")

#2

# n = int(input("Введите N: "))
# min_even = None
# for i in range(n):
#     num = int(input(f"Введите число {i + 1}: "))
#     if num % 2 == 0:
#         if min_even is None or num < min_even:
#             min_even = num

# if min_even is not None:
#     print(f"Чётное: {min_even}")
# else:
#     print(f"Не чётное")

#3

# n = int(input("Введите N: "))
# nums = [float(input(f"Введите число {i + 1}: ")) for i in range(n)]

# a = all(nums[i] > nums[i - 1] for i in range(1, n))

# print("Возрастающая" if a else "Не возрастающая")

#4

# a = float(input("Введите число: "))
# if a == 0:
#     print("Пусто")
# else:
#     b = [a]
#     while True:
#         c = float(input("Введите след. число: "))
#         if c == 0:
#             break
#         b.append(c)
    
#     d = all(b[i] > b[i + 1] for i in range(len(b) - 1))
#     print("Убывающая" if d else "Не убывающая")

#5

# sum_even = 0
# count_even = 0

# while True:
#     num = int(input("Введите число: "))
#     if num == 0:
#         break
#     if num % 2 == 0:
#         sum_even += num
#         count_even += 1

# if count_even > 0:
#     print(f"Среднее чётных: {sum_even / count_even:.2f}")
# else:
#     print("Чётных нет")

#6

n = int(input("Введите N: "))
sum_neg = 0
count_neg = 0

for i in range(n):
    num = float(input(f"Введите число {i + 1}: "))
    if num < 0:
        sum_neg += num
        count_neg += 1

if count_neg > 0:
    print(f"Среднее отрицательных: {sum_neg / count_neg:.2f}")
else:
    print("Отрицательных нет")