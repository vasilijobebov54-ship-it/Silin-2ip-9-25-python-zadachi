a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print(count)

price = float(input())
for kg in range(1, 11):
    cost = price * kg
    print(f"{kg} кг: {cost:.2f}")

price = float(input())
for i in range(1, 11):
    kg = i / 10
    cost = price * kg
    print(f"{kg:.1f} кг: {cost:.2f}")

price = float(input())
for i in range(6, 11):
    kg = i / 5
    cost = price * kg
    print(f"{kg:.1f} кг: {cost:.2f}")

a = int(input())
b = int(input())
product = 1
for i in range(a, b + 1):
    product *= i
print(product)

a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    total += i * i
print(total)

n = int(input())
total = 0
for i in range(n, 2 * n + 1):
    total += i * i
print(total)

n = int(input())
product = 1.0
for i in range(1, n + 1):
    product *= 1 + i * 0.1
print(f"{product:.2f}")

n = int(input())
total = 0.0
for i in range(1, n + 1):
    term = 1 + i * 0.1
    if i % 2 == 0:
        total -= term
    else:
        total += term
print(f"{total:.2f}")

a = float(input())
n = int(input())
power = 1.0
for _ in range(n):
    power *= a
print(power)
