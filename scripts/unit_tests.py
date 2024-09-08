import unittest
import pandas as pd

class TestDataValidation(unittest.TestCase):

    def setUp(self):
      
        self.data = pd.read_csv('data/data.csv')
        
        self.data['datetime'] = pd.to_datetime(self.data['datetime'], errors='coerce')

    def test_data_types(self):
        self.assertTrue(self.data['open'].dtype == float)
        self.assertTrue(self.data['high'].dtype == float)
        self.assertTrue(self.data['low'].dtype == float)
        self.assertTrue(self.data['close'].dtype == float)
        
    
        self.assertTrue(self.data['volume'].dtype == int)
        
        self.assertTrue(self.data['instrument'].dtype == object)
        
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.data['datetime']))

if __name__ == '__main__':
    unittest.main()
