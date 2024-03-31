import unittest
from financial_data import FinancialData

class TestFinancialData(unittest.TestCase):
    def setUp(self):
        # Initialize the FinancialData object with a sample asset
        self.asset = FinancialData('AAPL')

    def test_get_price(self):
        # Test the get_price method
        price = self.asset.get_price()
        self.assertIsInstance(price, float)
        self.assertGreater(price, 0)

    def test_get_volume(self):
        # Test the get_volume method
        volume = self.asset.get_volume()
        self.assertIsInstance(volume, int)
        self.assertGreater(volume, 0)

    def test_get_returns(self):
        # Test the get_returns method
        returns = self.asset.get_returns()
        self.assertIsInstance(returns, float)

if __name__ == '__main__':
    unittest.main()