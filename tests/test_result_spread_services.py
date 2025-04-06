import unittest
import sys
import io
sys.path.insert(1, "..")
from aws_costs_cli.functions import testprint
from aws_costs_cli.functions import result_spread_services
from aws_costs_cli.SpreadCalculator import SpreadCalculator
from aws_costs_api.AWSCosts import AWSCosts
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_api_mock.CostExplorer import CostExplorer
class test_result_spread_services(unittest.TestCase):

    # def test_result_spread_services(self):
    #     __result_spread_services

    def test_testprint(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        testprint()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Hello world!\n")


    def test_result_spread_services(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        costExplorerMocked = CostExplorer()
        costExplorerMocked.set_mock_count(5)
        awscosts = AWSCosts(costExplorerMocked)

        awscosts = AWSCosts()
        terminal_formatter = TerminalFormatter()

        result_spread_services(awscosts, terminal_formatter)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Hello world!\n")
        