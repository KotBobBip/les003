# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 100)
# radius = 50
# for _ in range(3):
#     radius += 2
#     sd.circle(point, radius, (255, 0, 255))

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def bubble(point, step, tup_color):
    radius = 50
    for _ in range(4):
        radius += step
        sd.circle(point, radius, tup_color)



# Нарисовать 10 пузырьков в ряд
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 200)
#     bubble(point, 5)


# Нарисовать три ряда по 10 пузырьков
# for x in range(100, 1100, 100):
#     for y in range(100, 400, 100):
#         point = sd.get_point(x, y)
#         bubble(point, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
for _ in range(100):
    point = sd.random_point()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup_color = (r, g, b)
    bubble(point, 5, tup_color)

sd.pause()


