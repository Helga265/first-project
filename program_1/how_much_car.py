# Програма що рахує витрати на паливо

# внести відомі данні
costs_100km = input("""Яка витрата палива автомобілем за 100км?
>>""")
costs_100km = float(costs_100km)
buy_1l = input("""Скільки коштує паливо
>>""")
buy_1l = float(buy_1l)
how_km = input("""Скільки кілометрів треба здолати?
>>""")
how_km = float(how_km)
# витрати палива на 1 км
expenses = costs_100km / 100
# скільки коштує 1 км
costs = expenses * buy_1l
# Скільки піде грошей на заданий кілометраж
z = round(costs * how_km, 2)
print(f'На {how_km} km буде витрачено {z} UAH')
