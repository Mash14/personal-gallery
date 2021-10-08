from django.test import TestCase
from .models import Location

# Create your tests here.

class LocationTestCase(TestCase):

    #setUp method
    def setUp(self):
        self.new_location = Location(location = 'Nairobi')

    def tearDown(self):
        Location.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing instance variables
    def test_check_instance_variables(self):
        self.assertEquals(self.new_location.location,'Nairobi')

     # Test Save Method
    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Test update method
    def test_update_method(self):
        self.new_location.save_location()
        id = self.new_location.id
        Location.update_location(id, 'Mombasa')
        self.assertEqual(self.new_location.location, 'Mombasa')

    # Test delete method
    def test_delete_method(self):
        self.new_location.save_location()
        self.new_location.delete_location(id)
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

     