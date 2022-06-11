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
0.5065006818156758 USD
----
Month and day: 05-10
0.9377686945149113 USD
----
Month and day: 05-11
0.8457328317673153 USD
----
Month and day: 05-12
0.8283889161926373 USD
----
Month and day: 05-13
0.8269929126304396 USD
----
Total from last month: 3.945384036920979 USD
---//---
Above, the last month day by day cost from AWS account.
'''

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.terminal_formatter.get(awscosts.getCosts())
        sys.stdout = sys.__stdout__

        self.assertEqual(final_data, capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()
