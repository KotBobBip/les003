# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def draw_smile(coord_x, coord_y, color):
    center_point = sd.get_point(coord_x, coord_y)
    # Рисуем голову
    center_point_head = center_point
    sd.circle(center_point_head, 50, sd.COLOR_YELLOW, 1)

    # Рисуем улыбку в два подхода
    center_point_smile1 = sd.get_point(center_point.x, center_point.y - 20)
    sd.circle(center_point_smile1, 20, sd.COLOR_WHITE, 0)

    center_point_smile2 = center_point
    sd.circle(center_point_smile2, 30, sd.background_color, 0)

    # Рисуем глаза
    # Левый глаз
    center_point_left_eye = sd.get_point(center_point.x - 20, center_point.y + 10)
    sd.circle(center_point_left_eye, 10, sd.COLOR_BLACK, 0)

    # Правый глаз
    center_point_right_eye = sd.get_point(center_point.x + 20, center_point.y + 10)
    sd.circle(center_point_right_eye, 10, sd.COLOR_BLACK, 0)


draw_smile(100, 100, sd.COLOR_YELLOW)
draw_smile(200, 200, sd.COLOR_YELLOW)
draw_smile(300, 300, sd.COLOR_YELLOW)

# sd.lines(point_list, sd.COLOR_YELLOW)
sd.pause()
