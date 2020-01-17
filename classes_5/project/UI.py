from .ActionRunner import ActionRunner
from .VisitCardManager import VisitCardManager, Parameter
from .Validator import Validator


class UI:
    def __init__(self):
        self.visit_card_manager = VisitCardManager()
        self.action_runner = ActionRunner(self.visit_card_manager, self)
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
            'N': self.action_runner.new_visit_card,
            'V': self.action_runner.show_visit_card,
            'L': self.action_runner.show_list_of_visit_cards,
            'E': self.action_runner.edit_visit_card,
            'D': self.action_runner.delete_visit_card
        }

        func = switcher.get(self.choice, "invalid choice")
        return func()

    @staticmethod
    def get_validated_value(prompt, validation_func):
        param = ""

        while not validation_func(param):
            param = input(prompt)

        return param

    @staticmethod
    def print_parameters():
        print("  Parameters: ")
        for parameter in Parameter:
            print(f"    {parameter.name}")

