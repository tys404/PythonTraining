
class VisitCardPrinter:
    def __init__(self):
        self.prefix_length = 20
        self.max_length = 0

    def print(self, visit_card):
        self.calculate_lengths(visit_card)
        name = visit_card.name
        surname = visit_card.surname
        birthday = visit_card.birthday
        city = visit_card.city
        initials = f"{name[0]}.{surname[0]}."

        print(f"{self.line()}")
        print(f"     | Name and surname: {name} {surname} {self.suffix_spaces(name, surname)}|")
        print(f"{initials} | Birth date:       {birthday} {self.suffix_spaces(birthday)}|")
        print(f"     | City:             {city} {self.suffix_spaces(city)}|")
        print(f"{self.line()}")

    def calculate_lengths(self, visit_card):
        name_and_surname_length = len(f"{visit_card.name} {visit_card.surname}")
        birthday_length = len(f"{visit_card.birthday}")
        city_length = len(f"{visit_card.city}")
        self.max_length = max([name_and_surname_length, birthday_length, city_length])

    def suffix_spaces(self, param1, param2=""):
        parameter_length = len(f"{param1}{param2}")
        if param2 != "":
            parameter_length += 1

        spaces = ""
        for _ in range(self.max_length - parameter_length):
            spaces += " "

        return spaces

    def line(self):
        line_ = "      "
        for _ in range(self.prefix_length + self.max_length):
            line_ += "-"

        return line_


