from django.test import TestCase
from .models import Location,Category

# Create your tests here.

class LocationTestCase(TestCase):

    #setUp method
    def setUp(self):
        self.new_location = Location(location = 'Nairobi')

    # tearDown method
    def tearDown(self):
        Location.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    # Testing instance variables
    def test_check_instance_variables(self):
        self.assertEquals(self.new_location.location, 'Nairobi')

    # Test Save Method
    def test_save_method(self):
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # Test update method
    def test_update_method(self):
        self.new_location.save_location()
        location_id = self.new_location.id
        Location.update_location(location_id, 'Mombasa')
        self.assertEquals(self.new_location.location, 'Mombasa')

    # Test delete method
    def test_delete_method(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class CategoryTestClass(TestCase):

    #setUp method
    def setUp(self):
        self.new_category = Category(category = 'Travel')

    # tearDown method
    def tearDown(self):
        Category.objects.all().delete()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    # Testing instance variables
    def test_check_instance_variables(self):
        self.assertEquals(self.new_category.category, 'Travel')

    # Test Save Method
    def test_save_method(self):
        self.new_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    # Test update method
    def test_update_method(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        Category.update_category(category_id, 'Food')
        self.assertEquals(self.new_category.category, 'Food')

     # Test delete method
    def test_delete_method(self):
        self.new_category.save_category()
        category_id = self.new_category.id
        self.new_category.delete_category(category_id)
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)