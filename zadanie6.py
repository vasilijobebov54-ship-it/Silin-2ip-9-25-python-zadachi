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
