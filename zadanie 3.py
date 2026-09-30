A = int(input("Введите целое число A: "))
is_odd = A % 2 != 0
print(is_odd)


A = int(input("Введите целое число A: "))
isnt_odd = A % == 0
print(isnt_odd)


A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
if A > 2 and B <= 3:
    print("Истина (Оба неравенства справедливы)")
else:
    print("Ложь (Одно или оба неравенства не выполняются)")


A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
if A >= 0 or B < -2:
    print("Истина (По крайней мере одно из условий выполняется)")
else:
    print("Ложь (Ни одно из условий не выполнилось)")


A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
if (A < B < C) or (C < B < A):
    print("Истина (B находится между A и C)")
else:
    print("Ложь (B не находится между A и C)")


A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
if A % 2 != 0 and B % 2 != 0:
    print("Истина (Каждое из чисел нечетное)")
else:
    print("Ложь (Одно или оба числа четные)")


A = int(input())
B = int(input())
if A % 2 != 0 or B % 2 != 0:
    print("Хотя бы одно из чисел нечетное")
else:
    print("Оба числа четные")


a = int(input())
b = int(input())
if a % 2 == 0 and b % 2 == 0:
    print("четность одинаковая")
else:
    print("не одинаковая")


A = int(input())
B = int(input())
C = int(input())
if A > 0 or B > 0 or C > 0:
    print("какое то из чисел положительное")
else:
    print("ни одно не положительное")



num = int(input("Введите целое число: "))
if num > 0:
    num = num + 1
print(num)


num = int(input("Введите целое число: "))
if num > 0:
    num += 1
else:
    num -= 2
print(num)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
count = 0
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1
print("Количество положительных чисел:", count)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
positive_count = 0
negative_count = 0
if a > 0:
    positive_count += 1
elif a < 0:
    negative_count += 1
if b > 0:
    positive_count += 1
elif b < 0:
    negative_count += 1
if c > 0:
    positive_count += 1
elif c < 0:
    negative_count += 1
print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)










