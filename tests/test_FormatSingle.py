import sys
import unittest
sys.path.insert(1, "..")
from aws_costs_cli.FormatSingle import FormatSingle

class test_FormatSingle(unittest.TestCase):

    def setUp(self):
        self.formatSingle = FormatSingle(self.__return_test_dict())

    def test_getMonthDay(self):
        expected_string = "01-13"
        returned_expression = self.formatSingle.getMonthDay()
        self.assertEqual(expected_string, returned_expression)

    def test_getAmount(self):
        expected_string = 2.0561094838
        returned_expression = self.formatSingle.getAmount()
        self.assertEqual(expected_string, returned_expression)

    def test_getAmountUnit(self):
        expected_string = "USD"
        returned_expression = self.formatSingle.getAmountUnit()
        self.assertEqual(expected_string, returned_expression)

    def __return_test_dict(self):
        return {
            "TimePeriod": {
                "Start": "2021-01-13",
                "End": "2021-01-14"
            },
            "Total": {
                "BlendedCost": {
                    "Amount": "2.0561094838",
                    "Unit": "USD"
                }
            },
            "Groups": [],
            "Estimated": False
        }

