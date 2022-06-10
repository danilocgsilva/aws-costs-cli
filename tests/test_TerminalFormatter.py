import unittest
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_api.AWSCosts import AWSCosts
from aws_api_mock.CostExplorer import CostExplorer
import io
import sys

class test_TerminalFormatter(unittest.TestCase):

    def setUp(self):
        self.terminal_formatter = TerminalFormatter()
    
    def test_get(self):

        costExplorerMocked = CostExplorer()
        costExplorerMocked.set_mock_count(5)
        awscosts = AWSCosts(costExplorerMocked)

        awscosts.getCosts()

        final_data = '''Month and day: 05-09
0.8283195865 USD
----
Month and day: 05-10
0.9383288394 USD
----
Month and day: 05-11
0.8283300322 USD
----
Month and day: 05-12
0.828390103 USD
----
Month and day: 05-13
0.8269931709 USD
----
Total from last month: 4.250361732 USD
---//---
Above, the last month day by day cost from AWS account.
'''

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.terminal_formatter.get(awscosts.getCosts())
        sys.stdout = sys.__stdout__

        self.assertEqual(final_data, capturedOutput.getvalue())

    def test_print_spread(self):
        self.assertEqual("needs", "works")
