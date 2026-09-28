a = float(input())
b = float(input())
c = float(input())
V = a * b * c 
S = 2 * (a * b + b * c + a * c)
print(V)
print(S)



R = float(input("Введите радиус"))
PI = 3.14
L = 2 * PI * R
S = PI * R ** 2



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




import math
a = float(input())
b = float(input())
c = math.sqrt(a ** 2 + b ** 2)
P = a + b + c
print(c)
print(P)



PI = 3.14
R1 = float(input("Введите внешний радиус R1: "))
R2 = float(input("Введите внутренний радиус R2: "))
S1 = PI * (R1 ** 2)
S2 = PI * (R2 ** 2)
S3 = S1 - S2

print(f"Площадь внешнего круга (S1): {S1}")
print(f"Площадь внутреннего круга (S2): {S2}")
print(f"Площадь кольца (S3): {S3}")



PI = 3.14
L = float(input())
R = L / (2 * PI)
S = PI * (R ** 2)
print(R)
print(S)


PI = 3.14
S = float(input())
R = (S / PI) ** 0.5
D = 2 * R
L = 2 * PI * R
print(D)
print(L)



x1 = float(input())
x2 = float(input())
distance = abs(x2 - x1)
print(distance)


a = float(input())
b = float(input())
c = float(input())
distance1 = abs(a - b)
distance2 = abs(b - c)
sumdistance = distance2 + distance1
print(distance1, distance2, sumdistance)




a = 1
b = 5
c = 3
ab = abs(a - b)
bc = abs(b - c)
abbc = ab * bc
print(ab, bc, abbc)



x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
width = abs(x2 - x1)
height = abs(y2 - y1)
perimeter = 2 * (width + height)
area = width * height
print(perimeter)
print(area)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(distance)












