# Програма, що рахує абонплату за комунальним лічильника
abonent = input("""Выберите одно:
1. Оплата абонплати за електроенергю 
2. Оплата абонплати за газ
>>""")

x = float(input("""Введіть попередні значення лічильника:
>>"""))
y = float(input("""Введіть поточні значення лічильника:
>>"""))

if abonent == '1':
    z = float(input("""Скільки коштує 1 кВт електроенергії:
>>"""))
# вирахувати різницю між данними
    summ = y - x
# отримати скільки буде коштувати дана різниця
    buy = abs(round(summ * z, 2))
    print(f'Треба сплатити: {buy} UAH')

if abonent == '2':
    z = float(input("""Скільки коштує 1 куб газу:
>>"""))


# вирахувати різницю між данними
    summ = y - x
# отримати скільки буде коштувати дана різниця
    buy = abs(round(summ * z, 2))
    print(f'Треба сплатити: {buy} UAH')
