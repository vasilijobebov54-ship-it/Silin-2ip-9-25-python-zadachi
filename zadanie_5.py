a = int(input("Введите отрезок A: "))
b = int(input("Введите отрезок B: "))
free = a
while free >= b:
    free -= b
print(free)


n = int(input("Введите N: "))
k = int(input("Введите K: "))
quotient = 0
rest = n
while rest >= k:
    rest -= k
    quotient += 1
print(quotient)
print(rest)


n = int(input("Введите N: "))
k = 0
while (k + 1) * (k + 1) <= n:
    k += 1
print(k)


n = int(input("Введите N: "))
total = 0
k = 0
while total < n:
    k += 1
    total += k
print(k)
print(total)


p = float(input("Введите процент P: "))
deposit = 1000.0
months = 0
while deposit <= 1100:
    deposit = deposit * (1 + p / 100)
    months += 1
print(months)
print(deposit)


a = int(input("Введите отрезок A: "))
b = int(input("Введите отрезок B: "))
free = a
count = 0
while free >= b:
    free -= b
    count += 1
print(count)


n = int(input("Введите число N: "))
rest = n
while rest % 3 == 0:
    rest //= 3
print(rest == 1)


n = int(input("Введите число N (степень двойки): "))
rest = n
k = 0
while rest > 1:
    rest //= 2
    k += 1
print(k)


n = int(input("Введите число N: "))
factorial = 1.0
current = n
while current > 0:
    factorial *= current
    current -= 2
print(factorial)


n = int(input("Введите число N: "))
k = 1
while k * k <= n:
    k += 1
print(k)


n = int(input("Введите число N: "))
power = 1
k = 0
while power <= n:
    power *= 3
    k += 1
print(k)


n = int(input("Введите число N: "))
power = 1
k = 0
while power * 3 < n:
    power *= 3
    k += 1
print(k)


n = int(input("Введите число N: "))
total = 0
k = 0
while total + (k + 1) <= n:
    k += 1
    total += k
print(k)
print(total)


a = float(input("Введите число A: "))
total_sum = 0.0
k = 0
while total_sum <= a:
    k += 1
    total_sum += 1 / k
print(k)
print(total_sum)


a = float(input("Введите число A: "))
total_sum = 0.0
k = 0
while total_sum + 1 / (k + 1) < a:
    k += 1
    total_sum += 1 / k
print(k)
print(total_sum)

