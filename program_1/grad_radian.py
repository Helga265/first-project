# Програма, яка конвертує градуси у радіани
# значення Pi
Pi = 3.14159265359
# вибір що хочемо перевести
convert = input("""Выберите одно:
1. Градуси в радіни 
2. Радіани в градуси
>>""")
# задаємо значення градусів чи радіан
x = input("""Введіть значення
>>""")
# вказуємо що ти даних буде дисятичний
x = float(x)
# вроводимо розрахунок згідно отриманих даних
if convert == '1':
    radian = round(x * Pi / 180, 5)
    print(f'{x}° = {radian} рад ')

if convert == '2':
    gradus = round(x * 180 / Pi, 5)
    print(f'{x} рад = {gradus}°')