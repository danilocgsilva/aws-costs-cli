import unittest
from aws_costs_cli.CSV import CSV

class test_CSV(unittest.TestCase):
    
    def setUp(self):
        self.csv = CSV()

    def test_get(self):
        self.assertEqual(self.csv.get(), "Hello world!")