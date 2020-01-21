from .Validator import Validator
from .VisitCardManager import Parameter, VisitCardManager
from .VisitCardPrinter import VisitCardPrinter
from .UI import UI


class ActionRunner:
    def __init__(self, ):
        self.manager = VisitCardManager()
        self.printer = VisitCardPrinter()

    def run(self, choice):
        switcher = {
            'N': self.new_visit_card,
            'V': self.show_visit_card,
            'L': self.show_list_of_visit_cards,
            'E': self.edit_visit_card,
            'D': self.delete_visit_card
        }

        func = switcher.get(choice, "invalid choice")
        return func()

    def new_visit_card(self):
        name, surname, birth_date_input, city = UI.get_new_visit_card_data()
        self.manager.add_card(name, surname, birth_date_input, city)

    def show_visit_card(self):
        index = UI.get_index(self.manager.card_list)
        card = self.manager.card_list[index]
        self.printer.print(card)

    def show_list_of_visit_cards(self):
        list_ = self.manager.get_names_list()

        print("--- List of cards ---")
        for card in list_:
            print(f"  {list_.index(card)}: {card}")

        print()

    def edit_visit_card(self):
        if len(self.manager.card_list) == 0:
            print("Card list is empty\n")
            return

        index = UI.get_index(self.manager.card_list)
        UI.print_parameters()
        param = UI.get_param_to_edit()
        value = UI.get_new_value(param)

        self.manager.edit_card(index, param, value)

    def delete_visit_card(self):
        if len(self.manager.card_list) == 0:
            print("Card list is empty\n")
            return

        index = UI.get_index(self.manager.card_list)
        self.manager.delete_card(index)
