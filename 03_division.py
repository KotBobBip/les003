# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 999864568, 37

i = 1
while b * i < a:
    i += 1
print("Целочисленное деление", a, "на", b, "дает", i - 1)
print("Проверка результата:", a // b)

