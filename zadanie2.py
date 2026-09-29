A = 1
B = 2
C = 3
temp = A
A = C
C = B
B = temp
print("A =", A)
print("B =", B)
print("C =", C)


A = 1
B = 2
C = 3
temp = A
A = B
B = C
C = temp
print("A =", A)
print("B =", B)
print("C =", C)


x = float(input("Введите значение x: "))
y = 4 * (x - 3)**6 - 7 * (x - 3)**3 + 2
print(f"При x = {x} значение функции y = {y}")


A = float(input("Введите число A: "))
A2 = A * A
A4 = A2 * A2
A8 = A4 * A4
print(f"A^2 = {A2}")
print(f"A^4 = {A4}")
print(f"A^8 = {A8}")


A = float(input())

A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5

print(A2)
print(A3)
print(A5)
print(A10)
print(A15)


alpha = float(input())
degrees = alpha * 180 / 3.14
print(degrees)


TF = float(input())
TC = (TF - 32) * 5 / 9
print(TC)


TC = float(input())
TF = TC * 9 / 5 + 32
print(TF)


X = float(input())
A = float(input())
Y = float(input())
price_per_kg = A / X
price_for_Y = price_per_kg * Y
print(price_per_kg)
print(price_for_Y)


X = float(input())
A = float(input())
Y = float(input())
B = float(input())
price_choco = A / X
price_toffee = B / Y
ratio = price_choco / price_toffee
print(price_choco)
print(price_toffee)
print(ratio)



V = float(input())
U = float(input())
T1 = float(input())
T2 = float(input())
S = V * T1 + (V - U) * T2
print(S)



V1 = float(input())
V2 = float(input())
S = float(input())
T = float(input())
total_distance = S + T * (V1 + V2)
print(total_distance)




M = int(input())
tons = M // 1000
print(tons)



bytes_size = int(input())
kilobytes = bytes_size // 1024
print(kilobytes)



A = int(input())
B = int(input())
count = A // B
print(count)





