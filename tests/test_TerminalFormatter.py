import unittest
from aws_costs_cli.TerminalFormatter import TerminalFormatter

class test_TerminalFormatter(unittest.TestCase):

    def setUp(self):
        self.terminal_formatter = TerminalFormatter()
    
    def test_get(self):
        final_data = '''Month and day: 06-03
0.9729120419 USD
----
Month and day: 06-04
1.0782099815 USD
----
Month and day: 06-05
0.8775415891 USD
----
Month and day: 06-06
0.9419058029 USD
----
Month and day: 06-07
0.9818281561 USD
----
Total from last month: 29.462248903299997 USD
'''
        data_from_object = self.terminal_formatter.get({})
        self.assertEqual(final_data, data_from_object)