from classes_5.project import VisitCardUI
from classes_5.project.ActionRunner import ActionRunner

action_runner = ActionRunner()
action_runner.manager.add_card("Krzysztof", "Tys", "01-01-1991", "DG")

while True:
    VisitCardUI.print_menu()
    choice = VisitCardUI.get_choice()

    if choice == 'X':
        break

    action_runner.run(choice)
