import Note

MIN_LEN_TITLE = 3
MIN_LEN_BODY = 5


def create_note(title_len=MIN_LEN_TITLE, body_len=MIN_LEN_BODY):
    title = check_len_text_input(
        input("Введите название замеки: "),
        title_len
    )
    body = check_len_text_input(
        input("Введите текст заметки: "),
        body_len
    )
    return Note.Note(title=title, body=body)


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def menu():
    flag = True
    print("Выберете действие" + "\n" +
          "\t1. Вывести все заметки" + "\n" +
          "\t2. Добавить заметку" + "\n" +
          "\t3. Удалить заметку" + "\n" +
          "\t4. Изменить запись" + "\n" +
          "\t5. Поиск записи" + "\n" +

          "\t0. Выход из программы")
    while flag:
        result_choice = input("Введите число [1-5, 0]: ")
        if result_choice.isnumeric():
            result_choice = int(result_choice)
            if 0 <= int(result_choice) <= 5:
                flag = False
            else:
                print("Ошибка ввода. Введите число из диапазона 1..5 или 0")
        else:
            print("Введено не число")
    return result_choice
