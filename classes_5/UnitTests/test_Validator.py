from unittest import TestCase
from ..project.Validator import Validator


class TestValidator(TestCase):
    def setUp(self):
        self.validator = Validator()


class DateValidation(TestValidator):
    def test_lap_year_correct(self):
        lap_year = 2012
        lap_year_2 = 2020
        lap_year_3 = 1984
        lap_year_100 = 2000
        lap_year_100_2 = 2400

        lap_years = [lap_year, lap_year_2, lap_year_3, lap_year_100, lap_year_100_2]

        for year in lap_years:
            self.assertTrue(self.validator.is_lap_year(year), f"{year}")

    def test_lap_year_incorrect(self):
        non_lap_year = 2011
        non_lap_year_2 = 2021
        non_lap_year_3 = 1985
        non_lap_year_100 = 1800
        non_lap_year_100_2 = 1900

        lap_years = [non_lap_year, non_lap_year_2, non_lap_year_3, non_lap_year_100, non_lap_year_100_2]

        for year in lap_years:
            self.assertFalse(self.validator.is_lap_year(year), f"{year}")

    def test_date_correct(self):
        date_january = "31-01-1900"
        date_february = "28-02-1900"
        date_february_lap = "29-02-2012"
        date_march = "31-03-1990"
        date_april = "30-04-1990"
        date_may = "31-05-1990"
        date_june = "30-06-1990"
        date_july = "31-07-1990"
        date_august = "31-08-1990"
        date_september = "30-09-1990"
        date_october = "31-10-1990"
        date_november = "30-11-1990"
        date_december = "31-12-1990"

        dates = [date_january, date_february, date_february_lap, date_march,
                 date_april, date_may, date_june, date_july, date_august,
                 date_september, date_october, date_november, date_december]

        for date in dates:
            self.assertTrue(self.validator.date(date), f"Should be valid date: {date}")

    def test_date_incorrect(self):
        date_january = "32-01-1900"
        date_february = "29-02-1900"
        date_february_lap = "30-02-2012"
        date_march = "32-03-1990"
        date_april = "31-04-1990"
        date_may = "32-05-1990"
        date_june = "31-06-1990"
        date_july = "32-07-1990"
        date_august = "32-08-1990"
        date_september = "31-09-1990"
        date_october = "32-10-1990"
        date_november = "31-11-1990"
        date_december = "32-12-1990"
        date_month_13 = "01-13-1999"
        date_month_20 = "01-20-1999"
        date_month_50 = "01-50-1999"
        date_month_99 = "01-99-1999"
        date_day_nozero = "1-01-1991"
        date_month_nozero = "01-1-1991"
        date_nozero = "1-1-1991"
        date_day_zero = "00-01-1991"
        date_month_zero = "01-00-1991"
        date_year_zero = "01-01-0000"
        date_zeros = "0-0-0000"

        dates = [date_january, date_february, date_february_lap, date_march,
                 date_april, date_may, date_june, date_july, date_august,
                 date_september, date_october, date_november, date_december,
                 date_month_13, date_month_20, date_month_50, date_month_99,
                 date_day_nozero, date_month_nozero, date_nozero, date_day_zero,
                 date_month_zero, date_year_zero, date_zeros]

        for date in dates:
            self.assertFalse(self.validator.date(date), f"Should not be valid date: {date}")


class TestChoice(TestValidator):
    def test_choice_correct(self):
        choices = ['N', 'V', 'L', 'E', 'D']

        for choice in choices:
            self.assertTrue(self.validator.action(choice), f"{choice}")

    def test_choice_incorrect(self):
        choices = ['n', 'v', 'l', 'e', 'd']

        for choice in choices:
            self.assertFalse(self.validator.action(choice), f"{choice}")


class TestParams(TestValidator):
    def test_parameter_correct(self):
        parameters = ["NAME", "SURNAME", "BIRTHDAY", "CITY"]

        for param in parameters:
            self.assertTrue(self.validator.parameter(param), f"{param}")

    def test_parameter_incorrect(self):
        parameters = ["name", "surname", "birthday", "city"]

        for param in parameters:
            self.assertFalse(self.validator.parameter(param), f"{param}")

