import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    #passing individual quotes to the getDataPoint function to verify if the function is working properly
    for quote in quotes:
       #note the return value of the getDataPoint function is a tuple and not list
       self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)) #asserts if the two values passed to it are equal or not
       #each individual value that is returned is asserted in the same order with the correct values

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
        #passing individual quotes to the getDataPoint function to verify if the function is working properly
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)) #asserts if the two values passed to it are equal or not
       #each individual value that is returned is asserted in the same order with the correct values


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidEqualToAsk(self):
      quotes = [
        {'top_ask': {'price': 119.2, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 119.2, 'size': 109}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'DEF'}
      ]
      """ ------------ Add the assertion below ------------ """
          #passing individual quotes to the getDataPoint function to verify if the function is working properly
      for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'],quote['top_bid']['price'],quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2)) #asserts if the two values passed to it are equal or not
        #each individual value that is returned is asserted in the same order with the correct values

#testing for the getRatio function
  def test_getRatio_Agreater_calculateRatio(self):
    #when a is greater than b
    price_a = 119.2
    price_b = 115.2
    self.assertEqual(getRatio(price_a,price_b),(price_a/price_b)) #asserts if the two values passed to it are equal or not

  def test_getRatio_Bgreater_calculateRatio(self):
    #when b is greater than a
    price_a = 115.2
    price_b = 119.2
    self.assertEqual(getRatio(price_a,price_b),(price_a/price_b)) #asserts if the two values passed to it are equal or not

  def test_getRatio_B_is_O_calculateRatio(self):
    #when b is 0
    price_a = 119.2
    price_b = 0
    self.assertEqual(getRatio(price_a,price_b),None) #since it returns nothing, we assert it to None

if __name__ == '__main__':
    unittest.main()
