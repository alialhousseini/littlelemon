from django.test import TestCase
from .models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .serializers import MenuItemSerializer
from django.test import TestCase, RequestFactory
from restaurant.views import MenuItemsView

class MenuTest(TestCase):
    
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")
        

mocks = [
    {
        'title' : 'Couscous',
        'price' : 25.49,
        'inventory' : 5,
    },
    {
        'title' : 'Tajine',
        'price' : 17.99,
        'inventory' : 4,
    },
    {
        'title' : 'Tanjia',
        'price' : 15.99,
        'inventory' : 4,
    },
]


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title='food_one', price='13.00', inventory=5)
        self.item2 = Menu.objects.create(title='food_two', price='17.00', inventory=10)
        self.item3 = Menu.objects.create(title='food_tree', price='5.99', inventory=15)


    def test_get_all_menu(self):
        food_one = Menu.objects.get(title='food_one')
        food_two = Menu.objects.get(title='food_two')
        food_tree = Menu.objects.get(title='food_tree')

        self.assertEqual(str(food_one), 'food_one : 13.00')
        self.assertEqual(str(food_two), 'food_two : 17.00')
        self.assertNotEqual(str(food_tree), 'food_tree : 10.00')