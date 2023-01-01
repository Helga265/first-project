from podatok_def import podatok_nadhod

if __name__ == '__main__':
    print('Рахуємо податок від надхождення на рахунок підприємця')
    # Вхідні дані:
    size_income = float(input("""Який розмір надходження?
    >>"""))
    percentage_tax = float(input("""Який відсоток податка?
    >>"""))

    # Викликамо функцію
    fun = (podatok_nadhod(size_income, percentage_tax))
    print(f'Чистий прибуток складе: {fun} UAH')
