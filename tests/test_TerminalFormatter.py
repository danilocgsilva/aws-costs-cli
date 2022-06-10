import unittest
from aws_costs_cli.TerminalFormatter import TerminalFormatter
from aws_costs_api.AWSCosts import AWSCosts
from aws_costs_cli.functions import spread
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

        costExplorerMocked = CostExplorer()
        costExplorerMocked.set_mock_count(5)
        awscosts = AWSCosts(costExplorerMocked)

        data_all_services = spread(awscosts)
        self.terminal_formatter.set_all_data_services(data_all_services)
        self.terminal_formatter.print_spread()

        print(data_all_services)

        exit()

        terminal_formatter.set_all_data_services(data_all_services)

        expected_output = '''2022-06-06:
    tax: 0.0
    ec2: 0.1318400459
    compute: 0.0073056648
    s3: 0.3583520821
    workmail: 0.4000000032
    cloudwatch: 0.0
    sns: 0.0
    route53: 4.48e-05
    rds: 0.0110297581
    codecommit: 0.0
    dynamodb: 0.0
    kms: 0.0333333336
    cloudfront: 7.2e-09
    efs: 1.08e-07
    ce: 0.0
    TOTAL: 0.9419058029000001
2022-06-07:
    tax: 0.0
    ec2: 0.17108143
    compute: 0.0191135028
    s3: 0.3583790942
    workmail: 0.4000000032
    cloudwatch: 0.0
    sns: 0.0
    route53: 3.92e-05
    rds: 0.0110297581
    codecommit: 0.0
    dynamodb: 0.0
    kms: 0.0333333336
    cloudfront: 1.44e-08
    efs: 1.08e-07
    ce: 0.0
    TOTAL: 0.9929764443000001
2022-06-08:
    tax: 0.0
    ec2: 0.067777781
    compute: 0.0007653324
    s3: 0.3583048832
    workmail: 0.4000000032
    cloudwatch: 0.0
    sns: 0.0
    route53: 3.72e-05
    rds: 0.0110297581
    codecommit: 0.0
    dynamodb: 0.0
    kms: 0.0333333336
    cloudfront: 7.2e-09
    efs: 1.08e-07
    ce: 0.17
    TOTAL: 1.0412484067
2022-06-09:
    tax: 0.0
    ec2: 0.0799999992
    compute: 0.0
    s3: 0.3583537058
    workmail: 0.4000000032
    cloudwatch: 0.0
    sns: 0.0
    route53: 3.08e-05
    rds: 0.0110297581
    codecommit: 0.0
    dynamodb: 0.0
    kms: 0.0333333336
    cloudfront: 1.44e-08
    efs: 1.08e-07
    ce: 0.02
    TOTAL: 0.9027477223
2022-06-10:
    tax: 0.0
    ec2: 0.0766666659
    compute: 0.0
    s3: 0.3583488248
    workmail: 0.4000000032
    cloudwatch: 0.0
    sns: 0.0
    route53: 3.6e-05
    rds: 0.0110173657
    codecommit: 0.0
    dynamodb: 0.0
    kms: 0.0305555558
    cloudfront: 7.2e-09
    efs: 1.08e-07
    ce: 2.04
    TOTAL: 2.9166245306
'''

        self.assertEqual(expected_output, "works")

if __name__ == '__main__':
    unittest.main()
