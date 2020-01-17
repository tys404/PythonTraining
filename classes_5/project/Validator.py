
import re


class Validator:
    @staticmethod
    def date(date):
        if re.match(r"[0-3][0-9]-[0-3][0-9]-[1-2][0-9][0-9][0-9]", date):
            return True
        else:
            return False

    @staticmethod
    def choice(choice):
        if re.match(r"[NVLE]", choice):
            return True
        else:
            return False
