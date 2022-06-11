import unittest
from aws_costs_cli.SpreadCalculator import SpreadCalculator
from aws_costs_api.AWSCosts import AWSCosts
from aws_api_mock.CostExplorer import CostExplorer


class test_SpreadCalculator(unittest.TestCase):

    def setUp(self):
        self.spreadCalculator = SpreadCalculator()

    def test_get_data(self):
        mocked_ce_client = CostExplorer()
        mocked_ce_client.set_mock_count(5)
        awscosts = AWSCosts(mocked_ce_client)
        self.spreadCalculator.set_client(awscosts)

        spread_calculations_get_data_results = {
            '2017-05-09': {
                'tax': 0.5065006818156758,
                'ec2': 0.5065006818156758, 
                'compute': 0.5065006818156758, 
                's3': 0.5065006818156758, 
                'workmail': 0.5065006818156758, 
                'cloudwatch': 0.5065006818156758, 
                'sns': 0.5065006818156758, 
                'route53': 0.5065006818156758, 
                'rds': 0.5065006818156758, 
                'codecommit': 0.5065006818156758, 
                'dynamodb': 0.5065006818156758, 
                'kms': 0.5065006818156758, 
                'cloudfront': 0.5065006818156758, 
                'efs': 0.5065006818156758, 
                'ce': 0.5065006818156758, 
                'TOTAL': 7.597510227235137
            }, 
            '2017-05-10': {
                'tax': 0.9377686945149113, 
                'ec2': 0.9377686945149113, 
                'compute': 0.9377686945149113, 
                's3': 0.9377686945149113, 
                'workmail': 0.9377686945149113, 
                'cloudwatch': 0.9377686945149113, 
                'sns': 0.9377686945149113, 
                'route53': 0.9377686945149113, 
                'rds': 0.9377686945149113, 
                'codecommit': 0.9377686945149113, 
                'dynamodb': 0.9377686945149113, 
                'kms': 0.9377686945149113, 
                'cloudfront': 0.9377686945149113, 
                'efs': 0.9377686945149113, 
                'ce': 0.9377686945149113, 
                'TOTAL': 14.066530417723671
            }, 
            '2017-05-11': {
                'tax': 0.8457328317673153, 
                'ec2': 0.8457328317673153, 
                'compute': 0.8457328317673153, 
                's3': 0.8457328317673153, 
                'workmail': 0.8457328317673153, 
                'cloudwatch': 0.8457328317673153, 
                'sns': 0.8457328317673153,
                'route53': 0.8457328317673153, 
                'rds': 0.8457328317673153, 
                'codecommit': 0.8457328317673153, 
                'dynamodb': 0.8457328317673153, 
                'kms': 0.8457328317673153, 
                'cloudfront': 0.8457328317673153, 
                'efs': 0.8457328317673153, 
                'ce': 0.8457328317673153, 
                'TOTAL': 12.685992476509725
            },
            '2017-05-12': {
                'tax': 0.8283889161926373, 
                'ec2': 0.8283889161926373, 
                'compute': 0.8283889161926373, 
                's3': 0.8283889161926373, 
                'workmail': 0.8283889161926373, 
                'cloudwatch': 0.8283889161926373, 
                'sns': 0.8283889161926373, 
                'route53': 0.8283889161926373, 
                'rds': 0.8283889161926373, 
                'codecommit': 0.8283889161926373, 
                'dynamodb': 0.8283889161926373, 
                'kms': 0.8283889161926373, 
                'cloudfront': 0.8283889161926373, 
                'efs': 0.8283889161926373, 
                'ce': 0.8283889161926373, 
                'TOTAL': 12.425833742889559
            }, 
            '2017-05-13': {
                'tax': 0.8269929126304396, 
                'ec2': 0.8269929126304396, 
                'compute': 0.8269929126304396, 
                's3': 0.8269929126304396, 
                'workmail': 0.8269929126304396, 
                'cloudwatch': 0.8269929126304396, 
                'sns': 0.8269929126304396, 
                'route53': 0.8269929126304396, 
                'rds': 0.8269929126304396, 
                'codecommit': 0.8269929126304396, 
                'dynamodb': 0.8269929126304396, 
                'kms': 0.8269929126304396, 
                'cloudfront': 0.8269929126304396, 
                'efs': 0.8269929126304396, 
                'ce': 0.8269929126304396, 
                'TOTAL': 12.404893689456593
            }
        }

        object_return = self.spreadCalculator.get_data()

        self.assertEqual(spread_calculations_get_data_results, object_return)


if __name__ == '__main__':
    unittest.main()
