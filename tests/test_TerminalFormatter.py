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
    tax: 0.07750604831243847
    ec2: 0.00023062766560844955
    compute: 0.00023062766560844955
    s3: 0.06277746863558648
    workmail: 0.0005650859427642049
    cloudwatch: 0.01622120972822173
    sns: 0.33792137932933264
    route53: 0.00044697600173265045
    rds: 0.0019059481681484788
    codecommit: 0.0034959729024870434
    dynamodb: 0.0026248906690162195
    kms: 0.0016610571033699383
    cloudfront: 2.1378637410903408e-05
    efs: 0.0008907188622516529
    ce: 1.292191698499126e-06
    TOTAL: 0.5065006818156758
2017-05-10:
    tax: 0.0270957561413653
    ec2: 0.2606873031952407
    compute: 6.991959144333819e-05
    s3: 0.013362197214836651
    workmail: 0.0017843835819167377
    cloudwatch: 0.35781953456089244
    sns: 0.22200739727958446
    route53: 0.011544074348980738
    rds: 0.030156378441861344
    codecommit: 0.003198798955589783
    dynamodb: 0.0065967739382003275
    kms: 5.90082810675901e-05
    cloudfront: 0.000837491200090579
    efs: 0.002326208935844471
    ce: 0.00022346884799679583
    TOTAL: 0.9377686945149113
2017-05-11:
    tax: 0.3716383862048105
    ec2: 0.0013544868433794071
    compute: 0.0019787699609398485
    s3: 0.1863271395640563
    workmail: 0.014989036544669394
    cloudwatch: 0.08101186362064511
    sns: 0.006452084779391441
    route53: 0.028675412093054266
    rds: 0.028675412093054266
    codecommit: 0.08634450604532178
    dynamodb: 0.015171487411262383
    kms: 0.00029279515269651585
    cloudfront: 0.009717306916773654
    efs: 0.013094107931944828
    ce: 1.0036605315467037e-05
    TOTAL: 0.8457328317673153
2017-05-12:
    tax: 0.00587164869451952
    ec2: 0.736754368657322
    compute: 0.0541338762984979
    s3: 0.0253198289418126
    workmail: 0.00132222073376983
    cloudwatch: 0.000203127889969165
    sns: 0.00222109692636827
    route53: 0.00178406610111942
    rds: 0.000428806746532002
    codecommit: 3.15446211876148e-06
    dynamodb: 0.000142014743730588
    kms: 6.37980431704079e-05
    cloudfront: 2.50960903483979e-05
    efs: 6.13661984855237e-06
    ce: 0.000109675243509909
    TOTAL: 0.8283889161926373
2017-05-13:
    tax: 0.0299832912632027
    ec2: 0.372927787199885
    compute: 0.000797423115319135
    s3: 0.147615957271569
    workmail: 0.231040508438865
    cloudwatch: 0.0329626398249305
    sns: 0.00579219649437249
    route53: 0.0020068905186178
    rds: 1.15841295916939e-05
    codecommit: 0.00266443381913916
    dynamodb: 0.000222039088770916
    kms: 0.000294786357069851
    cloudfront: 0.00057829454181199
    efs: 8.9047393279388e-05
    ce: 6.03317401480726e-06
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
