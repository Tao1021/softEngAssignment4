import unittest
from src.data_scraper import *


class Test(unittest.TestCase):
	
	def test_aws_connection(self):
		myconnection=Connection.connect_to_AWS(self)
		myconnection
		# self.assertTrue(myconnection=="connection succeededT")
	def test_bike_connection(self):

		myconnection=Connection.read_from_dublinbike(self)

		myconnection
	def test_weather_connection(self):

	  	myconnection=Connection.read_from_weather(self)
	  	myconnection
		
if __name__ == "__main__":
	unittest.main()