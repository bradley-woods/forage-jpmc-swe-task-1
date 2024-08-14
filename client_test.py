import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price)/2
      data = stock, bid_price, ask_price, price
      self.assertEqual(getDataPoint(quote), data)
                       
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      price = (bid_price + ask_price)/2
      data = stock, bid_price, ask_price, price
      self.assertEqual(getDataPoint(quote), data)

  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    price_a = 100
    price_b = 99
    self.assertEqual(getRatio(price_a, price_b), price_a/price_b)
  
  
  def test_getRatio_divideByZero(self):
    price_a = 100
    price_b = 0
    with self.assertRaises(ZeroDivisionError):
      getRatio(price_a, price_b)
      

if __name__ == '__main__':
    unittest.main()
