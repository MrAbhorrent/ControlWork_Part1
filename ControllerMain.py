from NotesView import menu
from utils import print_divider
from ControllerFileOperation import *

def main():
    work_flag = True
    phonebook_data = read_file()
    while work_flag:
        user_choice = menu()
        print_divider('-')
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