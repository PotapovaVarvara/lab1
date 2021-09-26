import math


def sprint_task_number(number):
    print('-' * 7, number, '-' * 7)

sprint_task_number(1)
print("Ваше имя: Варвара")
print("Ваша фамилия: Потапова")
print("Год назад ваш возраст был: 19")
sprint_task_number(2)

print("Лишь выпьет солнышко росу,")
print(" "*5, "Как он уже снует в лесу")
print(" "*10, "Над лютиками, кашками,")
print(" "*15, "Над белыми ромашками…")

print("То погудит, то попоет —")
print(" "*5, "В заботах весь, в работе…")
print(" "*10, "А то вдруг резко вверх уйдет")
print(" "*15, "На самой низкой ноте…")
sprint_task_number(3)

r = input("Радиус круга: ")
print("Площадь круга", math.pi * math.pow(int(r),2))

sprint_task_number(4)
s1, s2, s3 = input("Стороны треугольника: ").split(",")
p = (int(s1)+int(s2)+int(s3))/2
s = math.sqrt((p)*(p-int(s1))*(p-int(s2))*(p-int(s3)))
print("Площадь треугольника: ", s)

sprint_task_number(5)
number = input("Десятичное число: ")
print("Шестнадцатеричное число: ", hex(int(number)))

sprint_task_number(6)
word = input("Вы ввели слово: ")
print("Слово после преобразования 4 раза ", word*4)

sprint_task_number(7)
number71, number72 = input("Вы ввели числа: ").split(",")
print("Остаток от деления: ", int(number71)%int(number72))

sprint_task_number(8)
osn = input("Основание параллелограмма: ")
higth = input("Высота параллелограмма: ")
print("Площадь параллелограмма: ", int(osn)*int(higth))

sprint_task_number(9)
b = input("Размер файла (b): ")
print("Размер файла в килобайтах: ", int(b)/1024)

sprint_task_number(10)
m = input("Мужское имя: ")
g = input("Женское имя: ")
print("{0} + {1} = Love".format(m,g))