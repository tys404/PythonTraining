from classes_5.project.UI import *
from classes_5.project.ActionRunner import *
from classes_5.project.UI import UI
action_runner = ActionRunner()
action_runner.manager.add_card("Krzysztof", "Tys", "01-01-1991", "DG")

while True:
    UI.print_menu()
    choice = UI.get_choice()

    if choice == 'X':
        break

    action_runner.run(choice)
