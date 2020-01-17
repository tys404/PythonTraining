from unittest import TestCase
from ..project.VisitCardManager import VisitCardManager
import datetime
from ..project.VisitCardManager import Parameter


class TestVisitCardManager(TestCase):
    def setUp(self):
        self.visit_card_manager = VisitCardManager()
        self.visit_card_manager.add_card("Richard0", "Feynman", "11-05-1918", "Los Angeles")
        self.visit_card_manager.add_card("Richard1", "Feynman", "11-05-1918", "Los Angeles")
        self.visit_card_manager.add_card("Richard2", "Feynman", "11-05-1918", "Los Angeles")
        self.visit_card_manager.add_card("Richard3", "Feynman", "11-05-1918", "Los Angeles")


class TestAddCard(TestVisitCardManager):
    def test_add_one_card(self):
        self.visit_card_manager.add_card("Richard4", "Feynman4", "04-04-1904", "Los Angeles")
        self.assertEqual(self.visit_card_manager.card_list[4].name, "Richard4")
        self.assertEqual(self.visit_card_manager.card_list[4].surname, "Feynman4")
        self.assertEqual(self.visit_card_manager.card_list[4].birthday, datetime.date(1904, 4, 4))
        self.assertEqual(self.visit_card_manager.card_list[4].city, "Los Angeles")

    def test_add_more_cards(self):
        self.visit_card_manager.add_card("Richard4", "Feynman", "11-05-1918", "Los Angeles")
        self.visit_card_manager.add_card("Richard5", "Feynman", "11-05-1918", "Los Angeles")
        self.visit_card_manager.add_card("Richard6", "Feynman", "11-05-1918", "Los Angeles")
        self.visit_card_manager.add_card("Richard7", "Feynman7", "07-07-1907", "Los Angeles7")

        self.assertEqual(len(self.visit_card_manager.card_list), 8)
        self.assertEqual(self.visit_card_manager.card_list[7].name, "Richard7")
        self.assertEqual(self.visit_card_manager.card_list[7].surname, "Feynman7")
        self.assertEqual(self.visit_card_manager.card_list[7].birthday, datetime.date(1907, 7, 7))
        self.assertEqual(self.visit_card_manager.card_list[7].city, "Los Angeles7")


class TestGetNamesList(TestVisitCardManager):
    def test_name_list(self):
        name_list = self.visit_card_manager.get_names_list()

        self.assertEqual(name_list[0], "Richard0")
        self.assertEqual(name_list[1], "Richard1")
        self.assertEqual(name_list[2], "Richard2")
        self.assertEqual(name_list[3], "Richard3")


class TestEditItem(TestVisitCardManager):
    def test_edit_name(self):
        self.visit_card_manager.edit_card(0, Parameter.NAME, "John")
        self.visit_card_manager.edit_card(2, Parameter.NAME, "Felix")

        self.assertEqual(self.visit_card_manager.card_list[0].name, "John")
        self.assertEqual(self.visit_card_manager.card_list[2].name, "Felix")
        self.assertEqual(self.visit_card_manager.card_list[1].name, "Richard1")
        self.assertEqual(self.visit_card_manager.card_list[3].name, "Richard3")

    def test_edit_surname(self):
        self.visit_card_manager.edit_card(0, Parameter.SURNAME, "John")
        self.visit_card_manager.edit_card(2, Parameter.SURNAME, "Felix")

        self.assertEqual(self.visit_card_manager.card_list[0].surname, "John")
        self.assertEqual(self.visit_card_manager.card_list[2].surname, "Felix")
        self.assertEqual(self.visit_card_manager.card_list[1].surname, "Feynman")
        self.assertEqual(self.visit_card_manager.card_list[3].surname, "Feynman")

    def test_edit_birthday(self):
        self.visit_card_manager.edit_card(0, Parameter.BIRTHDAY, datetime.date(1992, 5, 7))
        self.visit_card_manager.edit_card(2, Parameter.BIRTHDAY, datetime.date(1990, 1, 1))

        self.assertEqual(self.visit_card_manager.card_list[0].birthday, datetime.date(1992, 5, 7))
        self.assertEqual(self.visit_card_manager.card_list[2].birthday, datetime.date(1990, 1, 1))
        self.assertEqual(self.visit_card_manager.card_list[1].birthday, datetime.date(1918, 5, 11))
        self.assertEqual(self.visit_card_manager.card_list[3].birthday, datetime.date(1918, 5, 11))

    def test_edit_city(self):
        self.visit_card_manager.edit_card(0, Parameter.CITY, "New York")
        self.visit_card_manager.edit_card(2, Parameter.CITY, "Washington")

        self.assertEqual(self.visit_card_manager.card_list[0].city, "New York")
        self.assertEqual(self.visit_card_manager.card_list[2].city, "Washington")
        self.assertEqual(self.visit_card_manager.card_list[1].city, "Los Angeles")
        self.assertEqual(self.visit_card_manager.card_list[3].city, "Los Angeles")


class TestDelete(TestVisitCardManager):
    def test_delete_one(self):
        self.visit_card_manager.delete_card(0)

        self.assertEqual(len(self.visit_card_manager.card_list), 3)
        self.assertEqual(self.visit_card_manager.card_list[0].name, "Richard1")

    def test_delete_multiple(self):
        self.visit_card_manager.delete_card(0)
        self.visit_card_manager.delete_card(0)
        self.visit_card_manager.delete_card(0)

        self.assertEqual(len(self.visit_card_manager.card_list), 1)
        self.assertEqual(self.visit_card_manager.card_list[0].name, "Richard3")
