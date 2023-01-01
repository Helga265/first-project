def podatok_nadhod(size_income: float, percentage_tax: float) -> float:
    # перевести отриманий відсокот в число
    percent = percentage_tax / 100
    # скільки потрібно сплатити податку
    pay_percent = round(size_income * percent, 2)
    print(f'Податку буде сплачено: {pay_percent} UAH')
    # скільки залишиться чистого прибутку
    remainder = round(size_income - pay_percent, 2)
    return remainder