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





