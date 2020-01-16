# name = input("Name: ")
# surname = input("Surname: ")
# birthDate = input("Date of birth (dd-mm-rrrr): ")
# city = input("City: ")

import re


def validate(date):
    re.compile("[1-31]-[1-12]-[1-2020]")
    if re.match(r"\d\d-\d\d-[1-2020]", date):
        print("date is good")
    else:
        print("date is bad")


def suffix_spaces(parameter_length):
    spaces = ""

    for _ in range(max_length - parameter_length):
        spaces += " "

    return spaces


def line():
    line_ = "      "

    for _ in range(prefix_length+max_length):
        line_ += "-"

    return line_


name = "Richard"
surname = "Feynman"
birthday = "1-05-1918"
validate(birthday)
city = "Los Angeles"

name_and_surname_length = len(f"{name} {surname}")
birthday_length = len(f"{birthday}")
city_length = len(f"{city}")

max_length = max([name_and_surname_length, birthday_length, city_length])
prefix_length = 20

initials = f"{name[0]}.{surname[0]}."

print(f"{line()}")
print(f"     | Name and surname: {name} {surname} {suffix_spaces(name_and_surname_length)}|")
print(f"{initials} | Birth date:       {birthday} {suffix_spaces(birthday_length)}|")
print(f"     | City:             {city} {suffix_spaces(city_length)}|")
print(f"{line()}")


