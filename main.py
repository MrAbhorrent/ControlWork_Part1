from utils import print_divider


def read_notes(_file):
    data = []
    with (open(_file, 'r', encoding="utf-8")) as _file:
        for line in _file:
            data.append(line.strip())
    return data


def save_note(_file, _type_operation, _note):
    with (open(_file, _type_operation, encoding="utf-8")) as _file:
        for line in _note:
            _file.write(str(line) + "\n")


def add_note(_file):
    new_contact_last_name = input("Введите Фамилию: ")
    new_contact_first_name = input("Введите Имя: ")
    new_contact_surrender_name = input("Введите Отчество: ")
    new_contact_phonenumber = input("Введите Номер: ")
    input_string = f"{new_contact_last_name};{new_contact_first_name};{new_contact_surrender_name};{new_contact_phonenumber}"
    record = []
    record.append(input_string)
    save_note(_file, 'a', _note=record)


def search_note(_data, search_name, position=0):
    search_note_data = []
    for note in _data:
        record = note.split(';')
        if search_name.lower() == record[position].lower():
            search_note_data.append(note)
    return search_note_data


def delete_note(_data):
    phonebook_data = read_notes(_data)
    print_records(phonebook_data)
    print_divider(n=10)
    print()
    number_delete_record = input("Введите номер записи для удаления: ")
    print("Удаляем запись - " + phonebook_data.pop(int(number_delete_record) - 1))
    print_records(phonebook_data)
    save_note(_data, 'w', _note=phonebook_data)


def input_edit(_string, defult_value=''):
    result = input(_string + f" [{defult_value}]: ")
    return result if len(result) > 0 else defult_value


def edit_note(_data):
    phonebook_data = read_notes(_data)
    print_records(phonebook_data)
    print_divider(symbol="*", n=25)
    print()
    number_delete_record = int(input("Введите номер записи для редактирования: ")) - 1
    edit_record = phonebook_data.pop(number_delete_record)
    print("Редактируем запись - " + edit_record)
    last_name, first_name, surrender_name, phone_number = edit_record.split(';')
    last_name = input_edit("Введите Фамилию", last_name)
    first_name = input_edit("Введите Имя", first_name)
    surrender_name = input_edit("Введите Отчество", surrender_name)
    phone_number = input_edit("Введите Номер", phone_number)
    input_string = f"{last_name};{first_name};{surrender_name};{phone_number}"
    phonebook_data.insert(number_delete_record, input_string)
    save_note(_data, 'w', _note=phonebook_data)


def print_records(_data):
    counter = 1
    for note in _data:
        print(str(counter), end=' | ')
        print(*note.split(';'))
        counter += 1


def main():
    work_flag = True
    phonebook_data = read_notes(data_file)
    while work_flag:
        user_choice = menu()
        print(f"Выбрано действие - {user_choice}")
        if user_choice == 1:
            print_records(phonebook_data)
        elif user_choice == 2:
            search = input("Введите фамилию: ")
            find_contact = search_note(phonebook_data, search)
            if len(find_contact) > 0:
                print_records(find_contact)
            else:
                print("Запись не найдена")
        elif user_choice == 3:
            add_note(data_file)
            phonebook_data = read_notes(data_file)
        elif user_choice == 4:
            delete_note(data_file)
            phonebook_data = read_notes(data_file)
        elif user_choice == 5:
            edit_note(data_file)
            phonebook_data = read_notes(data_file)
        elif user_choice == 0:
            work_flag = False
        print_divider()


data_file = 'data\data.txt'
main()
