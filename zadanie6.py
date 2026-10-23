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
