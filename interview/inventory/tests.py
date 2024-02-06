from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Inventory
from .serializers import InventorySerializer

class InventoryFactory:
    def __init__(self):
        '''
        Pass in the required fields to create an Inventory object
        because the Inventory model has required fields and our test is 
        just for ListAfterDateView, we don't need to pass in all the fields
        '''
        pass 
    
class TestInventoryListAfterDateView(TestCase):
    def setUp(self):
        # Create test data using the InventoryFactory
        self.inventory1 = InventoryFactory()
        self.inventory2 = InventoryFactory()

    def test_get_inventory_list_after_date(self):
        client = APIClient()
        date = '2023-01-01' 

        # Make GET request with date parameter
        response = client.get(f'/inventory/inventory-after-date/?date={date}')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_missing_date_parameter(self):
        client = APIClient()

        # Make GET request without date parameter
        response = client.get('/inventory/inventory-after-date/')        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
