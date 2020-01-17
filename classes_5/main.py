from classes_5.project.UI import *

ui = UI()
ui.visit_card_manager.add_card("Krzysztof", "Tys", "01-01-1991", "DG")

while True:
    ui.print_menu()
    ui.get_choice()
    ui.run_action()
