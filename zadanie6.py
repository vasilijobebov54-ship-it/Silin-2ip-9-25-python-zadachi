try:
    number = int(input("введите целое число: "))
    print(number)
except valueerror:
    print("ошибка ввода")

a = int(input("введите первое целое число: "))
b = int(input("введите второе целое число: "))
try:
    result = a / b
    print(f"{result:.1f}")
except zerodivisionerror:
    print("делить на ноль нельзя")

try:
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print(a / b)
except valueerror:
    print("ошибка ввода")
except zerodivisionerror:
    print("делить на ноль нельзя")

try:
    n = int(input("введите целое число: "))
    result = 100 / n
except valueerror:
    print("ошибка ввода")
except zerodivisionerror:
    print("делить на ноль нельзя")
else:
    print(result)
finally:
    print("вычисление завершено")

word = input("введите строку: ")
index = int(input("введите индекс: "))
try:
    print(word[index])
except indexerror:
    print("нет такого символа")

word = input("введите строку: ")
try:
    index = int(input("введите индекс: "))
    print(word[index])
except valueerror:
    print("ошибка ввода")
except indexerror:
    print("нет такого символа")


while true:
    try:
        number = int(input("введите целое число: "))
        break
    except valueerror:
        print("это не число. попробуй ещё:")
print(number)


total = 0
skipped = 0
while true:
    line = input("введите число (или пустую строку для выхода): ")
    if line == "":
        break
    try:
        total += int(line)
    except valueerror:
        skipped += 1
        print("пропущено: не число")
print(total)
print(skipped)


try:
    age = int(input("введите возраст: "))
    if age < 0 or age > 120:
        raise valueerror("возраст вне допустимого диапазона")
except valueerror as e:
    print(f"отклонено: {e}")
else:
    print(f"принято: {age}")


while true:
    try:
        choice = int(input("выберите пункт меню (1-5): "))
    except valueerror:
        print("введите число")
        continue
    if 1 <= choice <= 5:
        break
    print("такого пункта нет")
print(choice)


try:
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    result = a / b
except (valueerror, zerodivisionerror):
    print("посчитать не удалось")
else:
    print(f"{result:.2f}")


try:
    number = int(input("введите целое число: "))
except valueerror as e:
    print(e)
    print(type(e))
else:
    print(number)


try:
    a = float(input("введите число a: "))
    b = float(input("введите число b: "))
    print((a + b) / 2)
except valueerror:
    print("ошибка ввода")


try:
    number = int(input("введите целое число: "))
    if number > 0:
        number += 1
    elif number < 0:
        number -= 2
    else:
        number = 10
    print(number)
except valueerror:
    print("ошибка ввода")


try:
    n = int(input("введите число n (> 1): "))
    total = 0
    k = 0
    while total < n:
        k += 1
        total += k
    print(k)
    print(total)
except valueerror:
    print("ошибка ввода")
