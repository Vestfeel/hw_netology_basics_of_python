#first_task
phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
else:
    print('Фраза 2 длиннее фразы 1')

#second_task
year = 2019
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный год')
else:
    print('Обычный год')

date = int(input('Введите день'))
if date < 10:
    date = str(0) + str(date)

#third_task
month = str(input('Введите месяц'))
if month == 'Январь':
    month = int(1)
elif month == 'Февраль':
    month = int(2)
elif month == 'Март':
    month = int(3)
elif month == 'Апрель':
    month = int(4)
elif month == 'Май':
    month = int(5)
elif month == 'Июнь':
    month = int(6)
elif month == 'Июль':
    month = int(7)
elif month == 'Август':
    month = int(8)
elif month == 'Сентябрь':
    month = int(9)
elif month == 'Октябрь':
    month = int(10)
elif month == 'Ноябрь':
    month = int(11)
else:
    month = int(12)

concat = int(str(month)+str(date))

if 121 > concat > 100:
    print('Ваш знак зодиака: Козерог')
elif 219 > concat > 120:
    print('Ваш знак зодиака: Водолей')
elif 321 > concat > 218:
    print('Ваш знак зодиака: Рыбы')
elif 420 > concat > 320:
    print('Ваш знак зодиака: Овен')
elif 521 > concat > 419:
    print('Ваш знак зодиака: Телец')
elif 621 > concat > 520:
    print('Ваш знак зодиака: Близнецы')
elif 723 > concat > 620:
    print('Ваш знак зодиака: Рак')
elif 823 > concat > 722:
    print('Ваш знак зодиака: Лев')
elif 923 > concat > 822:
    print('Ваш знак зодиака: Дева')
elif 1023 > concat > 922:
    print('Ваш знак зодиака: Весы')
elif 1122 > concat > 1022:
    print('Ваш знак зодиака: Скорпион')
elif 1223 > concat > 1121:
    print('Ваш знак зодиака: Стрелец')
elif concat > 1222:
    print('Ваш знак зодиака: Козерог')


#fourth_task
width = 45
length = 205
height = 45

if width < 15 and length < 15 and height < 15:
    print('Коробка №1')
elif width > 200 or length > 200 or height > 200:
    print('Упаковка для лыж')
elif 15 < width < 50 or 15 < length < 50 or 15 < height < 50:
    print('Коробка №2')
else:
    print('Коробка №3')

#fifth_task
number = 123321
number = str(number)

f_part_number = number[:3]
s_part_number = number[3:]
sum_1 = sum(int(i) for i in f_part_number)
sum_2 = sum(int(i) for i in s_part_number)

if sum_1 == sum_2:
    print('Счастливый билет')
else:
    print('Несчастливый билет')

#sixth_task
import math

fig_type = str(input('Введите тип фигуры:'))
if fig_type == 'Круг':
    r_circle = int(input('Введите радиус круга:'))
    print(round(math.pi * r_circle**2, 2))
elif fig_type == 'Треугольник':
    a_triangle_side = int(input('Введите длину стороны A:'))
    b_triangle_side = int(input('Введите длину стороны B:'))
    c_triangle_side = int(input('Введите длину стороны C:'))
    half_perim = (a_triangle_side + b_triangle_side + c_triangle_side) / 2
    print(round(math.sqrt(half_perim * (half_perim - a_triangle_side) * (half_perim - b_triangle_side) * (half_perim - c_triangle_side)), 2))
elif fig_type == 'Прямоугольник':
    a_rectangle_side = int(input('Введите длину стороны A:'))
    b_rectangle_side = int(input('Введите длину стороны B:'))
    print(round(a_rectangle_side * b_rectangle_side, 2))