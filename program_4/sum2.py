num = ''
num_list = []
while True:
    try:
        num = input('Ведіть будь-яке число чи sum: ')
        if num == 'sum':
            print(f'Такі числа були введені: {num_list}')
            print(f'В сумі чисел отримаємо таке знвчення: {sum(num_list)}')
        else:
            num_list.append(float(num))
    except ValueError:
        print('Введіть число або sum, будь-ласка!')
