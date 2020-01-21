import re

class Validator:
    @staticmethod
    def is_lap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
            return True
        else:
            return False

    @staticmethod
    def date(date):
        if not re.match(r"[0-3][0-9]-[0-3][0-9]-[0-2][0-9][0-9][0-9]", date):
            return False

        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:])

        if day == 0 or month == 0 or year == 0:
            return False

        if month > 12:
            return False

        if month in months_31 and day > 31:
            return False

        if month in months_30 and day > 30:
            return False

        if month == 2 and Validator.is_lap_year(year) and day > 29:
            return False

        if month == 2 and not Validator.is_lap_year(year) and day > 28:
            return False

        return True

    @staticmethod
    def menu_choice(choice):
        if (
                not isinstance(choice, str) or
                len(choice) > 1 or
                not re.match(r"[NVLEDX]", choice)
        ):
            return False
        else:
            return True

    @staticmethod
    def visit_card_parameter(param):
        from ..project.VisitCardManager import Parameter
        is_valid = False

        for enumParameter in Parameter:
            if param == enumParameter.name:
                is_valid = True

        return is_valid

    @staticmethod
    def index(value, list_):
        try:
            value = int(value)
        except (ValueError, TypeError):
            return False

        max_index = len(list_) - 1
        if value < 0 or value > max_index:
            return False
        else:
            return True

    @staticmethod
    def string_nonempty(value):
        if not isinstance(value, str) or len(value) == 0:
            return False
        else:
            return True
