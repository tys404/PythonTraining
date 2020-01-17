from .Validator import Validator
import datetime


class VisitCard:
    def __init__(self, name, surname, birth_date_input, city):
        self.birthday = datetime.date(1900, 1, 1)
        self.modify_birthday(birth_date_input)
        self.name = name
        self.surname = surname
        self.city = city

    def modify_birthday(self, date):
        if Validator.date(date):
            day = int(date[0:2])
            month = int(date[3:5])
            year = int(date[6:])
            self.birthday = datetime.date(year, month, day)
        else:
            pass

