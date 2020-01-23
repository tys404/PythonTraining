from .Validator import Validator


def until_valid(prompt, validation_func, *args):
    param = ""

    if len(args) == 0:
        param = simple(prompt, validation_func)
    elif len(args) == 1 and isinstance(args[0], list):
        param = index(prompt, validation_func, args[0])
    else:
        print("Error. Validator not found.")

    return param


def simple(prompt, validation_func):
    param = ""

    while not validation_func(param):
        param = input(prompt)

    return param


def index(prompt, list_):
    param = ''

    while not Validator.index(param, list_):
        param = input(prompt)

    return int(param)


def menu_choice(prompt):
    return until_valid(prompt, Validator.menu_choice)


def date(prompt):
    return until_valid(prompt, Validator.date)


def string_nonempty(prompt):
    return until_valid(prompt, Validator.string_nonempty)


def visit_card_parameter(prompt):
    return until_valid(prompt, Validator.visit_card_parameter)
