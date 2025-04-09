import unittest
from aws_costs_cli.CSV import CSV
from aws_costs_api.AWSCosts import AWSCosts
from aws_api_mock.CostExplorer import CostExplorer

class test_CSV(unittest.TestCase):
    
    def setUp(self):
        self.csv = CSV()

    def test_get(self):

        awsCostExplorerMock = CostExplorer()
        awsCosts = AWSCosts(awsCostExplorerMock)
        self.csv.setAWSCostsClass(awsCosts)
        
        expected_string = '''2017-05-09 - 2017-05-09,0.5065006818156758
2017-05-10 - 2017-05-10,0.9377686945149113
2017-05-11 - 2017-05-11,0.8457328317673153
2017-05-12 - 2017-05-12,0.8283889161926373
2017-05-13 - 2017-05-13,0.8269929126304396
2017-05-14 - 2017-05-14,0.9381509479737521
2017-05-15 - 2017-05-15,0.8283510952889606
2017-05-16 - 2017-05-16,0.8282376282065929
2017-05-17 - 2017-05-17,0.8281756901483336
2017-05-18 - 2017-05-18,0.8282642744114878
'''
        
        returned_string = self.csv.get()
        
        self.assertEqual(returned_string, expected_string)
        
if __name__ == '__main__':
    unittest.main()
