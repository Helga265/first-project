# Программа, що перевіряє чи є введена строка дзеркальною(паліндромом)
# введення даних
info = str(input('Введіть текст або цифри: '))
# переводимо отримані данні в нижній реєстр і видаляємо пробіли
info = info.lower().replace(' ', '').replace('.', '').replace(',', '').replace('-', '').replace(':', '')\
    .replace(';', '').replace('?', '').replace('!', '').replace('"', '').replace("'", '')
# перевертаємо отримані дані
info_new = info[::-1]
# порівнюємо отримані та перевернуті дані
if info == info_new:
    print('It is a palindrome')
else:
    print('It is NOT a palindrome')
