# Програма, що рахує податок від надхождення на рахунок підприємця.
# Вхідні дані:
size_income = input("""Який розмір надходження?
>>""")
size_income = float(size_income)
percentage_tax = input("""Який відсоток податка?
>>""")
percentage_tax = float(percentage_tax)
# перевести отриманий відсокот в число
percent = percentage_tax / 100
# скільки потрібно сплатити податку
pay_percent = round(size_income * percent, 2)
print(f'Податку буде сплачено: {pay_percent} UAH')
# скільки залишиться чистого прибутку
remainder = round(size_income - pay_percent, 2)
print(f'Чистий прибуток складе: {remainder} UAH')
