from NotesView import menu
from utils import print_divider

from ControllerFileOperation import *
import ControllerNotes as cn


def main():
    work_flag = True
    while work_flag:
        user_choice = menu()
        print_divider('-')
        print(f"Выбрано действие - {user_choice}")
        if user_choice == 1:
            cn.show('all')
        elif user_choice == 2:
            cn.add()
        elif user_choice == 3:
            cn.show('all')
            cn.delete()
        elif user_choice == 4:
            cn.show('all')
            cn.edit()
        elif user_choice == 5:
            cn.show('id')
        elif user_choice == 0:
            work_flag = False
        print_divider()
