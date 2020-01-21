from enum import Enum
from .VisitCard import VisitCard


class Parameter(Enum):
    NAME = 1
    SURNAME = 2
    BIRTHDAY = 3
    CITY = 4


class VisitCardManager:
    def __init__(self):
        self.card_list = []

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

        if parameter not in Parameter.__members__:
            print("invalid parameter")
            return

        self.card_list[index].__dict__[parameter.lower()] = value

    def delete_card(self, index):
        if index > len(self.card_list):
            print("invalid index")
            return

        del self.card_list[index]
