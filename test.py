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
