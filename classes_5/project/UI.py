from .VisitCardManager import VisitCardManager, Parameter
from .Validator import Validator


class UI:
    def __init__(self):
        self.visit_card_manager = VisitCardManager()
        self.choice = ''

    @staticmethod
    def print_menu():
        print("[N]ew visit card")
        print("Show [V]isit card")
        print("Show [L]ist of visit cards")
        print("[E]dit visit card")
        print("[D]elete visit card")
        print()

    def get_choice(self):
        self.choice = self.get_validated_value("Your choice ", Validator.action)

    def run_action(self):
        switcher = {
            'N': self.new_visit_card,
            'V': self.show_visit_card,
            'L': self.show_list_of_visit_cards,
            'E': self.edit_visit_card,
            'D': self.delete_visit_card
        }

        func = switcher.get(self.choice, "invalid choice")
        return func()

    def new_visit_card(self):
        print("--- new card ---")
        name = input("Name: ")
        surname = input("Surname: ")
        birth_date = self.get_validated_value("Date of birth: ", Validator.date)
        city = input("City: ")
        self.visit_card_manager.add_card(name, surname, city, birth_date)

    def show_visit_card(self):
        index = input("Index of card to show: ")
        self.visit_card_manager.show_card(int(index))

    def show_list_of_visit_cards(self):
        list_ = self.visit_card_manager.get_names_list()

        for card in list_:
            print("--- List of cards ---")
            print(f"  {list_.index(card)}: {card}")

    def edit_visit_card(self):
        index = input("Index of card to edit: ")

        print("  Parameters: ")
        for parameter in Parameter:
            print(f"    {parameter.name}")

        param = self.get_validated_value("Parameter to edit: ", Validator.parameter)
        if param == Parameter.BIRTHDAY.name:
            value = self.get_validated_value("Date of birth (dd-mm-rrrr): ", Validator.date)
        else:
            value = input("New value: ")

        self.visit_card_manager.edit_card(int(index), param, value)

    def delete_visit_card(self):
        index = input("Index of card to delete: ")
        self.visit_card_manager.delete_card(int(index))

    @staticmethod
    def get_validated_value(prompt, validation_func):
        param = ""

        while not validation_func(param):
            param = input(prompt)

        return param

