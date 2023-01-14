# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# start_point = sd.get_point(50, 50)
# end_point = sd.get_point(350, 450)
# for i in range(7):
#     sd.line(start_point, end_point, rainbow_colors[i], 4)
#     start_point.x += 5
#     end_point.x += 5


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
start_point = sd.get_point(300, 0)
radius = 100
for i in range(7):
    sd.circle(start_point, radius, rainbow_colors[i],20)
    radius += 21

sd.pause()
