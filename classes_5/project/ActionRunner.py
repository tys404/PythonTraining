from .Validator import Validator
from .VisitCardManager import Parameter


class ActionRunner:
    def __init__(self, visit_card_manager, ui):
        self.visit_card_manager = visit_card_manager
        self.ui = ui

    def new_visit_card(self):
        print("--- new card ---")
        name = input("Name: ")
        surname = input("Surname: ")
        birth_date = self.ui.get_validated_value("Date of birth: ", Validator.date)
        city = input("City: ")
        self.visit_card_manager.add_card(name, surname, city, birth_date)

    def show_visit_card(self):
        index = input("Index of card to show: ")
        self.visit_card_manager.show_card(int(index))

    def show_list_of_visit_cards(self):
        list_ = self.visit_card_manager.get_names_list()

        print("--- List of cards ---")
        for card in list_:
            print(f"  {list_.index(card)}: {card}")

        print()

    def edit_visit_card(self):
        index = input("Index of card to edit: ")
        self.ui.print_parameters()
        param = self.ui.get_validated_value("Parameter to edit: ", Validator.parameter)

        if param == Parameter.BIRTHDAY.name:
            value = self.ui.get_validated_value("Date of birth (dd-mm-rrrr): ", Validator.date)
        else:
            value = input("New value: ")

        self.visit_card_manager.edit_card(int(index), param, value)

    def delete_visit_card(self):
        if len(self.visit_card_manager.card_list) == 0:
            print("Card list is empty\n")
            return

        index = input("Index of card to delete: ")
        self.visit_card_manager.delete_card(int(index))
