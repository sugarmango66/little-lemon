from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        #Define an instance method that adds a new instance of the Menu model. 
        item = Menu.objects.create(title="tea", price=12.5, inventory=6)
        #Call the assertEqual() method of the test class that 
        # compares the string representation of the newly added object
        # with the anticipated value.
        self.assertEqual(item.get_item(), "tea: 12.5")