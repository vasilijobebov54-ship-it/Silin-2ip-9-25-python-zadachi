a = float(input())
b = float(input())
c = float(input())
V = a * b * c 
S = 2 * (a * b + b * c + a * c)
print(V)
print(S)



R = float(input("Введите радиус"))
p = 3.14
L = 2 * p * R
S = p * R ** 2



a = 2
b = 2
c = (a * b) // 2
print(c)



import math
a = 2
b = 3
c = 2 * 3
koren = math.sqrt(c)
print(koren)




a = float(input("Введите первое ненулевое число (a): "))
b = float(input("Введите второе ненулевое число (b): "))
if a == 0 or b == 0:
    print("Ошибка: числа не должны быть равны нулю!")
else:
    
    sq_a = a ** 2
    sq_b = b ** 2
    sum_squares = sq_a + sq_b
    diff_squares = sq_a - sq_b
    prod_squares = sq_a * sq_b
    quot_squares = sq_a / sq_b

    print(f"Сумма квадратов: {sum_squares}")
    print(f"Разность квадратов: {diff_squares}")
    print(f"Произведение квадратов: {prod_squares}")
    print(f"Частное квадратов: {quot_squares}")





a = float(input("Введите первое ненулевое число (a): "))
b = float(input("Введите второе ненулевое число (b): "))
if a == 0 or b == 0:
    print("Ошибка: числа не должны быть равны нулю!")
else:
    module_b = abs(b)
    module_a = abs(a)
    result1 = module_a + module_b
    result2 = module_a - module_b
    result3 = module_a * module_b
    result4 = module_a / module_b
    
    print(result1, result2, result3, result4)






