from .Validator import Validator


class Ask:
    @staticmethod
    def until_valid(prompt, validation_func, *args):
        param = ""

        if len(args) == 0:
            param = Ask.simple(prompt, validation_func)
        elif len(args) == 1 and isinstance(args[0], list):
            param = Ask.index(prompt, validation_func, args[0])
        else:
            print("Error. Validator not found.")

        return param

    @staticmethod
    def simple(prompt, validation_func):
        param = ""

        while not validation_func(param):
            param = input(prompt)

        return param

    @staticmethod
    def index(prompt, list_):
        param = ''

        while not Validator.index(param, list_):
            param = input(prompt)

        return int(param)

    @staticmethod
    def menu_choice(prompt):
        return Ask.until_valid(prompt, Validator.menu_choice)

    @staticmethod
    def date(prompt):
        return Ask.until_valid(prompt, Validator.date)

    @staticmethod
    def string_nonempty(prompt):
        return Ask.until_valid(prompt, Validator.string_nonempty)

    @staticmethod
    def visit_card_parameter(prompt):
        return Ask.until_valid(prompt, Validator.visit_card_parameter)
