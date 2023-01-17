def menu(key_list: dict):
    """
    Виводить на екран перелік ключових слів
    :type key_list: dict
    :param key_list: вхідний параметр є ключові слова
    :return: кортеж ключів
    """
    print('>>> Перелік ключових слів:')
    for word, definition in key_list.items():
        print(f' {word:10} - {definition}')
    key = tuple(key_list.keys())
    return key


def notes_or_0(note_list: list):
    """
    Перевіряє чи щось є в списоку
    :param note_list: основний список
    :return: якщо список не пустий повертає True в іншому випадку повідомлення
    """
    if len(note_list) > 0:
        return True
    else:
        print('> Список з нотатками пустий!')


def how_note_print():
    """
    Цикл, до того момоменту, поки не буде введено ціле число від одного
    :return: повертає число, потім скільки записів буде виведено
    """
    while True:
        try:
            how_print = int(input('>>> '))
            if how_print > 0:
                return how_print
            else:
                print('>>> Ввдеіть значення від 1 !')
        except ValueError:
            print('> Ввдеіть ціле число!')
            continue


def user_input_note(key: tuple):
    """
    Фунція працює з ключами які вводяться та виконує певні завдання по кожній
    :param key: ключі із словника
    """
    note_list = []
    while True:
        print('>>> Введіть одну з команд')
        note = input('> ')
        # key - add
        if note == key[0]:
            print('>>> Скільки нотатків ви хочіте додати:')
            how_print = how_note_print()
            for x in range(how_print):
                notesss = input('> Введіть нотатку:')
                note_list.append(notesss)    # додаємо в список
        # key - earliest
        elif note == key[1]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print()
                print('>>> Від найранішої до найпізнішої:')
                for i in note_list[:how_print]:
                    print(f'> {i}')
        # key - latest
        elif note == key[2]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print()
                print('>>> Від найпізнішої до найранішої:')
                note_list_rever = list(reversed(note_list))   # reversed - перевертає список
                for i in note_list_rever[:how_print]:
                    print(f'> {i}')
        # key - longest
        elif note == key[3]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print()
                print('>>> Від найдовшої до найкоротшої:')
                note_list_sort = sorted(note_list, key=len, reverse=True)  # sorted - сортирує список по довжині key
                for i in note_list_sort[:how_print]:
                    print(f'> {i}')
        # key - shortest
        elif note == key[4]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print()
                print('>>> Від найкоротшої до найдовшої:')
                note_list_sort = sorted(note_list, key=len)
                for i in note_list_sort[:how_print]:
                    print(f'> {i}')
        # key - clear
        elif note == key[5]:
            if notes_or_0(note_list):
                note_list.clear()     # clear - видаляє все в списку
                print('>>> Список нотатків пустий')
        # key - exit
        elif note == key[6]:
            exit(0)
        else:
            print(f'Виберіть одну з команд: {key}')
