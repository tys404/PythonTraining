import re
import datetime

# name = input("Name: ")
# surname = input("Surname: ")
# birthday_input = input("Date of birth (dd-mm-rrrr): ")
# city = input("City: ")

name = "Richard"
surname = "Feynman"
birthday_input = "01-05-1918"
city = "Los Angeles"

today = datetime.date.today()
day = int(birthday_input[0:2])
month = int(birthday_input[3:5])
year = int(birthday_input[6:])
birthday = datetime.date(year, month, day)

name_and_surname_length = len(f"{name} {surname}")
birthday_length = len(f"{birthday}")
city_length = len(f"{city}")

max_length = max([name_and_surname_length, birthday_length, city_length])
prefix_length = 20

initials = f"{name[0]}.{surname[0]}."


def calculate_length():
    global max_length
    global name_and_surname_length
    global birthday_length
    global city_length

    name_and_surname_length = len(f"{name} {surname}")
    birthday_length = len(f"{birthday}")
    city_length = len(f"{city}")

    max_length = max([name_and_surname_length, birthday_length, city_length])


def validate(date_):
    re.compile("[1-31]-[1-12]-[1-2020]")
    if re.match(r"\d\d-\d\d-[1-2020]", date_):
        print("date is good")
        return True
    else:
        print("date is bad")
        return False


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


def modify_name():
    global name
    new_name = input("New name: ")
    name = new_name
    calculate_length()


def modify_surname():
    global surname
    new_surname = input("New surname: ")
    surname = new_surname
    calculate_length()


def modify_birthday():
    global birthday_input, day, month, year, birthday
    is_valid = False
    while not is_valid:
        new_birthday = input("New birth date (dd-mm-yyyy): ")
        is_valid = validate(new_birthday)

    birthday_input = new_birthday
    day = int(birthday_input[0:2])
    month = int(birthday_input[3:5])
    year = int(birthday_input[6:])
    birthday = datetime.date(year, month, day)


def modify_city():
    global city
    new_city = input("New city: ")
    city = new_city
    calculate_length()


def show_years():
    delta = year - today.year

    print(f"Age in years: {-delta}")


def show_days():
    delta = today - birthday

    print(f"Age in days: {delta.days}")


def show_visit_card():
    print(f"{line()}")
    print(f"     | Name and surname: {name} {surname} {suffix_spaces(name_and_surname_length)}|")
    print(f"{initials} | Birth date:       {birthday} {suffix_spaces(birthday_length)}|")
    print(f"     | City:             {city} {suffix_spaces(city_length)}|")
    print(f"{line()}")


def print_menu():
    print("modify [N]ame")
    print("modify [S]urname")
    print("modify [B]irth date")
    print("modify [C]ity")
    print("show age in [Y]ears")
    print("show age in [D]ays")
    print("show [V]isit card")


def run_choice(choice_):
    switcher = {
        'N': modify_name,
        'S': modify_surname,
        'B': modify_birthday,
        'C': modify_city,
        'Y': show_years,
        'D': show_days,
        'V': show_visit_card
    }

    func = switcher.get(choice_, "invalid choice")
    return func()


name_and_surname_length = len(f"{name} {surname}")
birthday_length = len(f"{birthday}")
city_length = len(f"{city}")

max_length = max([name_and_surname_length, birthday_length, city_length])
prefix_length = 20

initials = f"{name[0]}.{surname[0]}."

show_visit_card()

while True:
    print_menu()
    choice = input("Your choice: ")
    run_choice(choice)
    print()
