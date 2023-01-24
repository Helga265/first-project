def file_add() -> list:
    """
    Відкриття файлу "note_file.txt"
    Якщо його не має, то створюємо "file_note.txt"
    :return: повертає список нотатків
    """
    try:
        with open('note_file.txt', mode='r', encoding='utf-8') as f:   # зчитуємо файл
            list_file = f.readlines()
    except Exception:
        # створюємо пустий список привідсутності файлу
        list_file = list()
    return list_file


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


def how_note_print(note_list):
    """
    Цикл, до того момоменту, поки не буде введено ціле число від одного до кількості в списку
    :return: повертає число, потім скільки записів буде виведено
    """
    len_note = len(note_list)   # рахує кількість нотатків списку
    while True:
        try:
            how_print = int(input('>>> '))
            if len_note >= how_print > 0:    # якщо нотатків стількі скіли є в списку -> виводить
                return how_print
            elif len_note < how_print:   # якщо запит на більше ніж ж є в списку, просить ввести скільки є в списку
                print(f'>>> У вас всього {len_note} нотатків, введіть до цього числа!')
            else:
                print('>>> Ввдеіть значення від 1!')   # якщо не коректно введене число
        except ValueError:
            print('> Ввдеіть ціле число!')
            continue


def how_note():
    """
    Цикл, до того момоменту, поки не буде введено ціле число від одного
    :return: повертає число, потім скільки записів буде введено
    """
    while True:
        try:
            how_input = int(input('>>> '))
            if how_input > 0:
                return how_input
            else:
                print('>>> Ввдеіть значення від 1 !')
        except ValueError:
            print('> Ввдеіть ціле число!')
            continue


def user_input_note(key: tuple, notelist: list):
    """
    Фунція працює з ключами які вводяться та виконує певні завдання по кожній
    :param notelist: список нотаток з файлу
    :param key: ключі із словника
    """
    note_list = [note for note in notelist]
    while True:
        print('>>> Введіть одну з команд')
        note = input('> ')
        # key - add
        if note == key[0]:
            print('>>> Скільки нотатків ви хочіте додати:')
            how_input = how_note()
            for x in range(how_input):
                notesss = input('> Введіть нотатку:')
                note_list.append(notesss)  # додаємо в список
        # key - earliest
        elif note == key[1]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print(note_list)
                print('>>> Від найранішої до найпізнішої:')
                for i in note_list[:how_print]:
                    print(f'> {i}')
        # key - latest
        elif note == key[2]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print(note_list)
                print('>>> Від найпізнішої до найранішої:')
                note_list_rever = list(reversed(note_list))  # reversed - перевертає список
                for i in note_list_rever[:how_print]:
                    print(f'> {i}')
        # key - longest
        elif note == key[3]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print(note_list)
                print('>>> Від найдовшої до найкоротшої:')
                note_list_sort = sorted(note_list, key=len, reverse=True)  # sorted - сортирує список по довжині key
                for i in note_list_sort[:how_print]:
                    print(f'> {i}')
        # key - shortest
        elif note == key[4]:
            if notes_or_0(note_list):
                print('>>> Скільки нотатків вивести:')
                how_print = how_note_print(note_list)
                print('>>> Від найкоротшої до найдовшої:')
                note_list_sort = sorted(note_list, key=len)
                for i in note_list_sort[:how_print]:
                    print(f'> {i}')
        # key - clear
        elif note == key[5]:
            if notes_or_0(note_list):
                note_list.clear()  # clear - видаляє все в списку
                print('>>> Список нотатків пустий')
        # key - exit
        elif note == key[6]:
            with open('note_file.txt', mode='w', encoding='utf-8') as f:  # відкриваємо файл та
                for poz in note_list:  # записуємо по елементно зі списку і закриваємо
                    f.write(poz.strip()+'\n')

                print('>>> Ваші нотатки збережені :)')
            exit(0)
        else:
            print(f'Виберіть одну з команд: {key}')
