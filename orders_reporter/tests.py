import unittest
from .models import *

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        add_data = Manufacturer.objects.create(item="test", quantity=3,
                                               date_of_production='2022-12-12',
                                               sku='1000-000-0000', location='TEST-12')
        self.data = Manufacturer.objects.get(item='test')
    
    def tearDown(self):
        self.data.delete()
    
    def test_data_added(self):
        self.assertEqual(self.data.item, "test")
        self.assertEqual(self.data.quantity, 3)
        self.assertEqual(self.data.sku, '1000-000-0000')
        self.assertEqual(self.data.location, 'TEST-12')

if __name__ == '__main__':
    unittest.main()





