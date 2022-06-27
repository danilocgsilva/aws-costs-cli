import unittest
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_api.AWSCosts import AWSCosts
from aws_api_mock.CostExplorer import CostExplorer
import io
import sys
from aws_costs_cli.SpreadCalculator import SpreadCalculator

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

    def test_print_spread(self):

        costExplorerMocked = CostExplorer()
        costExplorerMocked.set_mock_count(5)
        awscosts = AWSCosts(costExplorerMocked)

        spreadCalculator = SpreadCalculator()
        spreadCalculator.set_client(awscosts)
        data_all_services = spreadCalculator.get_data()
        self.terminal_formatter.set_all_data_services(data_all_services)

        expected_result = '''2017-05-09:
    tax: 0.07750604831243847 (15.3%)
    ec2: 0.00023062766560844955 (0.05%)
    compute: 0.00023062766560844955 (0.05%)
    s3: 0.06277746863558648 (12.39%)
    workmail: 0.0005650859427642049 (0.11%)
    cloudwatch: 0.01622120972822173 (3.2%)
    sns: 0.33792137932933264 (66.72%)
    route53: 0.00044697600173265045 (0.09%)
    rds: 0.0019059481681484788 (0.38%)
    codecommit: 0.0034959729024870434 (0.69%)
    dynamodb: 0.0026248906690162195 (0.52%)
    kms: 0.0016610571033699383 (0.33%)
    cloudfront: 2.1378637410903408e-05 (0.0%)
    efs: 0.0008907188622516529 (0.18%)
    ce: 1.292191698499126e-06 (0.0%)
    TOTAL: 0.5065006818156758
2017-05-10:
    tax: 0.0270957561413653 (2.89%)
    ec2: 0.2606873031952407 (27.8%)
    compute: 6.991959144333819e-05 (0.01%)
    s3: 0.013362197214836651 (1.42%)
    workmail: 0.0017843835819167377 (0.19%)
    cloudwatch: 0.35781953456089244 (38.16%)
    sns: 0.22200739727958446 (23.67%)
    route53: 0.011544074348980738 (1.23%)
    rds: 0.030156378441861344 (3.22%)
    codecommit: 0.003198798955589783 (0.34%)
    dynamodb: 0.0065967739382003275 (0.7%)
    kms: 5.90082810675901e-05 (0.01%)
    cloudfront: 0.000837491200090579 (0.09%)
    efs: 0.002326208935844471 (0.25%)
    ce: 0.00022346884799679583 (0.02%)
    TOTAL: 0.9377686945149113
2017-05-11:
    tax: 0.3716383862048105 (43.94%)
    ec2: 0.0013544868433794071 (0.16%)
    compute: 0.0019787699609398485 (0.23%)
    s3: 0.1863271395640563 (22.03%)
    workmail: 0.014989036544669394 (1.77%)
    cloudwatch: 0.08101186362064511 (9.58%)
    sns: 0.006452084779391441 (0.76%)
    route53: 0.028675412093054266 (3.39%)
    rds: 0.028675412093054266 (3.39%)
    codecommit: 0.08634450604532178 (10.21%)
    dynamodb: 0.015171487411262383 (1.79%)
    kms: 0.00029279515269651585 (0.03%)
    cloudfront: 0.009717306916773654 (1.15%)
    efs: 0.013094107931944828 (1.55%)
    ce: 1.0036605315467037e-05 (0.0%)
    TOTAL: 0.8457328317673153
2017-05-12:
    tax: 0.00587164869451952 (0.71%)
    ec2: 0.736754368657322 (88.94%)
    compute: 0.0541338762984979 (6.53%)
    s3: 0.0253198289418126 (3.06%)
    workmail: 0.00132222073376983 (0.16%)
    cloudwatch: 0.000203127889969165 (0.02%)
    sns: 0.00222109692636827 (0.27%)
    route53: 0.00178406610111942 (0.22%)
    rds: 0.000428806746532002 (0.05%)
    codecommit: 3.15446211876148e-06 (0.0%)
    dynamodb: 0.000142014743730588 (0.02%)
    kms: 6.37980431704079e-05 (0.01%)
    cloudfront: 2.50960903483979e-05 (0.0%)
    efs: 6.13661984855237e-06 (0.0%)
    ce: 0.000109675243509909 (0.01%)
    TOTAL: 0.8283889161926373
2017-05-13:
    tax: 0.0299832912632027 (3.63%)
    ec2: 0.372927787199885 (45.09%)
    compute: 0.000797423115319135 (0.1%)
    s3: 0.147615957271569 (17.85%)
    workmail: 0.231040508438865 (27.94%)
    cloudwatch: 0.0329626398249305 (3.99%)
    sns: 0.00579219649437249 (0.7%)
    route53: 0.0020068905186178 (0.24%)
    rds: 1.15841295916939e-05 (0.0%)
    codecommit: 0.00266443381913916 (0.32%)
    dynamodb: 0.000222039088770916 (0.03%)
    kms: 0.000294786357069851 (0.04%)
    cloudfront: 0.00057829454181199 (0.07%)
    efs: 8.9047393279388e-05 (0.01%)
    ce: 6.03317401480726e-06 (0.0%)
    TOTAL: 0.8269929126304396
'''

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.terminal_formatter.print_spread()
        sys.stdout = sys.__stdout__
        generated_data = capturedOutput.getvalue()

        self.assertEqual(expected_result, generated_data)

if __name__ == '__main__':
    unittest.main()
