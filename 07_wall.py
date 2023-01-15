# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
start_point = sd.get_point(0, 0)
end_point = sd.get_point(100, 50)
brick_color = sd.COLOR_ORANGE
for j in range(1, 12, 1):
    for i in range(1, 7, 1):
        sd.rectangle(start_point, end_point, brick_color, 0)
        start_point.x += 101
        end_point.x += 101
    start_point.x = 0
    start_point.y += 51
    end_point.x = 100
    end_point.y += 51

sd.pause()
