from enum import Enum

from .VisitCard import VisitCard
# from .VisitCardPrinter import VisitCardPrinter


class Parameter(Enum):
    NAME = 1
    SURNAME = 2
    BIRTHDAY = 3
    CITY = 4


class VisitCardManager:
    def __init__(self):
        self.card_list = []
        # self.card_printer = VisitCardPrinter()

    def add_card(self, name, surname, birth_date_input, city):
        card = VisitCard(name, surname, birth_date_input, city)
        self.card_list.append(card)

    def get_names_list(self):
        name_list = []
        for visit_card in self.card_list:
            name_list.append(visit_card.name)

        return name_list

    def edit_card(self, index, parameter, value):
        if index > len(self.card_list):
            print("invalid index")
            return

        if parameter == Parameter.NAME or parameter == Parameter.NAME.name:
            self.card_list[index].name = value
        elif parameter == Parameter.SURNAME or parameter == Parameter.SURNAME.name:
            self.card_list[index].surname = value
        elif parameter == Parameter.BIRTHDAY or parameter == Parameter.BIRTHDAY.name:
            self.card_list[index].birthday = value
        elif parameter == Parameter.CITY or parameter == Parameter.CITY.name:
            self.card_list[index].city = value
        else:
            print("invalid parameter")

    def delete_card(self, index):
        if index > len(self.card_list):
            print("invalid index")
            return

        del self.card_list[index]

    # def show_card(self, index):
    #     if index > len(self.card_list):
    #         print("invalid index")
    #         return
    #
    #     self.card_printer.print(self.card_list[index])
