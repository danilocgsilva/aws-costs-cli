from ast import expr_context
import unittest
from aws_costs_cli.functions import spread
from aws_costs_api.AWSCosts import AWSCosts
from aws_api_mock.CostExplorer import CostExplorer

class test_spread(unittest.TestCase):

    def test_spread(self):

        constExplorerClientMocked = CostExplorer()
        constExplorerClientMocked.set_mock_count(5)
        awscosts = AWSCosts(constExplorerClientMocked)

        expected_output = '''{
    "2022-06-07": {
        "tax": 0.0,
        "ec2": 0.17108143,
        "compute": 0.0191135028,
        "s3": 0.3583790942,
        "workmail": 0.4000000032,
        "cloudwatch": 0.0,
        "sns": 0.0,
        "route53": 3.92e-05,
        "rds": 0.0110297581,
        "codecommit": 0.0,
        "dynamodb": 0.0,
        "kms": 0.0333333336,
        "cloudfront": 1.44e-08,
        "efs": 1.08e-07,
        "ce": 0.0,
        "TOTAL": 0.9929764443000001
    },
    "2022-06-08": {
        "tax": 0.0,
        "ec2": 0.067777781,
        "compute": 0.0007653324,
        "s3": 0.3583048832,
        "workmail": 0.4000000032,
        "cloudwatch": 0.0,
        "sns": 0.0,
        "route53": 3.72e-05,
        "rds": 0.0110297581,
        "codecommit": 0.0,
        "dynamodb": 0.0,
        "kms": 0.0333333336,
        "cloudfront": 7.2e-09,
        "efs": 1.08e-07,
        "ce": 0.17,
        "TOTAL": 1.0412484067
    },
    "2022-06-09": {
        "tax": 0.0,
        "ec2": 0.0799999992,
        "compute": 0.0,
        "s3": 0.3583537058,
        "workmail": 0.4000000032,
        "cloudwatch": 0.0,
        "sns": 0.0,
        "route53": 3.08e-05,
        "rds": 0.0110297581,
        "codecommit": 0.0,
        "dynamodb": 0.0,
        "kms": 0.0333333336,
        "cloudfront": 1.44e-08,
        "efs": 1.08e-07,
        "ce": 0.02,
        "TOTAL": 0.9027477223
    },
    "2022-06-10": {
        "tax": 0.0,
        "ec2": 0.0766666659,
        "compute": 0.0,
        "s3": 0.3583488248,
        "workmail": 0.4000000032,
        "cloudwatch": 0.0,
        "sns": 0.0,
        "route53": 3.6e-05,
        "rds": 0.0110173657,
        "codecommit": 0.0,
        "dynamodb": 0.0,
        "kms": 0.0305555558,
        "cloudfront": 7.2e-09,
        "efs": 1.08e-07,
        "ce": 2.04,
        "TOTAL": 2.9166245306
    }
}
'''
        spread_return = spread(awscosts)

        print(spread_return)
        
        self.assertEqual(expected_output, spread_return)

if __name__ == '__main__':
    unittest.main()

