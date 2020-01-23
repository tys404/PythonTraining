from . import Ask
from .VisitCardManager import Parameter


def print_menu():
    print("[N]ew visit card")
    print("Show [V]isit card")
    print("Show [L]ist of visit cards")
    print("[E]dit visit card")
    print("[D]elete visit card")
    print("e[X]it")
    print()


def get_choice():
    return Ask.menu_choice("Your choice: ")


def print_parameters():
    print("  Parameters: ")
    for parameter in Parameter:
        print(f"    {parameter.name}")


def get_new_visit_card_data():
    print("--- new card ---")
    name = Ask.string_nonempty("Name: ")
    surname = Ask.string_nonempty("Surname: ")
    birth_date = Ask.date("Date of birth: ")
    city = input("City: ")

    return name, surname, birth_date, city


def get_index(list_):
    return Ask.index("Index: ", list_)


def get_param_to_edit():
    return Ask.visit_card_parameter("Parameter to edit: ")


def get_new_value(param):
    if param == Parameter.BIRTHDAY.name:
        value = Ask.date("Date of birth: ")
    elif param == Parameter.NAME or param == Parameter.SURNAME:
        value = Ask.string_nonempty("New value: ")
    else:
        value = input("New value: ")

    return value
